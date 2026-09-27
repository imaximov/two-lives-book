"""Метрики качества старого EN по размеченной выборке (этап 2).

Вход: translation/calibration/cal-*.md (окна) + translation/analysis/legacy-en-sample-annotations.yml.
Выход: translation/analysis/legacy-en-sample-metrics.md.
Проверяет, что уровни правки заданы ровно для всех EN-блоков окон, а замечания ссылаются на абзацы окон.

    python -m tools.analysis.sample_metrics
"""
from __future__ import annotations

import re
from collections import Counter, defaultdict

import yaml

from tools.pylib.bookfmt import ROOT, sha256_text, write

CAL = ROOT / "translation/calibration"
ANN = ROOT / "translation/analysis/legacy-en-sample-annotations.yml"
OUT = ROOT / "translation/analysis/legacy-en-sample-metrics.md"
SEVS = ("critical", "major", "minor")
LEVELS = ("L0", "L1", "L2", "L3", "L4")


def parse_window(path):
    text = path.read_text(encoding="utf-8")
    meta = yaml.safe_load(text.split("---\n")[1])
    win = text.split("## Отрывок")[1].split("## Контекст после")[0]
    ru, en, en_ids = {}, {}, {}
    mode = None
    for line in win.splitlines():
        if line.startswith("RU:"):
            mode = "ru"
        elif line.startswith("EN"):
            mode = "en"
        m = re.match(r"^\{#([^}]+)\} ?(.*)$", line)
        if m and mode:
            ids = m.group(1).split()
            if mode == "ru":
                ru[ids[0]] = m.group(2)
            else:
                en[ids[0]] = m.group(2)
                en_ids[ids[0]] = ids
        elif en and mode == "en" and line and not line.startswith(("---", "EN", "RU")):
            last = list(en)[-1]
            en[last] += "\n" + line  # многострочный блок (стихи)
    return meta, ru, en, en_ids


def words(t: str) -> int:
    return len(re.sub(r"::: verse|:::|\*", " ", t).split())


