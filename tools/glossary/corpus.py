"""Вспомогательный корпус для глоссария (этап 3): RU ↔ старый EN по всем главам частей I–III, выровненный АВТОМАТИЧЕСКИ.

Нужен только для поиска доказательств: как термин или имя передан в старом переводе, где встречается впервые, в каком
контексте. Выравнивание не проверено, текст в content/ не пишется — кэш в .cache/corpus/ (не коммитится).
RU-ID совпадают с теми, что даст извлечение этапа 1а (тот же порядок абзацев). Часть III с гл. 10 — из нового Vol3
без диагностики слитного текста (DEC-020): ≈1% слов слиплось, для поиска терминов это допустимо.

    python -m tools.glossary.corpus build                 # один раз, ~несколько минут
    python -m tools.glossary.corpus find 'самооблад' [--en 'self-(control|possession)'] [--limit 20]
    python -m tools.glossary.corpus count 'самооблад'      # вхождения по частям + первое ID
"""
from __future__ import annotations

import argparse
import functools
import json
import re

import pymupdf

from tools.align import legacy_en as al
from tools.extract import legacy_en_pdf as lp
from tools.extract import ru_epub
from tools.pylib.bookfmt import ROOT, chapter_id, para_id

CACHE = ROOT / ".cache/corpus"
NEW_VOL3 = "sources/en-legacy/New/TwoLives-Vol3.pdf"


def legacy_blocks(part: int, number: int) -> list[str]:
    """Извлечение старого EN тем же кодом, что этап 1б, но без записи файлов и без сверки pypdf."""
    got = []
    lp.dump_chapter = lambda ch: got.append(ch) or ""
    lp.write = lambda *a, **k: None
    lp.crosscheck = lambda *a, **k: ""
    lp.sha256_text = lambda *a, **k: ""
    lp.print = lambda *a, **k: None
    lp.SOURCES = {**lp.SOURCES, 3: lp.SOURCES[3] if number <= 9 else NEW_VOL3}
    lp.extract(part, number)
    return [b.text for b in got[0].blocks]


def build() -> None:
    CACHE.mkdir(parents=True, exist_ok=True)
    lp.read_lines = functools.lru_cache(maxsize=4)(lp.read_lines.__wrapped__ if hasattr(lp.read_lines, "__wrapped__") else lp.read_lines)
    opened: dict[str, pymupdf.Document] = {}
    real_open = pymupdf.open
    lp.pymupdf.open = lambda p: opened.setdefault(str(p), real_open(p))  # один объект на PDF → кэш строк работает
    for part in (1, 2, 3):
        for c in ru_epub.read_part(part):
            cid = chapter_id(part, c.number)
            ru = c.paragraphs
            try:
                en = legacy_blocks(part, c.number)
            except StopIteration:
                print(cid, "EN: глава не найдена")
                en = []
            ratio = sum(map(al.plen, en)) / max(1, sum(map(al.plen, ru)))
            path = al.align(ru, en, ratio) if en else [(0, len(ru), 0, 0, 0.0)]
            links = [{"ru_ids": [para_id(part, c.number, i + 1) for i in range(a1, a2)],
                      "ru": "\n".join(ru[a1:a2]), "en": "\n".join(en[b1:b2]), "cost": round(cost, 2)}
                     for a1, a2, b1, b2, cost in path]
            (CACHE / f"{cid}.json").write_text(json.dumps({"chapter": cid, "title": c.title, "links": links},
                                                          ensure_ascii=False), encoding="utf-8")
            print(cid, len(ru), "RU /", len(en), "EN")


def links():
    """Связи по порядку; к каждой добавлено поле en_near — EN соседних связей (автовыравнивание может сдвигаться)."""
    for p in sorted(CACHE.glob("p*-c*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        ls = d["links"]
        for k, l in enumerate(ls):
            l["en_near"] = "\n".join(x["en"] for x in ls[max(0, k - 1):k + 2])
            yield d["chapter"], l


def find(rx_ru: str, rx_en: str | None, limit: int, width: int) -> None:
    r, e = re.compile(rx_ru, re.I), re.compile(rx_en, re.I) if rx_en else None
    n = 0
    for cid, l in links():
        m = r.search(l["ru"])
        if not m or (e and not e.search(l["en_near"])):
            continue
        n += 1
        if n <= limit:
            s = max(0, m.start() - width)
            print(f"== {l['ru_ids'][0]}  RU: …{l['ru'][s:m.end() + width]}…")
            en = l["en_near"] if e else l["en"]
            if e and (me := e.search(en)):
                s = max(0, me.start() - width)
                print(f"   EN: …{en[s:me.end() + width]}…")
            else:
                print(f"   EN: {en[:2 * width + 60]}…")
    print(f"всего связей: {n}")


def count(rx: str) -> None:
    r = re.compile(rx, re.I)
    per, first = {1: 0, 2: 0, 3: 0}, None
    for cid, l in links():
        k = len(r.findall(l["ru"]))
        if k:
            per[int(cid[1])] += k
            first = first or l["ru_ids"][0]
    print(f"RU {rx}: ч.I {per[1]}, ч.II {per[2]}, ч.III {per[3]}; первое: {first}")


def main() -> None:
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    sp.add_parser("build")
    f = sp.add_parser("find")
    f.add_argument("ru")
    f.add_argument("--en")
    f.add_argument("--limit", type=int, default=15)
    f.add_argument("--width", type=int, default=80)
    c = sp.add_parser("count")
    c.add_argument("ru")
    a = ap.parse_args()
    if a.cmd == "build":
        build()
    elif a.cmd == "find":
        find(a.ru, a.en, a.limit, a.width)
    else:
        count(a.ru)


if __name__ == "__main__":
    main()
