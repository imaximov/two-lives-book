"""1б. Старый английский перевод: PDF → translation/legacy-en/raw/part-N/ch-NN.md (+ отчёт).

Слова и пунктуация не меняются. Только техника (каждый случай — в отчёте):
склейка строк в абзацы, границы абзацев по отступу первой строки и интервалу, курсив → *…*.
Абзацы нумеруются по порядку в PDF: L001, L002, …

    python -m tools.extract.legacy_en_pdf --part 1 --chapter 1
"""
from __future__ import annotations

import argparse
import re
from collections import Counter
from dataclasses import dataclass

import difflib

import pymupdf
import pypdf

from tools.pylib.bookfmt import (ROOT, Block, Chapter, chapter_id, chapter_path, dump_chapter, rel, sha256_file,
                                 sha256_text, verse, write)

# Какой PDF для какой части (INVENTORY §3, DEC-010). Для части III понадобится диагностика
# слитного текста (DEC-020) — до неё извлечение части III не запускаем.
SOURCES = {1: "sources/en-legacy/TwoLives-Vol1-2018-part1.pdf",
           2: "sources/en-legacy/TwoLives-Vol2-2021-part2.pdf",
           # гл. 1–9 части III — из чистого PDF 2022 года (текст тот же, что в новом Vol3, DEC-010)
           3: "sources/en-legacy/TwoLives-Vol3-2022-part3-ch1-10.pdf"}
MAX_CHAPTER = {3: 9}  # дальше — новый Vol3 после диагностики слитного текста (DEC-020)

HEADING_SIZE = 14.0      # заголовки глав — 16 pt, основной текст — 11 pt
INDENT_MIN = 120.0       # левое поле ≈85, отступ первой строки ≈150
GAP_FACTOR = 1.35        # интервал между абзацами ≈22.5 при межстрочном ≈14.5


@dataclass
class Line:
    page: int
    x0: float
    y0: float
    y1: float
    size: float
    text: str        # с разметкой курсива
    plain: str


def read_lines(pdf: pymupdf.Document) -> list[Line]:
    out = []
    for pno, page in enumerate(pdf):
        for block in page.get_text("dict")["blocks"]:
            for l in block.get("lines", []):
                parts, plain = [], []
                for s in l["spans"]:
                    t = s["text"]
                    plain.append(t)
                    italic = bool(s["flags"] & 2) or "Italic" in s["font"]
                    parts.append(f"*{t.strip()}* " if italic and t.strip() else t)
                txt, pl = "".join(parts), "".join(plain)
                if not pl.strip():
                    continue
                size = max(s["size"] for s in l["spans"])
                out.append(Line(pno, l["bbox"][0], l["bbox"][1], l["bbox"][3], size, txt, pl))
    return out


def find_chapter(lines: list[Line], number: int) -> tuple[int, int]:
    def is_head(l: Line, n: int) -> bool:
        return l.size >= HEADING_SIZE and re.fullmatch(rf"\s*Chapter\s+{n}\s*", l.plain) is not None
    start = next(i for i, l in enumerate(lines) if is_head(l, number))
    end = next((i for i, l in enumerate(lines[start + 1:], start + 1)
                if is_head(l, number + 1) or re.search(r"The end of (part|volume)", l.plain)), len(lines))
    return start, end


def crosscheck(src, first_page: int, last_page: int, title: str, number: int, texts: list[str]) -> str:
    """Независимая сверка слов с другим извлекателем (pypdf): ничего не потеряно и не добавлено."""
    reader = pypdf.PdfReader(str(src))
    raw = "\n".join(reader.pages[i].extract_text() for i in range(first_page, last_page + 1))
    m = re.search(r"\s+".join(map(re.escape, title.split())), raw)  # название может занимать несколько строк
    raw = raw[m.end():] if m else raw
    raw = re.split(rf"Chapter\s+{number + 1}\b|The end of (?:part|volume)", raw)[0]
    tok = lambda t: re.findall(r"[\w’']+", re.sub(r"::: verse|:::", " ", t).replace("*", ""))
    ours, theirs = tok(" ".join(texts)), tok(raw)
    sm = difflib.SequenceMatcher(None, ours, theirs, autojunk=False)
    diffs = [o for o in sm.get_opcodes() if o[0] != "equal"]
    res = f"- Сверка с pypdf: слов {len(ours)} / {len(theirs)}, совпадение {sm.ratio():.5f}, расхождений {len(diffs)}"
    for tag, i1, i2, j1, j2 in diffs[:30]:
        res += f"\n  - {tag}: «{' '.join(ours[i1:i2])}» | pypdf «{' '.join(theirs[j1:j2])}»"
    return res


