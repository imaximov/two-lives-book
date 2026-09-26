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
    raw = path.read_text(encoding="utf-8")
    _, head, body = raw.split("---\n", 2)
    ch = Chapter(meta=yaml.safe_load(head))
    for chunk in body.strip().split("\n\n"):
        m = MARKER_RE.match(chunk)
        if not m:
            raise ValueError(f"{path}: блок без маркера ID: {chunk[:60]!r}")
        ch.blocks.append(Block(ids=m.group(1).split(), text=m.group(2)))
    return ch


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))
