"""Раскладка канонических ID по блокам перевода для одной связи выравнивания (ARCHITECTURE §3).

  1:1 → [ru]; N:1 → [ru1 ru2 …]; 1:N → [ru], [ru.2], [ru.3] …;
  N:M → явно из поля `blocks`; 1:0 → блок «⟦missing⟧»; 0:1 → продолжение предыдущего ID.
"""
from __future__ import annotations

from tools.pylib.bookfmt import split_ref

MISSING = "⟦missing⟧"


def layout(link: dict, prev_ref: str | None) -> list[tuple[str | None, list[str]]]:
    """Список (EN-абзац L… или None для missing, список ID блока)."""
    r, e = link["ru"], link["en"]
    if "blocks" in link:
        return [(lid, link["blocks"][lid]) for lid in e]
    if r and not e:
        return [(None, [x]) for x in r]
    if e and not r:
        base, n = split_ref(prev_ref) if prev_ref else (None, 1)
        return [(lid, [f"{base}.{n + k}"]) for k, lid in enumerate(e, 1)]
    if len(e) == 1:
        return [(e[0], list(r))]
    if len(r) == 1:
        return [(lid, [r[0] if k == 0 else f"{r[0]}.{k + 1}"]) for k, lid in enumerate(e)]
    raise ValueError(f"связь {r}↔{e}: для N:M нужно поле blocks")
