"""Общий формат текстов проекта (docs/ARCHITECTURE.md §3).

Файл главы: YAML-шапка + блоки, один блок = одна строка, блоки разделены пустой строкой.
Блок начинается с маркера {#ID ...}: список канонических ID (или ID с суффиксом .N).
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]

MARKER_RE = re.compile(r"^\{#([^}]+)\}\s?(.*)$")


def chapter_id(part: int, chapter: int) -> str:
    return f"p{part}-c{chapter:02d}"


def para_id(part: int, chapter: int, n: int) -> str:
    return f"{chapter_id(part, chapter)}-{n:03d}"


def chapter_path(base: str, part: int, chapter: int) -> Path:
    return ROOT / base / f"part-{part}" / f"ch-{chapter:02d}.md"


@dataclass
class Block:
    ids: list[str]
    text: str


@dataclass
class Chapter:
    meta: dict
    blocks: list[Block] = field(default_factory=list)


def dump_chapter(ch: Chapter) -> str:
    head = yaml.safe_dump(ch.meta, allow_unicode=True, sort_keys=False).strip()
    body = "\n\n".join("{#" + " ".join(b.ids) + "} " + b.text for b in ch.blocks)
    return f"---\n{head}\n---\n\n{body}\n"


def load_chapter(path: Path) -> Chapter:
    raw = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    _, head, body = raw.split("---\n", 2)
    ch = Chapter(meta=yaml.safe_load(head))
    for chunk in body.strip().split("\n\n"):
        m = MARKER_RE.match(chunk)
        if not m:
            raise ValueError(f"{path}: блок без маркера ID: {chunk[:60]!r}")
        ch.blocks.append(Block(ids=m.group(1).split(), text=m.group(2)))
    return ch


def sha256_file(path: Path) -> str:
    """Хеш бинарного файла (PDF, epub) — байты как есть."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sha256_text(path: Path) -> str:
    """Хеш текстового файла, не зависящий от ОС: BOM убирается, CRLF/CR → LF.

    На Windows git может выдать файлы с CRLF — хеш от этого не меняется."""
    data = path.read_bytes().removeprefix(b"\xef\xbb\xbf")
    return hashlib.sha256(data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")).hexdigest()


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    # newline="\n": на Windows не превращать переводы строк в CRLF
    path.write_text(text, encoding="utf-8", newline="\n")


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def split_ref(ref: str) -> tuple[str, int]:
    """'p1-c01-012' → ('p1-c01-012', 1); 'p1-c01-012.2' → ('p1-c01-012', 2)."""
    base, _, part = ref.partition(".")
    return base, int(part) if part else 1


def coverage_errors(canonical: list[str], blocks: list[Block]) -> list[str]:
    """Инвариант ARCHITECTURE §3: каждый канонический ID начинается ровно в одном блоке, по порядку;
    продолжение X.N (N ≥ 2) допустимо только первым в списке блока и только для последнего начатого ID."""
    errors, pos, last, last_n = [], 0, None, 1
    for bi, b in enumerate(blocks, 1):
        for k, ref in enumerate(b.ids):
            base, n = split_ref(ref)
            if n > 1:
                if k != 0:
                    errors.append(f"блок {bi}: продолжение {ref} не первым в списке")
                if base != last or n != last_n + 1:
                    errors.append(f"блок {bi}: продолжение {ref} не следует за {last}.{last_n}")
                last_n = n
                continue
            if pos >= len(canonical) or canonical[pos] != base:
                expected = canonical[pos] if pos < len(canonical) else "конец"
                errors.append(f"блок {bi}: ожидался {expected}, найден {base}")
                if base in canonical:
                    pos = canonical.index(base)
            pos += 1
            last, last_n = base, 1
    if pos < len(canonical):
        errors.append(f"не покрыты: {canonical[pos:]}")
    return errors
