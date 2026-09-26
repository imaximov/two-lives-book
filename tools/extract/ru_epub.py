"""1а. Русский оригинал: epub → content/ru/part-N/ch-NN.md (+ content/book.yml, отчёт).

Текст абзацев не меняется. Техническая нормализация (фиксируется в отчёте):
неразрывный пробел → обычный пробел, удаление мягких переносов, схлопывание пробелов.

    python -m tools.extract.ru_epub --part 1 --chapter 1
    python -m tools.extract.ru_epub --part 1            # все главы части
    python -m tools.extract.ru_epub --book-yml          # только структура книги
"""
from __future__ import annotations

import argparse
import re
import warnings
from dataclasses import dataclass, field

import ebooklib
import yaml
from bs4 import BeautifulSoup, NavigableString, Tag
from ebooklib import epub

from tools.pylib.bookfmt import (ROOT, Block, Chapter, chapter_id, chapter_path, dump_chapter, para_id,
                                 rel, sha256_file, write)

warnings.filterwarnings("ignore")

SOURCES = {1: "sources/ru/original/part-1.epub",
           2: "sources/ru/original/part-2.epub",
           3: "sources/ru/original/part-3.epub"}

CHAPTER_RE = re.compile(r"^Глава\s+(\d+)\.?\s*(.*)$")
VOLUME_RE = re.compile(r"^Том\s+([\d-]+)$")
PART4_RE = re.compile(r"^Часть\s+IV\b")


@dataclass
class RawChapter:
    part: int
    number: int
    volume: str
    title: str
    paragraphs: list[str] = field(default_factory=list)
    unsupported: list[str] = field(default_factory=list)
    stats: dict = field(default_factory=lambda: {"nbsp": 0, "soft_hyphen": 0, "whitespace": 0})


def inline_text(node: Tag) -> str:
    out = []
    for ch in node.children:
        if isinstance(ch, NavigableString):
            out.append(str(ch))
        elif ch.name in ("em", "i"):
            out.append("*" + inline_text(ch) + "*")
        elif ch.name in ("strong", "b"):
            out.append("**" + inline_text(ch) + "**")
        elif ch.name == "br":
            out.append(" ")
        else:
            out.append(inline_text(ch))
    return "".join(out)


def normalize(text: str, stats: dict) -> str:
    stats["nbsp"] += text.count("\xa0")
    stats["soft_hyphen"] += text.count("\xad")
    t = text.replace("\xa0", " ").replace("\xad", "")
    t2 = re.sub(r"\s+", " ", t).strip()
    if t2 != t:
        stats["whitespace"] += 1
    return t2


def read_part(part: int) -> list[RawChapter]:
    book = epub.read_epub(str(ROOT / SOURCES[part]))
    chapters: list[RawChapter] = []
    volume = ""
    in_part4 = False  # в конце part-3.epub приложена гл. 1 части IV — в часть III не включаем
    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        soup = BeautifulSoup(item.get_content(), "html.parser")
        body = soup.body
        if body is None:
            continue
        cur: RawChapter | None = None
        for h in body.find_all("h2"):
            text = h.get_text(" ", strip=True).replace("\xa0", " ")
            if PART4_RE.match(text):
                in_part4 = True
            elif m := VOLUME_RE.match(text):
                volume = m.group(1)
            elif m := CHAPTER_RE.match(text):
                title = m.group(2).strip()
                if not title:
                    sub = body.find(class_="subtitle")
                    title = sub.get_text(" ", strip=True) if sub else ""
                cur = RawChapter(part, int(m.group(1)), volume, title)
        if cur is None or in_part4:
            continue
        section = body.find("div", class_="section1") or body
        for node in section.children:
            if not isinstance(node, Tag):
                continue
            classes = node.get("class", [])
            if node.name == "div" and ("title2" in classes or "subtitle" in classes):
                continue
            if node.name == "p" and "empty-line" in classes:
                continue
            if node.name == "p" and "subtitle" in classes:
                continue
            if node.name == "p" and not classes:
                text = normalize(inline_text(node), cur.stats)
                if text:
                    cur.paragraphs.append(text)
                continue
            cur.unsupported.append(f"<{node.name} class={classes}>: {node.get_text(' ', strip=True)[:80]}")
        chapters.append(cur)
    return chapters


def build_book_yml() -> None:
    parts = []
    for part in SOURCES:
        vols: dict[str, list] = {}
        for c in read_part(part):
            vols.setdefault(c.volume, []).append(
                {"id": chapter_id(part, c.number), "number": c.number, "title": {"ru": c.title}})
        parts.append({"part": part, "source": SOURCES[part],
                      "volumes": [{"volume": v, "chapters": chs} for v, chs in vols.items()]})
    parts.append({"part": 4, "note": "в репозитории только гл. 1 (в конце part-3.epub); полный текст не получен (PLAN D7)"})
    data = {"title": {"ru": "Две жизни", "en": "Two Lives"},
            "author": {"ru": "Конкордия Евгеньевна Антарова", "en": "Concordia Antarova"},
            "parts": parts}
    write(ROOT / "content/book.yml", "# Структура книги. Генерируется: python -m tools.extract.ru_epub --book-yml\n"
          + yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=120))
    print("content/book.yml")


def extract(part: int, only: int | None) -> None:
    for c in read_part(part):
        if only is not None and c.number != only:
            continue
        cid = chapter_id(part, c.number)
        if c.unsupported:
            raise SystemExit(f"{cid}: неподдержанные элементы, нужно доработать извлечение:\n  "
                             + "\n  ".join(c.unsupported))
        ch = Chapter(meta={"id": cid, "lang": "ru", "part": part, "volume": c.volume,
                           "chapter": c.number, "title": c.title})
        ch.blocks = [Block([para_id(part, c.number, i)], t) for i, t in enumerate(c.paragraphs, 1)]
        out = chapter_path("content/ru", part, c.number)
        write(out, dump_chapter(ch))
        words = sum(len(t.split()) for t in c.paragraphs)
        report = ROOT / "translation/reports/extract-ru" / f"{cid}.md"
        write(report, f"""# Извлечение RU: {cid}

- Источник: `{SOURCES[part]}` (sha256 `{sha256_file(ROOT / SOURCES[part])}`)
- Результат: `{rel(out)}` (sha256 `{sha256_file(out)}`)
- Том: {c.volume}; заголовок: «{c.title}»
- Абзацев: {len(c.paragraphs)}; слов: {words}

## Техническая нормализация (текст не менялся)

| Что | Сколько |
|---|---|
| неразрывные пробелы → обычные | {c.stats['nbsp']} |
| мягкие переносы удалены | {c.stats['soft_hyphen']} |
| абзацы, где схлопнуты или обрезаны пробелы | {c.stats['whitespace']} |
""")
        print(rel(out), len(c.paragraphs), "абзацев")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--part", type=int)
    ap.add_argument("--chapter", type=int)
    ap.add_argument("--book-yml", action="store_true")
    a = ap.parse_args()
    if a.book_yml:
        build_book_yml()
    if a.part:
        extract(a.part, a.chapter)


if __name__ == "__main__":
    main()
