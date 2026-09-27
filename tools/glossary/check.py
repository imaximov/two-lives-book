"""Проверка translation/glossary.yml и translation/characters.yml (TRANSLATION-PROCESS §9).

Ошибки: нет обязательного поля, неизвестный уровень или статус, повтор id, дубль (ru, sense) (§9.2 п.3),
approved без approved_by/decided, core утверждён не владельцем, first_seen/evidence ссылаются на несуществующую главу,
RU-цитата evidence не найдена в тексте своего абзаца (сверка с epub; куски между «…» ищутся по отдельности),
в en.term глоссария стоит форма имени из en.avoid персонажа (расхождение glossary.yml и characters.yml).
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


def ru_paragraphs() -> dict[str, str]:
    from tools.extract import ru_epub
    from tools.pylib.bookfmt import para_id
    return {para_id(part, c.number, i): t for part in (1, 2, 3) for c in ru_epub.read_part(part)
            for i, t in enumerate(c.paragraphs, 1)}


def norm_text(t: str) -> str:
    t = t.replace("ё", "е").replace("Ё", "Е")
    t = re.sub(r"[«»„“”\"']", "", t)
    t = re.sub(r"[—–-]", "-", t)
    return re.sub(r"\s+", " ", t).strip().lower()


def quote_found(quote: str, para: str) -> bool:
    p = norm_text(para)
    chunks = [norm_text(c) for c in re.split(r"…|\.\.\.|\[[^\]]*\]| / ", quote)]
    return all(c.strip(" .,;:!?-") in p for c in chunks if len(c.strip(" .,;:!?-")) >= 6)


def main() -> None:
    errors, warnings = [], []
    paras = ru_paragraphs()
    avoid_names: set[str] = set()
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
            if e.get("tier") not in TIERS:
                errors.append(f"{where}: уровень {e.get('tier')!r}")
            check_ref(f"{where} first_seen", e.get("first_seen"), errors)
            for ev in e.get("evidence", []) or []:
                check_ref(f"{where} evidence", ev.get("id"), errors)
                q, pid = ev.get("ru"), ev.get("id")
                if q and pid in paras and not quote_found(q, paras[pid]):
                    errors.append(f"{where} evidence {pid}: RU-цитата не найдена в абзаце: «{q[:60]}»")
            if kind == "characters":
                avoid_names.update(a for a in (e.get("en", {}).get("avoid") or []) if isinstance(a, str) and a[:1].isupper())
            if not e.get("evidence"):
                warnings.append(f"{where}: нет evidence")
        if kind == "glossary":  # у слова несколько записей-значений → каждая должна объяснять различие
            groups: dict[str, list] = {}
            for e in entries:
                groups.setdefault(e.get("id", "").split("#")[0], []).append(e)
            for base, es in groups.items():
                if len(es) > 1 and base not in ("formula", "rule"):
                    for e in es:
                        if not e.get("distinguish"):
                            warnings.append(f"{path.name}:{e.get('id')}: значение многозначного слова без distinguish")
            for lang in ("en", "pl"):
                if lang in e:
                    check_lang(f"{where}.{lang}", e.get("tier"), e[lang], name_key, errors)
        if kind == "glossary":
            glossary_entries = entries
        print(f"{path.name}: {len(entries)} записей")
    for e in glossary_entries:  # имена в примерах глоссария — только по characters.yml
        term = str(e.get("en", {}).get("term", ""))
        for name in avoid_names:
            if re.search(rf"(?<![\w-]){re.escape(name)}(?![\w-])", term):
                errors.append(f"glossary.yml:{e['id']}: en.term содержит «{name}» — эта форма в en.avoid персонажа")
    for w in warnings:
        print("предупреждение:", w)
    if errors:
        print("\n".join("ОШИБКА: " + x for x in errors))
        sys.exit(1)
    print("ok")


if __name__ == "__main__":
    main()
