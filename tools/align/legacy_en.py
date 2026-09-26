"""1в. Выравнивание старого EN (raw, абзацы L…) с каноническими ID оригинала.

Динамическое программирование по «бусинам» (1:1, 1:2, 2:1, 2:2, 1:3, 3:1, 1:0, 0:1) с ценой
из отношения длин и совпадения признаков (реплика диалога, вопросы, восклицания, числа).
Всё, что не 1:1 или выглядит сомнительно, помечается `review: needed` — это проверяет человек
или агент, читая оба текста, и ставит `review: done` с примечанием.

Проверенные связи (`review: done`) — опоры: при повторном запуске они сохраняются, а автомат
перевыравнивает только промежутки между ними. Поле `reviewed` в файле: `full` — проверена вся глава
(только такую можно импортировать), иначе — список проверенных окон.

    python -m tools.align.legacy_en --part 1 --chapter 1          # создать или перевыровнять вокруг опор
    python -m tools.align.legacy_en --part 1 --chapter 1 --force  # с нуля, ручные правки теряются
"""
from __future__ import annotations

import argparse
import math
import re

import yaml

from tools.pylib.bookfmt import ROOT, chapter_id, chapter_path, load_chapter, rel, sha256_text, write

BEADS = {(1, 1): 0.0, (1, 2): 3.0, (2, 1): 3.0, (2, 2): 5.0, (1, 3): 6.0, (3, 1): 6.0, (1, 0): 9.0, (0, 1): 9.0}
SIGMA2 = 0.06            # дисперсия log(отношения длин) для 1:1
SUSPICIOUS_LOG = 0.40    # |log(факт/ожидание)| выше этого — на проверку


def plen(t: str) -> int:
    return len(re.sub(r"\s", "", t))


def features(t: str, lang: str) -> dict:
    s = t.lstrip("*")
    return {"dialog": s.startswith(("—", "–", "-")) if lang == "ru" else s.startswith(("“", '"', "‘")),
            "q": t.count("?"), "ex": t.count("!"),
            "num": sorted(re.findall(r"\d+", t))}


def bead_cost(ru: list[str], en: list[str], ratio: float) -> float:
    if not ru or not en:
        return 0.0
    a, b = sum(map(plen, ru)), sum(map(plen, en))
    c = math.log((b + 10) / (ratio * a + 10)) ** 2 / SIGMA2
    fr, fe = features(ru[0], "ru"), features(en[0], "en")
    c += 2.0 * (fr["dialog"] != fe["dialog"])
    q_ru = sum(features(t, "ru")["q"] for t in ru)
    q_en = sum(features(t, "en")["q"] for t in en)
    c += 0.7 * abs(q_ru - q_en)
    n_ru = sorted(sum((features(t, "ru")["num"] for t in ru), []))
    n_en = sorted(sum((features(t, "en")["num"] for t in en), []))
    c += 1.5 * (n_ru != n_en)
    return c


def align(ru: list[str], en: list[str], ratio: float) -> list[tuple[int, int, int, int, float]]:
    n, m = len(ru), len(en)
    INF = float("inf")
    cost = [[INF] * (m + 1) for _ in range(n + 1)]
    back = [[None] * (m + 1) for _ in range(n + 1)]
    cost[0][0] = 0.0
    for i in range(n + 1):
        for j in range(m + 1):
            if cost[i][j] == INF:
                continue
            for (di, dj), pen in BEADS.items():
                ni, nj = i + di, j + dj
                if ni > n or nj > m:
                    continue
                c = cost[i][j] + pen + bead_cost(ru[i:ni], en[j:nj], ratio)
                if c < cost[ni][nj]:
                    cost[ni][nj] = c
                    back[ni][nj] = (i, j)
    path, i, j = [], n, m
    while (i, j) != (0, 0):
        pi, pj = back[i][j]
        path.append((pi, i, pj, j, bead_cost(ru[pi:i], en[pj:j], ratio)))
        i, j = pi, pj
    return path[::-1]


