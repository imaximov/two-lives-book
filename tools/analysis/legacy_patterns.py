"""Проверка закономерностей по всему корпусу старого EN (этап 2), с разбивкой по томам.

Вход: PDF старого перевода (Vol1, Vol2, Vol3 из New/) и epub оригинала (для сопоставления имён и титулов).
Выход: translation/analysis/legacy-en-corpus-patterns.md — частоты на 10 000 слов и примеры со страницами.

Ограничение: в новом Vol3 ≈1% текста извлекается без пробелов (INVENTORY §3) — совпадения внутри таких
фрагментов не находятся, поэтому для Vol3 числа — нижняя оценка.

    python -m tools.analysis.legacy_patterns
"""
from __future__ import annotations

import re
import warnings

import ebooklib
import pymupdf
from bs4 import BeautifulSoup
from ebooklib import epub

from tools.pylib.bookfmt import ROOT, sha256_file, write

warnings.filterwarnings("ignore")

VOLS = {"Vol1 (ч. I)": "sources/en-legacy/TwoLives-Vol1-2018-part1.pdf",
        "Vol2 (ч. II)": "sources/en-legacy/TwoLives-Vol2-2021-part2.pdf",
        "Vol3 (ч. III)": "sources/en-legacy/New/TwoLives-Vol3.pdf"}
RU = {"Vol1 (ч. I)": "sources/ru/original/part-1.epub",
      "Vol2 (ч. II)": "sources/ru/original/part-2.epub",
      "Vol3 (ч. III)": "sources/ru/original/part-3.epub"}

# (группа, название, regex EN, regex RU для сопоставления или None, флаги)
PATTERNS = [
    ("Имена и титулы", "duke без Grand Duke (кандидаты «князь» → duke)", r"(?<!Grand )(?<!grand )\b[Dd]uke(?:s|’s)?\b", r"\bкня(?:зь|зя|зю|зем|зе|зья|зей)\b"),
    ("Имена и титулы", "Grand Duke (допустимо: великий князь)", r"\b[Gg]rand [Dd]uke(?:s|’s)?\b", None),
    ("Имена и титулы", "prince (любые: и «князь», и сказочный принц)", r"\b[Pp]rince(?:s|’s)?\b", None),
    ("Имена и титулы", "Левушка → Lovushka", r"\bLovushka\b", r"\bЛ[её]вушк"),
    ("Имена и титулы", "Левушка → Lyovushka", r"\bLyovushka\b", None),
    ("Имена и титулы", "Левушка → Levushka", r"\bLevushka\b", None),
    ("Имена и титулы", "Флорентиец → Florentian", r"\bFlorentian", r"\bФлоренти[йе]"),
    ("Имена и титулы", "Флорентиец → Florentine", r"\bFlorentine", None),
    ("Имена и титулы", "Уоми → Vomi", r"\bVomi\b", r"\bУоми\b"),
    ("Имена и титулы", "Уоми → Uomi/Oomi/Womi", r"\b(?:Uomi|Oomi|Womi|Wommi|Uommi)\b", None),
    ("Имена и титулы", "Жанна → Joan", r"\bJoan\b", r"\bЖанн"),
    ("Имена и титулы", "Жанна → Jeanne/Jane", r"\b(?:Jeanne|Jane)\b", None),
    ("Имена и титулы", "Алиса → Alyssa", r"\bAlyssa\b", r"\bАлис[аыеуо]"),
    ("Имена и титулы", "Алиса → Alice", r"\bAlice\b", None),
    ("Имена и титулы", "Али старший → the elder Ali", r"\b[Tt]he elder Ali\b", r"\bАли[- ]старш"),
    ("Имена и титулы", "Али старший → the older Ali", r"\b[Tt]he older Ali\b", None),
    ("Имена и титулы", "Али старший → the old Ali", r"\b[Tt]he old Ali\b", None),
    ("Имена и титулы", "«И.» → I. (с пробелом/знаком после; без чужих инициалов вида «F. I.»)",
     r"(?<![A-Z]\. )(?<![A-Za-z])I\.(?=[’'\s,;:!?)”])", r"(?<![А-Яа-я])И\.(?=[\s,;:!?)»”])"),
    ("Кальки", "everything what / all what", r"\b(?:[Ee]verything|[Aa]ll) what\b", None),
    ("Кальки", "According to me", r"\b[Aa]ccording to me\b", None),
    ("Кальки", "глагол речи/действия + by -ing (деепричастие)",
     r"\b(?:uttered|said|added|answered|asked|told|came in|went up|was telling|was speaking|was saying|were telling)\b[^.”“]{0,30}?\bby [a-z]+ing\b", None),
    ("Кальки", "hair were (волосы — мн. ч.)", r"\bhair were\b", None),
    ("Кальки", "begin and start (начать и кончить)", r"\bbegin and (?:to )?start\b", None),
    ("Регистр и лексика", "глагол речи uttered", r"\buttered\b", None),
    ("Регистр и лексика", "be going to + глагол (без going to + место)",
     r"\b(?:am|is|are|was|were|’s|’re|’m)\s+going to (?!(?:the|a|an|his|her|my|our|their|your|its|this|that|bed|church|school|town|sleep|see)\b)[a-z]+", None),
    ("Регистр и лексика", "clumsy sailor (матрос-верзила)", r"\bclumsy sailor\b", r"\bверзил"),
    ("Регистр и лексика", "oriental robe (халат)", r"\boriental robes?\b", r"\bхалат"),
    ("Регистр и лексика", "слово calm (все формы, без calmly; может передавать «мир», «покой», «спокойствие»)", r"\bcalm\b", None),
    ("Регистр и лексика", "peace", r"\bpeace\b", r"\bмир(?:а|у|ом|е)?\b"),
    ("Пунктуация", "глагол речи + продолжение реплики без запятой: «uttered “they»",
     r"\b(?:said|uttered|answered|asked|added|continued|replied|whispered|shouted|cried|exclaimed|told \w+|went on|was speaking(?: to \w+)?|was telling(?: \w+)?)(?: \w+ly)? “[a-z]", None),
    ("Орфография", "gotten (американское; брит. got)", r"\bgotten\b", None),
    ("Орфография", "colour / color", r"\b[Cc]olour", None),
    ("Орфография", "color (американское)", r"\b[Cc]olor(?!ado)", None),
    ("Орфография", "honour / honor", r"\b[Hh]onour", None),
    ("Орфография", "honor (американское)", r"\b[Hh]onor(?!ary)", None),
    ("Орфография", "grey", r"\b[Gg]rey\b", None),
    ("Орфография", "gray (американское)", r"\b[Gg]ray\b", None),
    ("Орфография", "theatre", r"\b[Tt]heatre", None),
    ("Орфография", "theater (американское)", r"\b[Tt]heater", None),
    ("Орфография", "recogniz- / realiz- (оксфордское -ize)", r"\b(?:[Rr]ecogniz|[Rr]ealiz)", None),
    ("Орфография", "recognis- / realis- (-ise)", r"\b(?:[Rr]ecognis|[Rr]ealis)", None),
]


