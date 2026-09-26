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

Отчёты каждого шага — в `translation/reports/`. Общий формат и проверка покрытия ID — `tools/pylib/bookfmt.py`.
