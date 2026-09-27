"""Пакет внешнего ревью для анализа старого перевода (этап 2): translation/reviews/en/analysis-legacy/request.md.

Пакет привязан к версии (DEC-016): в шапке — коммит, в котором зафиксированы все включённые файлы, и их хеши.
Запускать ПОСЛЕ коммита проверенного состояния; незакоммиченные изменения во включённых файлах — ошибка.
Результаты внутреннего ревью во внешний пакет не включаются (TRANSLATION-PROCESS §7.3).

    python -m tools.review.packet_analysis
"""
from __future__ import annotations

import subprocess

from tools.pylib.bookfmt import ROOT, sha256_text, write

FILES = ["translation/analysis/legacy-en-report.md",
         "translation/analysis/legacy-en-sample-annotations.yml",
         "translation/analysis/legacy-en-sample-metrics.md",
         "translation/analysis/legacy-en-corpus-patterns.md",
         "translation/calibration/cal-1-narrative.md",
         "translation/calibration/cal-2-drama.md",
         "translation/calibration/cal-3-dialogue.md",
         "translation/calibration/cal-4-teaching.md",
         "translation/calibration/cal-5-verse.md"]
OUT = ROOT / "translation/reviews/en/analysis-legacy/request.md"

INSTRUCTIONS = """## Инструкция ревьюеру

**Кто вы.** Независимый ревьюер-лингвист (русский → английский), носитель или уверенный пользователь литературного
британского английского. Вы проверяете анализ качества старого английского перевода романа К. Е. Антаровой «Две жизни».
Этот анализ определит, как глубоко редактировать старый перевод (он станет основой новой английской версии).

**Что проверить.**
1. **Разметку выборки** (раздел «Разметка»): верны ли замечания с `sev: major` и все записи `source-divergence`
   (содержание, которого нет в нашей русской редакции; мы предполагаем, что перевод делался с другой, более полной
   редакции). Верны ли категория и серьёзность? Выборочно проверьте и мелкие замечания.
2. **Пропущенные серьёзные ошибки**: прочитайте окна выборки (раздел «Выборка», части «## Отрывок») — RU рядом со
   старым EN — и укажите серьёзные (major/critical) проблемы, которых нет в разметке. Особенно важны письмо Учителя
   (cal-4) и стихи (cal-5).
3. **Выводы отчёта** (раздел «Отчёт»): обоснованы ли оценка качества и рекомендация «глубокая построчная редактура (L2)
   как норма, L3 для смысловых ошибок, L4 для стихов»? Не преувеличены ли гипотезы (§3 о другой редакции, §5 о
   «мир → calm»)? Разделены ли выводы по выборке и по корпусу?
4. **Английский язык и голос** — здесь ваш взгляд особенно важен (владелец проекта не носитель английского):
   действительно ли старый перевод годится как основа? Верно ли выбраны примеры того, «что сохраняем» (§6.2)?
   Что ещё обязательно исправлять (§6.3)? Как лучше сохранить литературный голос (§6.5)?
5. Уровни правки блоков (L0–L4 в разметке) — укажите явные несогласия.

**Правила.** Разница в числе слов между EN и RU не является доказательством добавлений. Каждое замечание — с ID блока
и цитатами. Если сомневаетесь — пишите `unsure` и почему. Не переписывайте перевод целиком: цель — проверить анализ.

**Формат ответа — строго JSON** (можно в блоке кода), без текста до и после:

```json
{
  "unit": "analysis-legacy",
  "lang": "en",
  "commit": "<коммит из шапки пакета>",
  "reviewer": "<vendor>-<model>",
  "level": "external",
  "findings": [
    {
      "target": "annotation | missed | level | report",
      "id": "<ID блока, например p3-c01-071, или раздел отчёта, например §6.2>",
      "verdict": "confirmed | wrong | severity-too-high | severity-too-low | category-wrong | divergence-doubtful | missed | agree | disagree | unsure",
      "category": "mistranslation | omission | addition | terminology | name | grammar | fluency | style | register | typography | logic | evidence | overclaim | missing",
      "severity": "critical | major | minor",
      "source_excerpt": "<цитата RU, если уместно>",
      "target_excerpt": "<цитата EN, если уместно>",
      "suggestion": "<что исправить>",
      "rationale": "<почему>"
    }
  ],
  "overall": {
    "legacy_usable_as_base": "yes | no | unsure",
    "recommended_depth": "<ваша рекомендация по глубине редактуры>",
    "accuracy": 1, "fluency": 1, "style": 1,
    "comment": "<5–10 предложений: главное, с чем вы согласны и не согласны>"
  }
}
```
Оценки `accuracy/fluency/style` — по шкале 1–5 для **старого перевода** по выборке.
"""


def main() -> None:
    dirty = subprocess.run(["git", "status", "--porcelain", "--"] + FILES, cwd=ROOT, capture_output=True, text=True).stdout
    if dirty.strip():
        raise SystemExit("включённые файлы не закоммичены:\n" + dirty)
    commit = subprocess.run(["git", "rev-parse", "--short=12", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    head = ["---", "unit: analysis-legacy", "lang: en", f"commit: {commit}", "files:"]
    head += [f"  - {{path: {f}, sha256: {sha256_text(ROOT / f)}}}" for f in FILES]
    head += ["---", "", "# Запрос на внешнее ревью: анализ старого английского перевода (этап 2)", "",
             f"Пакет собран из коммита `{commit}` репозитория проекта. Всё нужное для ревью — ниже в этом файле.", ""]
    body = [INSTRUCTIONS]
    sections = [("Отчёт", FILES[0:1]), ("Разметка", FILES[1:2]), ("Метрики по выборке", FILES[2:3]),
                ("Закономерности по корпусу", FILES[3:4]), ("Выборка", FILES[4:])]
    for title, files in sections:
        body.append(f"\n# {title}\n")
        for f in files:
            text = (ROOT / f).read_text(encoding="utf-8")
            fence = "```yaml" if f.endswith(".yml") else "````markdown"
            close = "```" if f.endswith(".yml") else "````"
            body.append(f"\n## Файл `{f}`\n\n{fence}\n{text.rstrip()}\n{close}\n")
    write(OUT, "\n".join(head + body))
    size = OUT.stat().st_size
    print(f"{OUT.relative_to(ROOT)}: {size // 1024} КБ, коммит {commit}")


if __name__ == "__main__":
    main()