def en_pages(path: str) -> list[str]:
    return [p.get_text() for p in pymupdf.open(ROOT / path)]


def ru_text(path: str) -> str:
    book = epub.read_epub(str(ROOT / path))
    return "\n".join(BeautifulSoup(i.get_content(), "html.parser").get_text(" ")
                     for i in book.get_items_of_type(ebooklib.ITEM_DOCUMENT))


def main() -> None:
    data = {}
    for vol, path in VOLS.items():
        pages = [re.sub(r"\s+", " ", p) for p in en_pages(path)]
        ru = re.sub(r"\s+", " ", ru_text(RU[vol]))
        if vol.startswith("Vol3"):
            ru = ru.split(" Часть IV ")[0]
        data[vol] = (pages, ru)
    words = {v: sum(len(p.split()) for p in pages) for v, (pages, _) in data.items()}

    out = ["# Закономерности по корпусу старого EN (генерируется)", "",
           "Файл создан `python -m tools.analysis.legacy_patterns`; не править вручную. Числа — **сырые совпадения поисковых",
           "шаблонов** в томе и на 10 000 слов английского текста тома, а не число подтверждённых ошибок: каждое вхождение",
           "проверяется при редактуре по контексту и RU. RU — вхождения в оригинале соответствующей части (для сопоставления имён и титулов).",
           "Для Vol3 — нижняя оценка (≈1% текста извлекается слитно). Примеры: страница PDF (с 1) и фрагмент.", "",
           "| Том | Файл | sha256 | Слов EN |", "|---|---|---|---|"]
    for vol, path in VOLS.items():
        out.append(f"| {vol} | `{path}` | `{sha256_file(ROOT / path)[:16]}…` | {words[vol]} |")
    group = None
    for g, name, rx, rx_ru in PATTERNS:
        if g != group:
            out += ["", f"## {g}", "", "| Закономерность | " + " | ".join(VOLS) + " | RU (ч. I / II / III) |",
                    "|---|" + "---|" * len(VOLS) + "---|"]
            group = g
            examples_block = []
        cells, ru_cells, ex = [], [], []
        for vol, (pages, ru) in data.items():
            hits = [(i + 1, m) for i, p in enumerate(pages) for m in re.finditer(rx, p)]
            cells.append(f"{len(hits)} ({10000 * len(hits) / words[vol]:.1f})")
            if rx_ru:
                ru_cells.append(str(len(re.findall(rx_ru, ru))))
            for pno, m in hits[:2]:
                p = pages[pno - 1]
                ex.append(f"{vol.split()[0]} с.{pno}: «…{p[max(0, m.start() - 45):m.end() + 45].strip()}…»")
        out.append(f"| {name} | " + " | ".join(cells) + f" | {' / '.join(ru_cells) if ru_cells else '—'} |")
        out.append(f"|  | " + "<br>".join(ex[:3]).replace("|", "\\|") + " |" + " |" * len(VOLS))
    write(ROOT / "translation/analysis/legacy-en-corpus-patterns.md", "\n".join(out) + "\n")
    print("\n".join(out[:12]))


if __name__ == "__main__":
    main()
