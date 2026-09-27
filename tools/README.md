# Инструменты

## Извлечение и выравнивание (Python)

Для PDF (координаты символов, несколько извлекателей) удобнее Python, поэтому этот конвейер на нём.
Проверки, сайт и сборки будут на Node/TypeScript (docs/ARCHITECTURE.md §7).

```bash
python3 -m venv .venv && .venv/bin/pip install -r tools/requirements.txt

# 1а. Русский оригинал
.venv/bin/python -m tools.extract.ru_epub --book-yml             # content/book.yml
.venv/bin/python -m tools.extract.ru_epub --part 1 --chapter 1   # content/ru/part-1/ch-01.md
.venv/bin/python -m tools.extract.verify_ru_pdf --part 1 --chapter 1

# 1б. Старый английский перевод без правок
.venv/bin/python -m tools.extract.legacy_en_pdf --part 1 --chapter 1   # translation/legacy-en/raw/…

# 1в. Выравнивание → ручная проверка всех `review: needed` → импорт
.venv/bin/python -m tools.align.legacy_en --part 1 --chapter 1         # translation/legacy-en/alignment/…
.venv/bin/python -m tools.align.import_legacy --part 1 --chapter 1     # content/en/part-1/ch-01.md
```

Ручные правки выравнивания — `tools/align/manual.py` (`set_links`): исправленные связи и проверенные окна
помечаются `review: done` и становятся опорами; повторный запуск `tools.align.legacy_en` перевыравнивает
только промежутки. Импорт разрешён только для глав с `reviewed: full`.

```bash
# Калибровочный набор (отрывки для сравнения моделей)
.venv/bin/python -m tools.calibration.build        # translation/calibration/passages.yml → cal-*.md
```

Отчёты каждого шага — в `translation/reports/`. Общий формат и проверка покрытия ID — `tools/pylib/bookfmt.py`.

## Анализ старого перевода (этап 2)

```bash
.venv/bin/python -m tools.analysis.sample_metrics    # метрики разметки выборки
.venv/bin/python -m tools.analysis.legacy_patterns   # закономерности по корпусу (сырые совпадения)
```

## Глоссарий (этап 3)

```bash
# Вспомогательный корпус RU ↔ старый EN, выровненный АВТОМАТИЧЕСКИ (не проверен; кэш .cache/corpus/, не коммитится)
.venv/bin/python -m tools.glossary.corpus build
.venv/bin/python -m tools.glossary.corpus find 'самооблад' --en 'self-(control|possession)'
.venv/bin/python -m tools.glossary.corpus count 'самооблад'
# Проверка translation/glossary.yml и translation/characters.yml (TRANSLATION-PROCESS §9)
.venv/bin/python -m tools.glossary.check
```

Корпус нужен только для поиска доказательств (как термин передан в старом EN, где впервые встречается).
Цитаты EN из него перед использованием сверяются глазами: автовыравнивание может сдвигаться на абзац.
