"""Сверка извлечённой русской главы с PDF того же издания (sources/ru/original/part-N.pdf).

Сравниваются последовательности слов (без регистра и пунктуации). Результат дописывается в
отчёт translation/reports/extract-ru/<id>.md.

    python -m tools.extract.verify_ru_pdf --part 1 --chapter 1
"""
from __future__ import annotations

import argparse
import difflib
import re

import pymupdf

from tools.pylib.bookfmt import ROOT, chapter_id, chapter_path, load_chapter

PDFS = {1: "sources/ru/original/part-1.pdf", 2: "sources/ru/original/part-2.pdf", 3: "sources/ru/original/part-3.pdf"}


def words(text: str) -> list[str]:
    text = text.replace("\xad", "").replace("ё", "е").replace("Ё", "Е")
    # дефис на переносе строки в PDF неотличим от дефиса в слове («где-то») — дефисы не сравниваем
    text = text.replace("-\n", "").replace("-", "")
    return re.findall(r"\w+", text.lower())


def pdf_chapter_text(part: int, number: int) -> str:
    doc = pymupdf.open(ROOT / PDFS[part])
    full = "\n".join(p.get_text() for p in doc)
    start = re.search(rf"^\s*Глава\s+{number}\b.*$", full, re.M)
    nxt = re.search(rf"^\s*(Глава\s+{number + 1}\b|Том\s+\d|Часть\s+IV).*$", full[start.end():], re.M)
    return full[start.end(): start.end() + nxt.start()] if nxt else full[start.end():]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--part", type=int, required=True)
    ap.add_argument("--chapter", type=int, required=True)
    a = ap.parse_args()
    cid = chapter_id(a.part, a.chapter)
    ch = load_chapter(chapter_path("content/ru", a.part, a.chapter))
    ours = words("\n".join(b.text for b in ch.blocks))
    theirs = words(pdf_chapter_text(a.part, a.chapter))
    # в PDF после заголовка главы может стоять её название — отрезаем по первым словам нашего текста
    head = " ".join(ours[:6])
    joined = " ".join(theirs)
    if head in joined:
        theirs = joined[joined.index(head):].split()
    sm = difflib.SequenceMatcher(None, ours, theirs, autojunk=False)
    diffs = [op for op in sm.get_opcodes() if op[0] != "equal"]
    lines = [f"\n## Сверка с PDF (`{PDFS[a.part]}`)\n",
             f"- Слов: epub {len(ours)}, PDF {len(theirs)}; совпадение последовательностей {sm.ratio():.4f}",
             f"- Расхождений: {len(diffs)}"]
    for tag, i1, i2, j1, j2 in diffs[:50]:
        lines.append(f"  - {tag}: epub «{' '.join(ours[max(0, i1 - 3):i2 + 3])}» | PDF «{' '.join(theirs[max(0, j1 - 3):j2 + 3])}»")
    report = ROOT / "translation/reports/extract-ru" / f"{cid}.md"
    text = report.read_text(encoding="utf-8").split("\n## Сверка с PDF")[0].rstrip("\n") + "\n"
    report.write_text(text + "\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
