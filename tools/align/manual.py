"""Ручные правки выравнивания: заменить связи на участке проверенными (review: done).

Использование из Python:
    from tools.align.manual import set_links
    set_links("p1-c12", [((52, 53), (55,)), ((57,), (59, 60), "в L060 расширение")], window=(38, 58))
Номера — порядковые номера абзацев RU (…-052) и EN (L055). Для N:M можно передать blocks:
    ((35, 36, 37), (44, 45), "примечание", {44: [35, 36, 37], 45: ["37.2"]})
После правок запустите `python -m tools.align.legacy_en ...` — промежутки перевыровняются вокруг опор.
Все связи внутри окна `window` (включая неизменённые) помечаются как проверенные.
"""
from __future__ import annotations

import yaml

from tools.pylib.bookfmt import ROOT


def _rid(cid: str, n) -> str:
    return f"{cid}-{n:03d}" if isinstance(n, int) else f"{cid}-{int(n.split('.')[0]):03d}.{n.split('.')[1]}"


def set_links(cid: str, specs: list, window: tuple[int, int] | None = None, note: str = "") -> None:
    path = ROOT / "translation/legacy-en/alignment" / f"{cid}.yml"
    al = yaml.safe_load(path.read_text(encoding="utf-8"))
    new = []
    for spec in specs:
        ru, en = spec[0], spec[1]
        link = {"ru": [_rid(cid, n) for n in ru], "en": [f"L{n:03d}" for n in en],
                "type": f"{len(ru)}:{len(en)}", "review": "done",
                "note": spec[2] if len(spec) > 2 and spec[2] else "исправлено вручную при проверке"}
        if len(spec) > 3:
            link["blocks"] = {f"L{k:03d}": [_rid(cid, x) for x in v] for k, v in spec[3].items()}
        new.append(link)
    touched_ru = {r for l in new for r in l["ru"]}
    touched_en = {e for l in new for e in l["en"]}
    kept = [l for l in al["links"] if not (set(l["ru"]) & touched_ru or set(l["en"]) & touched_en)]
    num = lambda l: int(l["ru"][0].split("-")[-1]) if l["ru"] else None
    if window:
        lo, hi = window
        for l in kept:
            if l["ru"] and lo <= num(l) <= hi:
                l["review"] = "done"
                l.setdefault("note", "проверено вручную: граница верна")
        if al.get("reviewed") != "full":
            wins = list(al.get("reviewed") or [])
            tag = f"{_rid(cid, lo)}..{_rid(cid, hi)}"
            if tag not in wins:
                wins.append(tag)
            al["reviewed"] = wins
    # порядок: по первому RU-ID (EN-only связи остаются рядом с соседями по EN)
    en_pos = lambda l: int(l["en"][0][1:]) if l["en"] else 10**6
    al["links"] = sorted(kept + new, key=lambda l: (en_pos(l), num(l) or 0))
    if note:
        al["review_note"] = (al.get("review_note", "") + " " + note).strip()
    path.write_text(yaml.safe_dump(al, allow_unicode=True, sort_keys=False, width=200), encoding="utf-8", newline="\n")