def extract(part: int, number: int) -> None:
    src = ROOT / SOURCES[part]
    pdf = pymupdf.open(src)
    lines = read_lines(pdf)
    start, end = find_chapter(lines, number)
    i = start + 1
    title_lines = []
    while i < end and lines[i].size >= HEADING_SIZE:
        title_lines.append(lines[i].plain.strip())
        i += 1
    body = lines[i:end]

    line_h = Counter(round(b.y0 - a.y0, 1) for a, b in zip(body, body[1:])
                     if a.page == b.page and 0 < b.y0 - a.y0 < 30).most_common(1)[0][0]
    xs = Counter(round(l.x0) for l in body)
    paras: list[list[Line]] = []
    odd_x, hyphen_joins, italic_lines = [], [], 0
    prev: Line | None = None
    for l in body:
        new = prev is None or l.x0 >= INDENT_MIN or (l.page == prev.page and l.y0 - prev.y0 > line_h * GAP_FACTOR)
        if new:
            paras.append([l])
        else:
            paras[-1].append(l)
        if round(l.x0) not in (min(xs), max(xs, key=lambda x: xs[x] if x > INDENT_MIN else -1)):
            odd_x.append(l)
        if "*" in l.text:
            italic_lines += 1
        prev = l

    # Стихи: подряд идущие однострочные абзацы, целиком набранные курсивом → один блок verse
    grouped: list = []
    for p in paras:
        t = p[0].text.strip()
        if len(p) == 1 and len(t) > 2 and t.startswith("*") and t.endswith("*") and t.count("*") == 2:
            if grouped and isinstance(grouped[-1], tuple):
                grouped[-1][1].append(p[0])
            else:
                grouped.append(("verse", [p[0]]))
        else:
            grouped.append(p)
    grouped = [g[1] if isinstance(g, tuple) and len(g[1]) == 1 else g for g in grouped]  # одна строка — не стих

    texts, verse_blocks, italic_merges = [], 0, 0
    for p in grouped:
        if isinstance(p, tuple):
            texts.append(verse([l.text.strip() for l in p[1]]))
            verse_blocks += 1
            continue
        acc = ""
        for l in p:
            t = l.text.strip()
            if not acc:
                acc = t
            elif acc.endswith("-") and not acc.endswith(" -"):
                hyphen_joins.append(f"стр. {l.page + 1}: «…{acc[-25:]}» + «{t[:25]}…»")
                acc += t          # дефис на конце строки сохраняется (Word не переносит слова)
            else:
                acc += " " + t
        t = re.sub(r"\s+", " ", acc).strip()
        # курсив размечается по фрагментам строк: «*a* *b*» → «*a b*» (соседние курсивные куски)
        t, n = re.subn(r"\*\s+\*", " ", t)
        italic_merges += n
        texts.append(t)

    cid = chapter_id(part, number)
    ch = Chapter(meta={"id": cid, "lang": "en", "kind": "legacy-raw", "source": SOURCES[part],
                       "source_sha256": sha256_file(src),
                       "pages": f"{lines[start].page + 1}-{body[-1].page + 1}",
                       "legacy_heading": lines[start].plain.strip(), "legacy_title": " ".join(title_lines)})
    ch.blocks = [Block([f"L{n:03d}"], t) for n, t in enumerate(texts, 1)]
    out = chapter_path("translation/legacy-en/raw", part, number)
    write(out, dump_chapter(ch))

    rep = [f"# Извлечение старого EN (без правок): {cid}", "",
           f"- Источник: `{SOURCES[part]}` (sha256 `{sha256_file(src)}`), страницы {ch.meta['pages']} (нумерация с 1)",
           f"- Результат: `{rel(out)}` (sha256 текста, LF: `{sha256_text(out)}`)",
           f"- Заголовок в PDF: «{ch.meta['legacy_heading']}» / «{ch.meta['legacy_title']}»",
           f"- Строк текста: {len(body)}; абзацев: {len(texts)}; слов: {sum(len(t.split()) for t in texts)}",
           f"- Межстрочный интервал: {line_h}; новый абзац — отступ первой строки (x ≥ {INDENT_MIN}) или интервал > {GAP_FACTOR}×",
           f"- Левые позиции строк (x → число строк): {dict(sorted(xs.items()))}", "",
           "## Технические действия", "",
           f"- Строки склеены в абзацы через пробел: {sum(len(p) - 1 for p in grouped if not isinstance(p, tuple))} стыков.",
           f"- Стихотворных блоков (однострочные курсивные абзацы подряд → `::: verse`, переносы строк сохранены): {verse_blocks}",
           f"- Стыков с дефисом на конце строки (дефис сохранён, без пробела): {len(hyphen_joins)}"]
    rep += [f"  - {h}" for h in hyphen_joins]
    rep += [f"- Строк с курсивом (размечен `*…*`): {italic_lines}; склеено соседних курсивных фрагментов: {italic_merges}",
            f"- Строк с нетипичным левым краем: {len(odd_x)}"]
    rep_x = [f"  - стр. {l.page + 1}, x={l.x0:.1f}: «{l.plain.strip()[:70]}»" for l in odd_x]
    rep += rep_x + ["", "## Контроль", "",
                    crosscheck(src, lines[start].page, body[-1].page, ch.meta["legacy_title"], number, texts)]
    write(ROOT / "translation/reports/extract-legacy-en" / f"{cid}.md", "\n".join(rep) + "\n")
    print(rel(out), len(texts), "абзацев")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--part", type=int, required=True)
    ap.add_argument("--chapter", type=int, required=True)
    a = ap.parse_args()
    if a.part not in SOURCES or a.chapter > MAX_CHAPTER.get(a.part, 999):
        raise SystemExit(f"p{a.part}-c{a.chapter:02d}: извлечение ещё не подготовлено (часть III с гл. 10 — после DEC-020)")
    extract(a.part, a.chapter)


if __name__ == "__main__":
    main()