def make_link(ru_blocks, en_blocks, i1, i2, j1, j2, cost, ratio) -> dict:
    kind = f"{i2 - i1}:{j2 - j1}"
    ru_txt = " ".join(b.text for b in ru_blocks[i1:i2])
    en_txt = " ".join(b.text for b in en_blocks[j1:j2])
    dev = abs(math.log((plen(en_txt) + 10) / (ratio * plen(ru_txt) + 10))) if ru_txt and en_txt else None
    link = {"ru": [b.ids[0] for b in ru_blocks[i1:i2]], "en": [b.ids[0] for b in en_blocks[j1:j2]],
            "type": kind, "cost": round(cost, 2)}
    if kind != "1:1" or (dev is not None and dev > SUSPICIOUS_LOG) or cost > 4.0:
        link["review"] = "needed"
    return link


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--part", type=int, required=True)
    ap.add_argument("--chapter", type=int, required=True)
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    cid = chapter_id(a.part, a.chapter)
    out = ROOT / "translation/legacy-en/alignment" / f"{cid}.yml"
    old = yaml.safe_load(out.read_text(encoding="utf-8")) if out.exists() and not a.force else None
    ru_path = chapter_path("content/ru", a.part, a.chapter)
    en_path = chapter_path("translation/legacy-en/raw", a.part, a.chapter)
    ru, en = load_chapter(ru_path), load_chapter(en_path)
    ru_idx = {b.ids[0]: i for i, b in enumerate(ru.blocks)}
    en_idx = {b.ids[0]: j for j, b in enumerate(en.blocks)}
    ratio = sum(plen(b.text) for b in en.blocks) / sum(plen(b.text) for b in ru.blocks)
    anchors = [l for l in (old or {}).get("links", []) if l.get("review") == "done"]

    links: list[dict] = []
    i0 = j0 = 0

    def fill_gap(i1: int, j1: int) -> None:
        if i1 == i0 and j1 == j0:
            return
        if i1 == i0 or j1 == j0:  # с одной стороны пусто
            links.append(make_link(ru.blocks, en.blocks, i0, i1, j0, j1, 0.0, ratio))
            return
        path = align([b.text for b in ru.blocks[i0:i1]], [b.text for b in en.blocks[j0:j1]], ratio)
        for a1, a2, b1, b2, c in path:
            links.append(make_link(ru.blocks, en.blocks, i0 + a1, i0 + a2, j0 + b1, j0 + b2, c, ratio))

    for anc in anchors:
        ai = ru_idx[anc["ru"][0]] if anc["ru"] else i0
        aj = en_idx[anc["en"][0]] if anc["en"] else j0
        if ai < i0 or aj < j0:
            raise SystemExit(f"опора {anc['ru']}↔{anc['en']} нарушает порядок — поправьте вручную")
        fill_gap(ai, aj)
        links.append(anc)
        i0 = ai + len(anc["ru"])
        j0 = aj + len(anc["en"])
    fill_gap(len(ru.blocks), len(en.blocks))
    stats: dict = {}
    for l in links:
        stats[l["type"]] = stats.get(l["type"], 0) + 1
    data = {"chapter": cid, "ru": rel(ru_path), "ru_sha256": sha256_text(ru_path),
            "en_raw": rel(en_path), "en_raw_sha256": sha256_text(en_path),
            "method": "auto: DP по длинам и признакам (tools/align/legacy_en.py); проверенные связи — опоры",
            "reviewed": (old or {}).get("reviewed", []),
            "review_note": (old or {}).get("review_note", ""),
            "length_ratio_en_ru": round(ratio, 3), "stats": stats, "links": links}
    write(out, yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=200))
    need = sum(1 for l in links if l.get("review") == "needed")
    print(rel(out), stats, f"на проверку: {need}")


if __name__ == "__main__":
    main()
