"""Пакеты внешнего ревью ядра глоссария (этап 3): translation/reviews/en/glossary-core/request-{1,2}.md.

Привязка к версии (DEC-016): в шапке — коммит и хеши файлов; незакоммиченные изменения — ошибка.
Результаты внутреннего ревью во внешний пакет не включаются (TRANSLATION-PROCESS §7.3).
Пакет 1 — персонажи, титулы, обращения, условности, черновик речи торговца; пакет 2 — понятия учения, формулы, правила,
термины пилотной главы и калибровочных отрывков. В каждом — список id, по которым нужен явный вердикт (§7.4, §9.1).

    python -m tools.review.packet_glossary
"""
from __future__ import annotations

import subprocess

import yaml

from tools.pylib.bookfmt import ROOT, sha256_text, write

GLOSSARY = "translation/glossary.yml"
CHARACTERS = "translation/characters.yml"
MERCHANT = "translation/analysis/merchant-speech-draft.md"
FILES = [GLOSSARY, CHARACTERS, MERCHANT, "translation/decisions.md"]
OUT = ROOT / "translation/reviews/en/glossary-core"
TITLE_IDS_START, PILOT_IDS_START = "knyaz#title", "kupets"  # границы разделов glossary.yml (как в файле)

INSTRUCTIONS = """## Инструкция ревьюеру

**Кто вы.** Независимый ревьюер-лингвист (русский → английский), уверенный пользователь литературного британского
английского. Проект — новая английская версия романа К. Е. Антаровой «Две жизни» (1990-е, три части, ≈650 тыс. слов RU)
на основе старого английского перевода (его редактируем, DEC-003, DEC-023). Вы проверяете **ядро глоссария**:
предложенные английские варианты сквозных понятий, имён, титулов и формул. Утверждённое станет обязательным для всего
текста, поэтому ошибка здесь размножится на сотни мест.

**Как устроена запись.** `ru`, `sense` — значение по тексту; `distinguish` — чем отличается от других значений того же
слова; `evidence` — цитаты с ID абзаца (`en_legacy` — старый перевод этого места); `en.legacy` — как передавал старый
перевод, с частотами (≈ — оценка по автоматическому выравниванию); `en.term` / `en.name` — **предложение**;
`en.avoid` — чего не писать; `question` — вопрос владельцу с вариантами и рекомендацией.

**Правила проекта** (обязательны и для оценки): британский английский с оксфордским -ize (DEC-024); имя персонажа
восстанавливается только по основаниям в тексте романа, «так естественнее по-английски» недостаточно (DEC-028);
по умолчанию сохраняется вариант старого перевода, если он не ошибочен (§9.2); разные значения — разные записи;
никаких доктринальных толкований, которых нет в тексте романа. Выдержка из журнала решений — в конце пакета.

**Что сделать.**
1. **Вердикт по каждому id из списка «Требуют вердикта»** — `agree` (согласен с предложением `en.term`/`en.name`),
   `object` (не согласен — дайте свой вариант и довод), `unsure` (почему). Термин без вердикта считается
   неподтверждённым; молчание — не согласие (DEC-015).
2. Для записей с `question` — ваш выбор варианта и довод (в поле `rationale` вердикта).
3. Замечания по существу (`findings`): неверное значение или разделение значений, неверная цитата или ID, конфликт
   терминов (одно английское слово для разных понятий), пропущенное сквозное понятие или персонаж, неестественный
   английский, неверная капитализация.
4. Пакет 1 дополнительно: черновик образцов речи торговца (DEC-025) — умеренная или лёгкая плотность, не карикатурно ли,
   правдоподобно ли.

**Формат ответа — строго JSON** (можно в блоке кода), без текста до и после:

```json
{
  "unit": "glossary-core",
  "part": "<1 или 2 — номер пакета>",
  "lang": "en",
  "commit": "<коммит из шапки пакета>",
  "reviewer": "<vendor>-<model>",
  "level": "external",
  "terms": [
    {"term_id": "<id>", "lang": "en", "verdict": "agree | object | unsure", "suggestion": "<если object>", "rationale": "<довод; для question — выбранный вариант>"}
  ],
  "findings": [
    {"id": "<id записи>", "category": "terminology | name | evidence | consistency | missing | fluency | typography | style",
     "severity": "critical | major | minor", "source_excerpt": "…", "target_excerpt": "…", "suggestion": "…", "rationale": "…"}
  ],
  "overall": {"comment": "<5–10 предложений: главное, с чем согласны и не согласны>"}
}
```
"""


