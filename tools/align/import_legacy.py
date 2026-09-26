"""1в (импорт). raw + alignment → content/en/part-N/ch-NN.md, текст старого перевода без изменений.

Раскладка ID по блокам — tools/align/layout.py.
Импорт запрещён, пока глава не проверена целиком (`reviewed: full`) или есть `review: needed`.

    python -m tools.align.import_legacy --part 1 --chapter 1
"""
from __future__ import annotations

import argparse
from itertools import zip_longest

import yaml

from tools.align.layout import MISSING, layout
from tools.pylib.bookfmt import (ROOT, Block, Chapter, chapter_id, chapter_path, coverage_errors, dump_chapter,
                                 load_chapter, rel, sha256_text, write)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--part", type=int, required=True)
    ap.add_argument("--chapter", type=int, required=True)
    a = ap.parse_args()
    cid = chapter_id(a.part, a.chapter)
    al_path = ROOT / "translation/legacy-en/alignment" / f"{cid}.yml"
    al = yaml.safe_load(al_path.read_text(encoding="utf-8"))
    if al.get("reviewed") != "full":
        raise SystemExit(f"{rel(al_path)}: выравнивание проверено не целиком (reviewed: {al.get('reviewed')!r}) — импорт запрещён")
    pending = [l for l in al["links"] if l.get("review") == "needed"]
    if pending:
        raise SystemExit(f"{rel(al_path)}: {len(pending)} связей ещё не проверены (review: needed)")
    ru = load_chapter(ROOT / al["ru"])
    raw = load_chapter(ROOT / al["en_raw"])
    for key, path in (("ru_sha256", al["ru"]), ("en_raw_sha256", al["en_raw"])):
        if sha256_text(ROOT / path) != al[key]:
            raise SystemExit(f"{path} изменился после выравнивания — выровняйте заново")
    en_text = {b.ids[0]: b.text for b in raw.blocks}

    blocks: list[Block] = []
    for link in al["links"]:
        prev = blocks[-1].ids[-1] if blocks else None
        blocks += [Block(ids, MISSING if lid is None else en_text[lid]) for lid, ids in layout(link, prev)]

    errors = coverage_errors([b.ids[0] for b in ru.blocks], blocks)
    if errors:
        raise SystemExit("нарушен инвариант покрытия:\n  " + "\n  ".join(errors))
    used = sum(len(l["en"]) for l in al["links"])
    if used != len(raw.blocks):
        raise SystemExit(f"использовано {used} абзацев EN из {len(raw.blocks)}")

    # Контроль «текст не менялся» — до записи: блоки по порядку == абзацы raw по порядку
    got = [b.text for b in blocks if b.text != MISSING]
    want = [b.text for b in raw.blocks]
    if got != want:
        bad = next(i for i, (x, y) in enumerate(zip_longest(got, want)) if x != y)
        raise SystemExit(f"текст при импорте изменился бы (первое расхождение на абзаце {bad + 1}) — файл не записан")

    ch = Chapter(meta={"id": cid, "lang": "en", "part": a.part, "volume": ru.meta["volume"],
                       "chapter": a.chapter, "title": raw.meta["legacy_title"]})
    ch.blocks = blocks
    out = chapter_path("content/en", a.part, a.chapter)
    write(out, dump_chapter(ch))
    missing = sum(1 for b in blocks if b.text == MISSING)
    report = ROOT / "translation/reports/align-legacy-en" / f"{cid}.md"
    notes = [f"- {', '.join(x[-3:] for x in l['ru'])} ↔ {', '.join(l['en'])} ({l['type']}): {l['note']}"
             for l in al["links"] if l.get("note") and not l["note"].startswith("проверено вручную")]
    write(report, "\n".join([
        f"# Выравнивание и импорт старого EN: {cid}", "",
        f"- RU: `{al['ru']}` — {len(ru.blocks)} абзацев",
        f"- EN raw: `{al['en_raw']}` — {len(raw.blocks)} абзацев",
        f"- Выравнивание: `{rel(al_path)}` — {al['method']}",
        f"- Типы связей: {al['stats']}",
        f"- Доля 1:1: {al['stats'].get('1:1', 0)} из {len(al['links'])} связей",
        f"- Импорт: `{rel(out)}` — {len(blocks)} блоков, «⟦missing⟧»: {missing}",
        "- Инвариант покрытия: выполнен; текст при импорте не менялся (проверено).", "",
        "## Примечания к связям", ""] + notes) + "\n")
    print(rel(out), len(blocks), "блоков; missing:", missing)


if __name__ == "__main__":
    main()
