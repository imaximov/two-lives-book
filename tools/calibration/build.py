"""Сборка калибровочного набора: translation/calibration/passages.yml → translation/calibration/<id>.md.

Для каждого отрывка: RU-абзацы и старый EN, разложенный по блокам с каноническими ID (как в главах).
Требования: все связи в окне и контексте проверены вручную (review: done); границы окна и контекста
не режут связи.

    python -m tools.calibration.build
"""
from __future__ import annotations

import yaml

from tools.align.layout import MISSING, layout
from tools.pylib.bookfmt import ROOT, chapter_path, load_chapter, rel, sha256_text, write

CAL = ROOT / "translation/calibration"


def num(ref: str) -> int:
    return int(ref.split("-")[-1].split(".")[0].rstrip("abcdefghijklmnopqrstuvwxyz"))


def render_links(links, ru, en, prev_ref):
    lines, ru_words, en_words = [], 0, 0
    for l in links:
        lines.append("RU:")
        for r in l["ru"]:
            lines.append("{#" + r + "} " + ru[r])
            ru_words += len(ru[r].split())
        lines.append("")
        lines.append("EN (старый перевод):")
        for lid, ids in layout(l, prev_ref):
            text = MISSING if lid is None else en[lid]
            lines.append("{#" + " ".join(ids) + "} " + text)
            en_words += 0 if lid is None else len(text.split())
            prev_ref = ids[-1]
        lines.append("")
        lines.append("---")
        lines.append("")
    return lines, ru_words, en_words, prev_ref


def build(p: dict) -> dict:
    cid = p["chapter"]
    part, chap = int(cid[1]), int(cid[4:6])
    ru_path = chapter_path("content/ru", part, chap)
    raw_path = chapter_path("translation/legacy-en/raw", part, chap)
    al_path = ROOT / "translation/legacy-en/alignment" / f"{cid}.yml"
    al = yaml.safe_load(al_path.read_text(encoding="utf-8"))
    if sha256_text(ru_path) != al["ru_sha256"] or sha256_text(raw_path) != al["en_raw_sha256"]:
        raise SystemExit(f"{cid}: тексты изменились после выравнивания")
    ru = {b.ids[0]: b.text for b in load_chapter(ru_path).blocks}
    en = {b.ids[0]: b.text for b in load_chapter(raw_path).blocks}
    (w1, w2), (c1, c2) = p["window"], p["context"]

    sections = {"before": [], "window": [], "after": []}
    prev_ref, started = None, False
    for l in al["links"]:
        if not l["ru"]:
            if started and sections["window"] and not sections["after"]:
                raise SystemExit(f"{cid}: связь без RU внутри окна — нужна ручная проверка")
            continue
        a, b = num(l["ru"][0]), num(l["ru"][-1])
        if b < c1 or a > c2:
            prev_ref = l["ru"][-1] if not started else prev_ref
            continue
        started = True
        if l.get("review") != "done":
            raise SystemExit(f"{cid}: связь {l['ru']}↔{l['en']} в окне/контексте не проверена")
        where = "before" if b < w1 else "after" if a > w2 else "window"
        if where == "window" and (a < w1 or b > w2):
            raise SystemExit(f"{cid}: граница окна {w1}–{w2} режет связь {l['ru']}↔{l['en']}")
        if (a < c1 or b > c2):
            raise SystemExit(f"{cid}: граница контекста {c1}–{c2} режет связь {l['ru']}↔{l['en']}")
        sections[where].append(l)

    out_lines, stats, prev = [], {}, prev_ref
    for key, title in (("before", "Контекст до (не оценивается)"), ("window", "Отрывок"),
                       ("after", "Контекст после (не оценивается)")):
        body, rw, ew, prev = render_links(sections[key], ru, en, prev)
        stats[key] = (rw, ew)
        out_lines += [f"## {title}", ""] + body
    meta = {"id": p["id"], "chapter": cid, "genre": p["genre"],
            "window": [f"{cid}-{w1:03d}", f"{cid}-{w2:03d}"], "context": [f"{cid}-{c1:03d}", f"{cid}-{c2:03d}"],
            "words_ru": stats["window"][0], "words_en_legacy": stats["window"][1],
            "evaluate": p.get("evaluate", "prose"),
            "sources": {"ru": rel(ru_path), "ru_sha256": al["ru_sha256"],
                        "en_raw": rel(raw_path), "en_raw_sha256": al["en_raw_sha256"],
                        "alignment": rel(al_path), "alignment_sha256": sha256_text(al_path)}}
    head = yaml.safe_dump(meta, allow_unicode=True, sort_keys=False, width=200).strip()
    doc = [f"---\n{head}\n---", "", f"# {p['id']}: {p['genre']}", "", f"Зачем: {p['why']}", ""] + out_lines
    write(CAL / f"{p['id']}.md", "\n".join(doc).rstrip() + "\n")
    return meta


def main() -> None:
    spec = yaml.safe_load((CAL / "passages.yml").read_text(encoding="utf-8"))
    rows = []
    for p in spec["passages"]:
        m = build(p)
        rows.append(f"| [{m['id']}]({m['id']}.md) | {m['chapter']} | {m['window'][0][-3:]}–{m['window'][1][-3:]} | "
                    f"{m['words_ru']} | {m['words_en_legacy']} | {m['evaluate']} | {p['genre']} |")
        print(m["id"], m["words_ru"], m["words_en_legacy"])
    index = CAL / "README.md"
    text = index.read_text(encoding="utf-8") if index.exists() else ""
    table = "\n".join(["<!-- table:start -->", "| Отрывок | Глава | Абзацы RU | Слов RU | Слов EN (старый) | Оценка | Жанр |",
                       "|---|---|---|---|---|---|---|"] + rows + ["<!-- table:end -->"])
    if "<!-- table:start -->" in text:
        text = text.split("<!-- table:start -->")[0] + table + text.split("<!-- table:end -->")[1]
    else:
        text += "\n" + table + "\n"
    index.write_text(text, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