def compact(e: dict) -> dict:
    keep = ["id", "ru", "sense", "distinguish", "gender", "role", "aliases", "origin", "tier", "first_seen", "counts",
            "note", "evidence", "en", "question"]
    out = {k: e[k] for k in keep if k in e}
    if "evidence" in out:
        out["evidence"] = out["evidence"][:4]
    return out


def dump(entries: list[dict]) -> str:
    return yaml.safe_dump([compact(e) for e in entries], allow_unicode=True, sort_keys=False, width=120)


def main() -> None:
    dirty = subprocess.run(["git", "status", "--porcelain", "--"] + FILES, cwd=ROOT, capture_output=True, text=True).stdout
    if dirty.strip():
        raise SystemExit("включённые файлы не закоммичены:\n" + dirty)
    commit = subprocess.run(["git", "rev-parse", "--short=12", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    g = yaml.safe_load((ROOT / GLOSSARY).read_text(encoding="utf-8"))["entries"]
    ch = yaml.safe_load((ROOT / CHARACTERS).read_text(encoding="utf-8"))["entries"]
    ids = [e["id"] for e in g]
    t0, p0 = ids.index(TITLE_IDS_START), ids.index(PILOT_IDS_START)
    concepts_etc, titles, pilot = g[:t0], g[t0:p0], g[p0:]
    decisions = (ROOT / "translation/decisions.md").read_text(encoding="utf-8")
    packs = {1: [("Персонажи (characters.yml)", ch), ("Титулы, обращения, условности (glossary.yml)", titles)],
             2: [("Понятия учения, формулы, правила (glossary.yml)", concepts_etc),
                 ("Термины пилотной главы p1-c01 и калибровочных отрывков (glossary.yml)", pilot)]}
    for n, sections in packs.items():
        head = ["---", "unit: glossary-core", f"part: {n}", "lang: en", f"commit: {commit}", "files:"]
        head += [f"  - {{path: {f}, sha256: {sha256_text(ROOT / f)}}}" for f in FILES]
        head += ["---", "", f"# Запрос на внешнее ревью: ядро глоссария, пакет {n} из 2 (этап 3)", "",
                 f"Пакет собран из коммита `{commit}`. Всё нужное для ревью — в этом файле.", "", INSTRUCTIONS]
        verdict_ids = [e["id"] for _, es in sections for e in es]
        body = ["## Требуют вердикта", "", f"{len(verdict_ids)} id (по каждому — agree / object / unsure):", "",
                ", ".join(f"`{i}`" for i in verdict_ids), ""]
        for title, es in sections:
            body += [f"# {title}", "", "```yaml", dump(es).rstrip(), "```", ""]
        if n == 1:
            body += ["# Черновик: речь торговца (DEC-025)", "", "````markdown",
                     (ROOT / MERCHANT).read_text(encoding="utf-8").rstrip(), "````", ""]
        body += ["# Журнал решений (для справки)", "", "````markdown", decisions.rstrip(), "````", ""]
        out = OUT / f"request-{n}.md"
        write(out, "\n".join(head + body))
        print(f"{out.relative_to(ROOT)}: {out.stat().st_size // 1024} КБ, {len(verdict_ids)} id, коммит {commit}")


if __name__ == "__main__":
    main()