def main() -> None:
    ann = yaml.safe_load(ANN.read_text(encoding="utf-8"))
    passages = []
    all_ru, all_en, block_of = {}, {}, {}
    for p in sorted(CAL.glob("cal-*.md")):
        meta, ru, en, en_ids = parse_window(p)
        passages.append((meta, ru, en))
        all_ru.update({k: meta["id"] for k in ru})
        all_en.update({k: meta["id"] for k in en})
        for first, ids in en_ids.items():
            for i in ids:
                block_of[i] = first

    errors = []
    levels = ann["levels"]
    for k in all_en:
        if k not in levels:
            errors.append(f"нет уровня правки для блока {k}")
    for k, v in levels.items():
        if k not in all_en:
            errors.append(f"уровень для несуществующего блока {k}")
        if v not in LEVELS:
            errors.append(f"{k}: неизвестный уровень {v}")
    for f in ann["findings"]:
        base = f["id"].split(".")[0]
        if base not in all_ru:
            errors.append(f"замечание к абзацу вне окон: {f['id']}")
        if f["cat"] != "source-divergence" and f.get("sev") not in SEVS:
            errors.append(f"{f['id']}: нет серьёзности")
        if f["id"] not in block_of:
            errors.append(f"замечание {f['id']} не соответствует ни одному ID блоков EN")
    with_findings = {block_of[f["id"]] for f in ann["findings"] if f["id"] in block_of and f["cat"] != "source-divergence"}
    for k, v in levels.items():
        if v != "L0" and k not in with_findings:
            errors.append(f"блок {k}: уровень {v}, но нет ни одной находки")
    if errors:
        raise SystemExit("разметка не согласована с выборкой:\n  " + "\n  ".join(errors))

    by_pass = defaultdict(list)
    for f in ann["findings"]:
        by_pass[all_ru[f["id"].split(".")[0]]].append(f)

    def is_err(f, variant):
        return f["cat"] != "source-divergence" and not (variant == "B" and f.get("edition_candidate"))

    lines = ["# Метрики выборки старого EN (генерируется)", "",
             "Файл создан `python -m tools.analysis.sample_metrics`; не править вручную.", "",
             f"- Разметка: `translation/analysis/legacy-en-sample-annotations.yml` (sha256 текста `{sha256_text(ANN)}`)",
             "- `source-divergence` (вероятное расхождение редакций с внешним признаком) в ошибки не входит.",
             "- **Вариант A** — все остальные находки. **Вариант B** — без находок `edition_candidate` (содержание, которое",
             "  теоретически может восходить к другой редакции; зависит от D14).",
             "- Плотность — на 1 000 слов **русского** оригинала окна.", ""]
    tot_words = 0
    for variant in ("A", "B"):
        lines += [f"## По отрывкам — вариант {variant}", "",
                  "| Отрывок | Слов RU | Блоков EN | critical | major | minor | critical+major на 1000 | всего на 1000 |",
                  "|---|---|---|---|---|---|---|---|"]
        pc, pw = Counter(), 0
        for meta, ru, en in passages:
            errs = [f for f in by_pass[meta["id"]] if is_err(f, variant)]
            c = Counter(f["sev"] for f in errs)
            w = sum(words(t) for t in ru.values())
            if meta["evaluate"] == "prose":
                pc.update(c)
                pw += w
            lines.append(f"| {meta['id']} | {w} | {len(en)} | {c['critical']} | {c['major']} | {c['minor']} | "
                         f"{1000 * (c['critical'] + c['major']) / w:.1f} | {1000 * sum(c.values()) / w:.1f} |")
        lines += ["", f"**Проза вместе** (без стихов), вариант {variant}: {pw} слов RU; critical {pc['critical']}, major {pc['major']}, "
                  f"minor {pc['minor']}; critical+major — {1000 * (pc['critical'] + pc['major']) / pw:.1f} на 1000 слов, "
                  f"всего — {1000 * sum(pc.values()) / pw:.1f} на 1000 слов.", ""]
        tot_words = pw
    div = [f for f in ann["findings"] if f["cat"] == "source-divergence"]
    cand = [f for f in ann["findings"] if f.get("edition_candidate")]
    lines += [f"Вероятные расхождения редакций (`source-divergence`): {len(div)} — "
              + ", ".join(f"{f['id']} ({f.get('evidence')})" for f in div) + ".",
              f"Находки `edition_candidate`: {len(cand)} — " + ", ".join(f["id"] for f in cand) + ".", ""]

    lines += ["## По категориям (все отрывки, вариант A)", "", "| Категория | critical | major | minor | всего |", "|---|---|---|---|---|"]
    cats = defaultdict(Counter)
    for f in ann["findings"]:
        if f["cat"] != "source-divergence":
            cats[f["cat"]][f["sev"]] += 1
    for cat, c in sorted(cats.items(), key=lambda x: -sum(x[1].values())):
        lines.append(f"| {cat} | {c['critical']} | {c['major']} | {c['minor']} | {sum(c.values())} |")
    lines.append("")

    lines += ["## Нужная глубина правки блоков", "",
              "Уровни: L0 — оставить; L1 — точечно; L2 — построчная редактура; L3 — переписать фразы из-за смысловых ошибок; L4 — перевести заново.", "",
              "| Отрывок | L0 | L1 | L2 | L3 | L4 | доля L2+ |", "|---|---|---|---|---|---|---|"]
    allc, prosec = Counter(), Counter()
    for meta, ru, en in passages:
        c = Counter(levels[k] for k in en)
        allc.update(c)
        if meta["evaluate"] == "prose":
            prosec.update(c)
        lines.append(f"| {meta['id']} | " + " | ".join(str(c[l]) for l in LEVELS)
                     + f" | {100 * (c['L2'] + c['L3'] + c['L4']) / len(en):.0f}% |")
    for name, c in (("проза", prosec), ("всего", allc)):
        n = sum(c.values())
        lines.append(f"| **{name}** | " + " | ".join(str(c[l]) for l in LEVELS)
                     + f" | {100 * (c['L2'] + c['L3'] + c['L4']) / n:.0f}% |")
    write(OUT, "\n".join(lines) + "\n")
    print("\n".join(lines[9:]))


if __name__ == "__main__":
    main()
