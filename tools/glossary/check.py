"""Проверка translation/glossary.yml и translation/characters.yml (TRANSLATION-PROCESS §9).

Ошибки: нет обязательного поля, неизвестный уровень или статус, повтор id, дубль (ru, sense) (§9.2 п.3),
approved без approved_by/decided, core утверждён не владельцем, first_seen/evidence ссылаются на несуществующую главу.
Предупреждения: запись без evidence, многозначное слово без distinguish.

    python -m tools.glossary.check
"""
from __future__ import annotations

import re
import sys

import yaml

from tools.pylib.bookfmt import ROOT

FILES = {"glossary": ROOT / "translation/glossary.yml", "characters": ROOT / "translation/characters.yml"}
TIERS = {"core", "secondary"}
STATUSES = {"proposed", "approved", "rejected"}
ID_RE = re.compile(r"^p[1-4]-c\d{2}-\d{3}[a-z]?$")
CHAPTERS = {c["id"] for p in yaml.safe_load((ROOT / "content/book.yml").read_text(encoding="utf-8"))["parts"]
            for v in p.get("volumes", []) for c in v["chapters"]}


def check_lang(where: str, tier: str, d: dict, name_key: str, errors: list) -> None:
    if not d.get(name_key):
        errors.append(f"{where}: нет {name_key}")
    st = d.get("status")
    if st not in STATUSES:
        errors.append(f"{where}: статус {st!r} (нужен один из {sorted(STATUSES)})")
    if st == "approved":
        if not d.get("approved_by") or not d.get("decided"):
            errors.append(f"{where}: approved без approved_by/decided")
        if tier == "core" and d.get("approved_by") != "owner":
            errors.append(f"{where}: core утверждает только владелец (§9.1)")


def check_ref(where: str, ref: str, errors: list) -> None:
    if not ID_RE.match(ref or ""):
        errors.append(f"{where}: ID {ref!r} не в формате pX-cYY-NNN")
    elif ref.rsplit("-", 1)[0] not in CHAPTERS:
        errors.append(f"{where}: глава {ref} не существует")


def main() -> None:
    errors, warnings = [], []
    for kind, path in FILES.items():
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        entries = data.get("entries", [])
        seen, pairs = set(), set()
        name_key = "term" if kind == "glossary" else "name"
        for e in entries:
            eid = e.get("id", "?")
            where = f"{path.name}:{eid}"
            for k in ("id", "ru", "tier", "first_seen", "en"):
                if k not in e:
                    errors.append(f"{where}: нет поля {k}")
            if eid in seen:
                errors.append(f"{where}: id повторяется")
            seen.add(eid)
            if kind == "glossary":
                pair = (e.get("ru"), e.get("sense"))
                if pair in pairs:
                    errors.append(f"{where}: дубль (ru, sense) {pair}")
                pairs.add(pair)
                if "#" in eid and not e.get("distinguish"):
                    warnings.append(f"{where}: значение многозначного слова без distinguish")
            if e.get("tier") not in TIERS:
                errors.append(f"{where}: уровень {e.get('tier')!r}")
            check_ref(f"{where} first_seen", e.get("first_seen"), errors)
            for ev in e.get("evidence", []) or []:
                check_ref(f"{where} evidence", ev.get("id"), errors)
            if not e.get("evidence"):
                warnings.append(f"{where}: нет evidence")
            for lang in ("en", "pl"):
                if lang in e:
                    check_lang(f"{where}.{lang}", e.get("tier"), e[lang], name_key, errors)
        print(f"{path.name}: {len(entries)} записей")
    for w in warnings:
        print("предупреждение:", w)
    if errors:
        print("\n".join("ОШИБКА: " + x for x in errors))
        sys.exit(1)
    print("ok")


if __name__ == "__main__":
    main()
