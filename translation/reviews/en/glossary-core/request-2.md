---
unit: glossary-core
part: 2
lang: en
commit: 574498a2318e
files:
  - {path: translation/glossary.yml, sha256: bf090295a2ab0577bd73a4870a3b062cd80e00f17ce1d2030dddfc9429c39070}
  - {path: translation/characters.yml, sha256: 8a9d2382df2b304942ed13a9ce996a07aa4ab895fce4f0524c9e51c5c13e8682}
  - {path: translation/analysis/merchant-speech-draft.md, sha256: c0910da5419f0dff4a929eccf1dfa40535fa65fb1108c2c05bf3c3d88bc3deb1}
  - {path: translation/decisions.md, sha256: 9b04a201112dbd7974c3b4cdac3cf30cdd40ed630f30bcb8e0d28669653f6dad}
---

# Запрос на внешнее ревью: ядро глоссария, пакет 2 из 3 (этап 3)

Пакет собран из коммита `574498a2318e`. Всё нужное для ревью — в этом файле.

## Инструкция ревьюеру

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
  "part": "<1, 2 или 3 — номер пакета>",
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

## Требуют вердикта

109 id (по каждому — agree / object / unsure):

`uchitel#spiritual`, `uchitel#school`, `uchenik#disciple`, `uchenik#pupil`, `uchenichestvo`, `nastavnik`, `vladyka#master`, `vladyka#ruler`, `vladyka#god`, `vladyki-karm`, `sanat-kumara`, `maha-chohan`, `kumary`, `obshchina`, `svetloe-bratstvo`, `brat#sibling`, `brat#fellow`, `zhizn#life-divine`, `velikaya-zhizn`, `edinaya-zhizn`, `edinyi`, `velikaya-mat`, `mat-zhizni`, `vechnost`, `vechnoe`, `vechnoe-dvizhenie`, `svet#light-divine`, `svet#light`, `svet#society`, `svet#world`, `svetly`, `mir#peace`, `mir#world`, `mir-vselennaya`, `spokoistvie`, `pokoy`, `vselennaya`, `lyubov`, `radost`, `zvuchashchaya-radost`, `miloserdie`, `sostradanie`, `poshchada`, `zhalost`, `dobro#good`, `zlo`, `volya#will`, `volya#freedom`, `volya-k-dobru`, `ya#self`, `sovershenstvovanie`, `sovershenstvo`, `samoobladanie`, `bodrost`, `besstrashie`, `garmoniya`, `dukh#spirit`, `dukh#beings`, `dusha#soul`, `soznanie`, `vernost`, `predannost`, `trud`, `obshchee-blago`, `podvig`, `sotrudnik`, `sotrudnichestvo`, `put#path`, `stupen`, `osvobozhdenie`, `karma`, `temnye-sily`, `temnye-okkultisty`, `znanie`, `blagoslovenie`, `edinenie`, `tvorchestvo`, `samootverzhennost`, `luch#ray`, `uslovnost`, `predrassudok`, `tselesoobraznost`, `zakonomernost`, `seryi-den`, `gonets`, `zakalyat#temper`, `muzhestvo`, `sila#power`, `bozhestvennyi`, `istina`, `ogon`, `zemlya#planet`, `zemlya#earth`, `bog`, `formula#mir-tebe`, `formula#privet-i-mir`, `formula#pozhatie`, `formula#drug-brat-syn`, `formula#bud-blagosloven`, `formula#lyubimyi-i-lyubyashchii`, `formula#idi-s-mirom`, `formula#blazhenstvo`, `formula#svet-i-mir`, `formula#nikto-ne-drug`, `formula#muzhaysya`, `formula#zovi-imya`, `podpis#tvoy-drug`, `rule#capitalized-concepts`, `rule#capital-pronouns`

# Понятия учения, формулы, правила (glossary.yml)

```yaml
- id: uchitel#spiritual
  ru: Учитель
  sense: духовный Учитель (Али, Флорентиец, И., Ананда и др. по отношению к ученикам); с прописной
  distinguish: 'не путать с uchitel#school (школьный, музыкальный учитель, строчная: «поразили учителей» p1-c07-035). Прописная
    в RU почти всегда = духовный Учитель; но в изречении «…всякий человек тебе учитель» написание колеблется (Учитель p1-c23-070,
    учитель p2-c01-358, p2-c10-128, p3-c22-089) — смысл там один (см. formula#nikto-ne-drug). Строчная у духовного учителя
    встречается и в прямом обращении: «дорогой мой друг и учитель» p3-c19-092.'
  tier: core
  first_seen: p1-c23-070
  counts:
    p1: 1
    p2: 58
    p3: 601
  note: 'Центральное понятие части III: отношения «ученик — Учитель», «верность ученика своему Учителю». «Великий Учитель»,
    «Учитель И.», «Учитель-Владыка» (p3-c27-025) — сочетания с тем же значением.'
  evidence:
  - id: p3-c01-070
    ru: Что такое верность ученика своему Учителю?
    en_legacy: What is the disciple’s loyalty for his Teacher?
  - id: p2-c01-287
    ru: ученик идёт так, как ведёт его Учитель
    en_legacy: the disciple is going in such a way as the Master is leading him
  - id: p3-c27-025
    ru: усваивать уроки Учителя-Владыки
    en_legacy: master the Teacher-Master’s lessons
  - id: p3-c26-099
    ru: заведует сам Великий Учитель
    en_legacy: The Great Teacher himself is leading the laboratories
  en:
    term: Teacher
    legacy: Teacher ≈513 (ч. III), ≈43 (ч. II); Master ≈24 (сосредоточено в p2-c01-287…298 и p3-c25…c27, где Master служит
      и для «Владыки»); master ≈5; teacher 1
    avoid:
    - Master
    - guru
    status: proposed
  question: 'Teacher или Master? Варианты: (а) Teacher — старый перевод в ≈90% случаев; (б) Master. Доводы из текста: в части
    III есть отдельный, более высокий титул «Владыка», который старый перевод последовательно передаёт как Master (≈350);
    если «Учитель» тоже станет Master, различие «Учитель / Владыка» (p3-c25-059: «Старейшины, или, как их называет Учитель
    И., Владыки оазиса»; p3-c27-025 «Учитель-Владыка») исчезнет. Рекомендация: Teacher (с прописной, как в RU), Master оставить
    за «Владыкой».'
- id: uchitel#school
  ru: учитель
  sense: обычный учитель (гимназия, музыка, ремесло)
  distinguish: 'духовный Учитель — uchitel#spiritual; обычный: «мои познания поразили учителей» p1-c07-035, «переодеваясь…
    мог твой брат проникать как учитель» p1-c03-111'
  tier: core
  first_seen: p1-c03-111
  counts:
    p1: 9
    p2: 7
    p3: 34
  note: при правке сверять — строчная в RU не гарантирует обычного значения (p3-c19-092, p3-c19-164 — И.)
  evidence:
  - id: p1-c07-035
    ru: мои познания поразили учителей
    en_legacy: the level of my knowledge surprised the teachers
  en:
    term: teacher
    legacy: teacher ≈41; Teacher ≈8 (там, где речь о духовном учителе)
    avoid: []
    status: proposed
- id: uchenik#disciple
  ru: ученик
  sense: ученик духовного Учителя, член Общины/Братства на пути ученичества
  distinguish: 'не путать с uchenik#pupil (школьник, студент, ученик мастера): «ученицей курсов сестер милосердия» p3-c02-071'
  tier: core
  first_seen: p1-c17-114
  counts:
    p1: 4
    p2: 36
    p3: 292
  note: пара к uchitel#spiritual; «ученичество» — uchenichestvo
  evidence:
  - id: p3-c01-070
    ru: верность ученика своему Учителю
    en_legacy: the disciple’s loyalty for his Teacher
  - id: p3-c02-098
    ru: Я с радостью принимаю Вас в число моих учеников
    en_legacy: I accept you as my disciple with joy
  en:
    term: disciple
    legacy: disciple ≈295; student ≈9 (в основном другое значение); pupil 1
    avoid:
    - student
    status: proposed
- id: uchenik#pupil
  ru: ученик
  sense: школьник, студент, ученик мастера или артиста
  distinguish: духовный — uchenik#disciple
  tier: core
  first_seen: p1-c07-035
  counts:
    p1: 2
    p2: 4
    p3: 5
  note: 'критерий (правило 1): школьник, ученик мастера или артиста — pupil («мой ученик Игоро» p3-c17-058); учащийся курсов,
    университета — student (p2-c11-108 «ученица» курсов)'
  evidence:
  - id: p2-c11-108
    ru: Если вы ещё только ученица…
    en_legacy: if you are still only a student
  - id: p3-c17-058
    ru: блестящий режиссер, мой ученик Игоро
    en_legacy: an excellent director, my student Igor
  en:
    term: pupil
    legacy: student, pupil
    avoid:
    - disciple
    status: proposed
- id: uchenichestvo
  ru: ученичество
  sense: путь и состояние ученика при Учителе
  tier: core
  first_seen: p2-c01-286
  counts:
    p1: 0
    p2: 10
    p3: 49
  evidence:
  - id: p2-c01-286
    ru: Ты считал, что для тебя ученичество — это прежде всего целомудрие
    en_legacy: discipleship
  en:
    term: discipleship
    legacy: discipleship ≈50
    avoid: []
    status: proposed
- id: nastavnik
  ru: наставник / наставница
  sense: тот, кто ведёт и учит человека (И. для рассказчика, Али, Флорентиец; «наставники» Общины); у женщин — наставница
    (Дория для Наль, «наставницей в доме» для сирот)
  distinguish: 'uchitel#spiritual — RU ставит «наставника» рядом с «Учителем» как другое слово: «мой дорогой наставник, мой
    верный друг и Учитель» p3-c04-061; «Учителя, ближайшего наставника и помощника» p3-c28-040; «учителями и наставниками»
    p3-c22-089; «ближайший Учитель и наставник» p3-c23-009. Школьные «классные наставники» (p3-c24-104) — form masters по
    контексту.'
  tier: core
  first_seen: p1-c07-028
  counts:
    p1: 6
    p2: 10
    p3: 46
  note: сквозное обозначение И. в речи рассказчика ч. III («мой дорогой наставник» p3-c06-010, p3-c19-116)
  evidence:
  - id: p3-c04-061
    ru: мой дорогой наставник, мой верный друг и Учитель
    en_legacy: my dear guardian, my loyal friend and Teacher
  - id: p3-c28-040
    ru: держа за руку Учителя, ближайшего наставника и помощника
    en_legacy: while you are holding the hand of your Teacher, your closest guardian and assistant
  - id: p1-c07-028
    ru: предложили бы выбрать друга, наставника, брата
    en_legacy: I was offered to choose a friend, a guardian, a brother
  - id: p3-c23-118
    ru: сказал мне мой наставник
    en_legacy: my chief said to me
  en:
    term: mentor
    legacy: 'guardian ≈37 (сдвиг: guardian = опекун), teacher ≈14 (слияние с «Учителем»), chief ≈10, master ≈8 — в связях
      с «наставником» (61)'
    avoid:
    - guardian
    - teacher (для «наставника»)
    status: proposed
  question: 'mentor / instructor / guide? Доводы: RU отличает «наставника» от «Учителя» в одной фразе (p3-c04-061, p3-c28-040),
    поэтому teacher не годится; guardian старого EN значит «опекун»; instructor — «инструктор», слишком служебно; guide —
    возможно, но размыто. Рекомендация: mentor (наставница — mentor тоже).'
- id: vladyka#master
  ru: Владыка
  sense: 'титул высших духовных руководителей в ч. III (гл. 25–33): Владыки оазиса, Владыки мощи (p3-c26-055), Владыки Земли
    (p3-c30-092), Божественные Владыки (p3-c26-117), «старший Владыка» (p3-c25-088). Текст называет одних и тех же существ
    то Учителями, то Владыками («Учитель пятого луча» p3-c26-083 — «к Владыке этого луча» p3-c26-108; «первым Владыкой-Учителем»
    p3-c29-027), поэтому иерархию «выше Учителя» из текста не выводим'
  distinguish: 'не путать с vladyka#ruler (строчная: светский властелин, «владыкой пустыни» p3-c17-108; «новый владыка» сердца
    p2-c03-009), vladyka#god (церковнославянское «Владыко» в молитве p2-c02-039) и с vladyki-karm.'
  tier: core
  first_seen: p3-c25-046
  counts:
    p1: 0
    p2: 0
    p3: 347
  evidence:
  - id: p3-c25-088
    ru: старший Владыка еще раз поклонился И.
    en_legacy: the senior Master bowed to I. once again
  - id: p3-c25-059
    ru: Старейшины, или, как их называет Учитель И., Владыки оазиса
    en_legacy: The chiefs, or the Masters of the oasis
  - id: p3-c26-117
    ru: Эти Божественные Владыки — выше всего
    en_legacy: These Divine Masters are above everything
  en:
    term: Master
    legacy: Master ≈350; master ≈9; lord/Lord ≈9 (в основном другое значение)
    avoid:
    - Lord
    status: proposed
  question: 'Master или Lord? Довод лексический: в RU два разных слова — «Учитель» и «Владыка», и каждому нужно своё английское
    слово; Teacher занят «Учителем» (uchitel#spiritual), значит, «Владыке» остаётся Master; старый перевод последователен
    (Master ≈350). Вспомогательно: Lord в EN уже несёт «Господа» (bog, vladyka#god — там его различает контекст молитвы) и
    титул «лорд» (RU «лорд Бенедикт» ≈575, старый EN lord/Lord Benedict ≈609); для «Владыки» (365 раз) это было бы третье
    значение одного слова. Рекомендация: Master (с прописной); «Владыко» в молитве — Lord (vladyka#god).'
- id: vladyka#ruler
  ru: владыка
  sense: 'светский властелин, господин (строчная): хозяин пустыни или округа, «владыка» сердца, муж как «владыка» дочери'
  distinguish: духовный титул — vladyka#master (прописная); «Владыко» в молитве — vladyka#god; «владыки карм» — vladyki-karm
  tier: core
  first_seen: p2-c03-009
  counts:
    p1: 0
    p2: 2
    p3: 5
  note: 'критерий (правило 1): властелин места или людей — lord; «новый владыка» сердца (p2-c03-009) и муж как «владыка» (p2-c14-143)
    — master по контексту'
  evidence:
  - id: p3-c17-108
    ru: в пустыне, где я являюсь владыкой
    en_legacy: in the desert, the lord of which I am
  - id: p3-c16-110
    ru: Мы привыкли называть дедушкой нашего дорогого владыку.
    en_legacy: We got used to call our dear lord grandfather
  - id: p3-c16-159
    ru: дорогой владыка этого округа
    en_legacy: dear host of this oasis
  en:
    term: lord
    legacy: lord (p3-c16-110, p3-c17-108); host (p3-c16-159); the new person (p2-c03-009)
    avoid: []
    status: proposed
- id: vladyka#god
  ru: Владыко
  sense: церковнославянское обращение к Богу в молитве («Ныне отпущаеши раба Твоего, Владыко»)
  distinguish: духовный титул «Владыка» — vladyka#master; светский «владыка» — vladyka#ruler; «Господь/Господи» — bog
  tier: core
  first_seen: p2-c02-039
  counts:
    p1: 0
    p2: 1
    p3: 0
  note: 'молитва пастора (Песнь Симеона); связь с bog: и «Господь», и «Владыко» к Богу → Lord'
  evidence:
  - id: p2-c02-039
    ru: «Ныне отпущаеши раба Твоего, Владыко, по глаголу Твоему с миром»
    en_legacy: Lord, forgive us our sins, for we ourselves forgive everyone
    note: старый EN заменил молитву другой (из «Отче наш»)
  en:
    term: Lord
    legacy: Lord (p2-c02-039, в подменённой молитве)
    avoid: []
    status: proposed
  question: 'Молитву p2-c02-039 передать по английской библейской традиции («Lord, now lettest thou thy servant depart in
    peace, according to thy word», Nunc dimittis) или современно («Lord, now let your servant go in peace, as you have promised»)?
    Рекомендация: традиционная форма — это цитата, которую английский читатель узнаёт; thou здесь — часть цитаты, а не обращение
    персонажей (§6.3 п.8 не нарушается).'
- id: vladyki-karm
  ru: владыки карм
  sense: силы (существа), распоряжающиеся кармой людей; почти всегда во мн. ч.
  distinguish: 'титул «Владыка» — vladyka#master. RU пишет и с прописной, и со строчной: строчная — 8 (p2-c13-041, p3-c05…c10:
    «владыки карм» p3-c05-122), прописная — 18, все в p3-c26…c29 («Владыки карм» p3-c26-036, p3-c29-024), то есть RU не отделяет
    их от титула «Владыка» буквой; ед. ч. «кармы» — p3-c26-097 («Владыками кармы их этажа»).'
  tier: core
  first_seen: p2-c13-041
  counts:
    p1: 0
    p2: 1
    p3: 25
  evidence:
  - id: p3-c05-122
    ru: что такое «владыки карм», о которых ты еще ничего не знаешь
    en_legacy: who “the lords of karma”…
  - id: p3-c09-105
    ru: куда его пошлют владыки карм и рука их Учителя
    en_legacy: whom the masters of karmas or the Teacher’s hand sends
  en:
    term: Masters of karma
    legacy: Masters of karma(s) / masters of karma ≈20 (9 связей с прописной, 9 со строчной); lords of karma(s) ≈4; masters
      ≈2
    avoid:
    - lords of karma
    status: proposed
  question: 'Прописная: Masters of karma там, где в RU прописная (p3-c26…c29), и masters of karma там, где строчная (p2-c13-041,
    p3-c05…c10), — по rule#capitalized-concepts; или единообразно Masters of karma? Рекомендация: зеркалить RU. Сам термин
    — Masters of karma (старый EN, большинство; не ошибка, §9.2 п.6). lords of karma не брать: Lord сталкивается с титулом
    «лорд» (см. vladyka#master), а привычность выражения в теософской литературе — не довод из текста романа.'
- id: sanat-kumara
  ru: Санат Кумара
  sense: «Великий Бог, Господь нашей планеты» (p3-c28-038), «Защитник и Покровитель Земли» (p3-c29-033), Глава Светлого Братства
    (p3-c30-022)
  distinguish: Кумары (мн. ч.) — kumary; Маха-Чохан — maha-chohan
  tier: core
  first_seen: p3-c28-038
  counts:
    p1: 0
    p2: 0
    p3: 21
  note: имя (не титул); местоимения при нём в RU с прописной (rule#capital-pronouns). Толкований не даём — только текст
  evidence:
  - id: p3-c28-038
    ru: Великий Бог, Господь нашей планеты — Санат Кумара
    en_legacy: the Great God, the Lord of our planet – Sanat Kumara
  - id: p3-c30-022
    ru: со всем Светлым Братством, с Его Главою — Санат Кумарой
    en_legacy: with the whole Bright Brotherhood … with Her Master – Sanat Kumara
  - id: p3-c29-073
    ru: мимо рабочего места Санат Кумары
    en_legacy: through Sanat Kamara’s working place
    note: опечатка старого EN
  en:
    term: Sanat Kumara
    legacy: Sanat Kumara 20; Sanat Kamara 1 (опечатка, p3-c29-073)
    avoid:
    - Sanat Kamara
    status: proposed
- id: maha-chohan
  ru: Маха-Чохан
  sense: '«Великий Мировой Учитель», «Верховный Владыка пяти лучей» (p3-c29-053: «Великого Мирового Учителя Маха-Чохана»,
    «Верховному Владыке пяти лучей, Маха-Чохану»)'
  distinguish: Санат Кумара — sanat-kumara; «Учитель» при имени — uchitel#spiritual
  tier: core
  first_seen: p3-c29-053
  counts:
    p1: 0
    p2: 0
    p3: 6
  note: RU пишет через дефис; старый EN — без дефиса, последовательно; ошибки нет (§9.2 п.6)
  evidence:
  - id: p3-c29-053
    ru: Теперь ты видишь впервые Великого Мирового Учителя Маха-Чохана
    en_legacy: Now, for the first time you see the Great Teacher of the World Maha Chohan
    note: в корпусе связь начинается с p3-c29-051
  en:
    term: Maha Chohan
    legacy: Maha Chohan 6 (без дефиса)
    avoid: []
    status: proposed
- id: kumary
  ru: Кумары
  sense: «великие Кумары», «Великие три Кумары» — три ближайших помощника («три Его Брата») Живого Бога Земли (p3-c29-053)
  distinguish: Санат Кумара (ед., имя) — sanat-kumara; не путать род. п. «Санат Кумары» с мн. ч.
  tier: core
  first_seen: p3-c29-052
  counts:
    p1: 0
    p2: 0
    p3: 4
  evidence:
  - id: p3-c29-053
    ru: Здесь же Учитель Маха-Чохан получает мысли-шары от Великих трех Кумар непосредственно.
    en_legacy: thoughts directly from three Great Kumaras
  - id: p3-c29-052
    ru: приближаются к лучезарному облику великих Кумар
    en_legacy: they themselves are nearing the radiant image of great Kumaras
  en:
    term: the Kumaras
    legacy: Kumaras 4
    avoid: []
    status: proposed
- id: obshchina
  ru: Община
  sense: 'духовная община (Община Али, Община Раданды, «далёкая Община»): место, где живут и учатся ученики; с прописной'
  distinguish: 'строчная «община» — обычная (религиозная, сельская) община, 13 раз: p2-c17-150'
  tier: core
  first_seen: p2-c19-105
  counts:
    p1: 0
    p2: 2
    p3: 340
  evidence:
  - id: p3-c01-075
    ru: Та Община, где ты сейчас живешь, — это спасительная сеть
    en_legacy: That Community in which you are living now, - that’s the net of salvation
  - id: p2-c19-105
    ru: люди светлой Общины
    en_legacy: the people of the bright community
  en:
    term: Community
    legacy: Community ≈329 (ч. III); community (строчная) ≈8, в т. ч. для прописной p2-c19-105, p2-c20-056
    avoid:
    - commune
    - monastery
    status: proposed
  question: 'Оставить Community (старый EN, последовательно)? Альтернатив по тексту нет: Община — не монастырь: при Общине
    Али — больница и дом для сирот и беспризорных детей (p3-c06-073), в мастерских и школах Общины Раданды работают люди,
    живущие в своих семьях («мы все работаем тайно от наших семей в твоих мастерских и школах» p3-c20-206). Рекомендация:
    Community, с прописной.'
- id: svetloe-bratstvo
  ru: Светлое Братство
  sense: духовное Братство, которому служат Учителя и Общины; «Светлые Братья» — его члены
  distinguish: «Братство» с прописной в ч. III почти всегда = Светлое Братство (131 из 131). «Белое Братство» — 2 раза (p3-c18-136,
    p3-c21-057, в речи Рассула и о тайных скитах) — старый EN сливает его с Bright Brotherhood. Строчное «братство» — братство
    людей вообще (p1-c04-011 «к равенству и братству»).
  tier: core
  first_seen: p3-c18-042
  counts:
    p1: 0
    p2: 0
    p3: 123
  note: '«Светлые Братья», «Светлые Силы» — эпитет перед людьми и силами передаётся через of Light (svetly): the Brothers
    of Light; здесь — только название Братства.'
  evidence:
  - id: p3-c18-042
    ru: мир всего Светлого Братства, которое поручило мне передать вам свой привет
    en_legacy: it is from the whole Bright Brotherhood which entrusted me to give its greeting
  - id: p3-c18-136
    ru: поручиться за тебя перед Белым Братством
    en_legacy: warrant for you before the Bright Brotherhood
  en:
    term: Bright Brotherhood
    legacy: the Bright Brotherhood ≈125 (последовательно); Белое Братство → Bright Brotherhood (2 из 2); Светлые Братья →
      Bright Brothers
    avoid:
    - White Brotherhood (для «Светлого»)
    status: proposed
  question: '(1) Название: Bright Brotherhood (старый EN, ≈125, последовательно) или Brotherhood of Light? Доводы за of Light
    (языковое ревью): bright о людях по-английски значит прежде всего «сообразительный, жизнерадостный»; «of Light» устойчиво
    в английской прозе этого рода и даёт пару к the dark powers; эпитет перед людьми и силами уже переведён на of Light (svetly),
    и Brothers of Light рядом с Bright Brotherhood — несимметрично. Доводы за Bright Brotherhood: старый вариант не ошибочен
    как имя собственное (§9.2 п.6), к названию организации значение «смышлёный» не прилипает. Рекомендация: Bright Brotherhood;
    Brotherhood of Light — если владелец хочет единый эпитет с Brothers of Light. (2) «Белое Братство» (2 раза) — сохранить
    отличие от «Светлого»: White Brotherhood? Текст не говорит прямо, одно ли это братство. Рекомендация: White Brotherhood,
    как в RU (не додумывать тождество).'
- id: brat#sibling
  ru: брат
  sense: родной брат (Николай — брат Левушки)
  distinguish: 'brat#fellow — брат по Общине/Братству и обращение «брат мой». «Двоюродный брат» в ч. I — легенда для окружающих:
    И. выдаёт Левушку за своего кузена («моего двоюродного брата Лёвушку Т.» p1-c17-044), хотя он грек и не родственник («Другой
    мой друг — грек» p1-c07-027); «мой брат И.» (p1-c15-026) — часть той же легенды или братство по духу, но не родство. «брат-отец»
    (Николай, 26 раз) — characters.yml, nikolay.'
  tier: core
  first_seen: p1-c01-003
  counts:
    p1: 429
    p2: 87
    p3: 485
  note: «брат-отец» (Николай о себе, p1-c01-066) — brother-father, как в старом EN.
  evidence:
  - id: p1-c26-058
    ru: Брат Николай — невоспитанный человек!?
    en_legacy: My brother Nikolay is ill-mannered person?
  en:
    term: brother
    legacy: brother
    avoid: []
    status: proposed
- id: brat#fellow
  ru: брат (сестра)
  sense: 'член Общины/Братства и обращение между ними: «брат Франциск», «сестра Александра», «брат Левушка», «Мир тебе, брат
    мой милый», «братья и сестры» в речах Учителей, «Светлые Братья»'
  distinguish: родство — brat#sibling; различать по контексту Общины (ч. III), имени после слова, речи Учителя
  tier: core
  first_seen: p3-c01-067
  counts:
    p1: 0
    p2: 0
    p3: 60
  note: 'в речи Учителей: «братья и сёстры» — brothers and sisters, без архаичного brethren (старый EN: brothers 14, my brothers
    1, brethren 0; my sister 3); «сестра милосердия» — nurse (другое слово); «сестра Али Махмуд» (p1-c01-033) — родная сестра.
    Sister перед именем — к тому же британский титул старшей медсестры: подходит к «сестре Александре», старшей сестре больницы
    Общины (p3-c03-059; старый EN — nurse Alexandra 15, sister Alexandra 3).'
  evidence:
  - id: p3-c02-240
    ru: Мир тебе, брат мой милый
    en_legacy: Peace to you, my dear brother
  - id: p3-c01-067
    ru: все твои братья и сестры, идущие путем труда и совершенствования
    en_legacy: all of them are your brothers and sisters who are walking the path of their development and work
  - id: p3-c06-076
    ru: — Счастлива твоя жизнь, смиренная сестра моя
    en_legacy: “Your life is happy, my obedient sister,
  en:
    term: 'brother (сестра — sister); перед именем — с прописной: Brother Francis, Sister Alexandra'
    legacy: 'brother/sister перед именем всегда со строчной: brother Francisco 9, sister Carlota 7, sister Gerda 6 …'
    avoid: []
    status: proposed
  question: 'Писать ли титул перед именем с прописной (Brother Francis, Sister Gerda — английская норма для членов религиозных
    общин) или со строчной, как в RU и старом EN? Рекомендация: с прописной перед именем («Brother Francis»), со строчной
    в обращении без имени («my brother»).'
- id: zhizn#life-divine
  ru: Жизнь
  sense: Жизнь как высшее начало (живая, Единая, Великая Жизнь), с прописной; личное «Она», «Сама Жизнь»
  distinguish: 'обычная «жизнь» со строчной (2800+ раз) — life. Прописная в середине предложения различает: «Жизнь есть Вечное
    Движение» p3-c25-039 / «в жизни дня». Составные — velikaya-zhizn, edinaya-zhizn, mat-zhizni.'
  tier: core
  first_seen: p1-c14-034
  counts:
    p1: 11
    p2: 54
    p3: 324
  evidence:
  - id: p3-c25-039
    ru: Вы знаете, что Жизнь есть Вечное Движение
    en_legacy: You know that Life is the Eternal Movement.
  - id: p3-c21-081
    ru: Не передышки посылает Жизнь своим верным слугам, но Сама оживает в сердцах
    en_legacy: Life is sending not a break… but Life Himself comes to life in the hearts
  en:
    term: Life
    legacy: 'Life ≈265; life ≈55 (прописная потеряна); «Сама Жизнь» → Life Himself / himself — 18 раз (p3-c20-116 … p3-c33-039):
      ошибка рода'
    avoid:
    - Life Himself
    status: proposed
  question: 'Какое местоимение для Жизни: it/itself или She/Herself? Himself — точно ошибка. Доводы из текста за She: RU последовательно
    олицетворяет Жизнь прописным «Она/Ее/Сама» в поучениях («Он включен в труд Самой Жизни. Он один из Ее винтов» p3-c23-004;
    «как Сама Жизнь готовит ступени… где и как Она находит нужным» p3-c23-013); Life itself по-английски читается как «жизнь
    как таковая» и теряет олицетворение «Самой Жизни»; при it для Жизни и She для Великой Матери Жизни (mat-zhizni) у одного
    образа будут два разных местоимения. Доводы за it: английская норма для абстрактных понятий; She для Life непривычно.
    Рекомендация — стилистическая, не из текста: it/itself по умолчанию, She/Herself там, где Жизнь прямо олицетворена (Сама
    Жизнь, Она с прописной, Мать Жизнь). Если владелец ставит верность образу RU выше английской нормы — She/Herself везде.
    См. rule#capital-pronouns.'
- id: velikaya-zhizn
  ru: Великая Жизнь
  sense: то же высшее начало с эпитетом «великая»; даёт человеку «подарки», защиту, помощь
  tier: core
  first_seen: p2-c09-080
  counts:
    p1: 0
    p2: 2
    p3: 11
  note: 'с определённым артиклем везде, кроме звательного обращения: без артикля Great Life читается как имя собственное (ср.
    the Great Mother, the One Life)'
  evidence:
  - id: p3-c01-076
    ru: новый подарок, который тебе дала Великая Жизнь
    en_legacy: the new present which Great Life gives to you
  - id: p3-c18-148
    ru: дает Великая Жизнь в последний раз Свою защиту
    en_legacy: For the last time the Great Life gives its protection to you
  en:
    term: the Great Life
    legacy: 'Great Life ≈4 (с артиклем и без: the Great Life p3-c18-148); просто Life ≈7 (эпитет теряется)'
    avoid: []
    status: proposed
- id: edinaya-zhizn
  ru: Единая Жизнь
  sense: Жизнь как единое целое, частицами которой являются все существа
  distinguish: не путать с velikaya-zhizn; «частица Единой Жизни» p3-c07-064, «волна Единой Жизни» p3-c04-095
  tier: core
  first_seen: p2-c06-105
  counts:
    p1: 0
    p2: 1
    p3: 20
  evidence:
  - id: p3-c07-063
    ru: с момента твоего рождения к Единой Жизни
    en_legacy: from your birth for the Only One Life
  - id: p3-c07-064
    ru: к такому сознанию себя частицей Единой Жизни, единицей всей вселенной
    en_legacy: who felt to be the part of the Only One Life, the part of the entire universe
  en:
    term: the One Life
    legacy: the Only One Life ≈22 по корпусу ч. III (калька); Life / life ≈12 (эпитет потерян)
    avoid:
    - Only One Life
    - United Life
    status: proposed
  question: 'the One Life или the Single Life / the Whole Life? Only One Life — неидиоматичная калька. Рекомендация: the One
    Life (согласуется с edinyi → the One).'
- id: edinyi
  ru: Единый (Единое)
  sense: 'высшее единое начало (субстантив): «аспекты Единого» p3-c04-049, «Бог Един»'
  distinguish: прилагательное «Единая Жизнь/Сущность/Любовь» — edinaya-zhizn и др.; строчное «единый» — обычное прилагательное
  tier: core
  first_seen: p2-c04-045
  counts:
    p1: 0
    p2: 2
    p3: 85
  evidence:
  - id: p3-c09-012
    ru: поскольку в нем движутся все аспекты Единого
    en_legacy: Since all the aspects of the Only One are operating within him
  - id: p3-c04-049
    ru: пока… весь Единый в человеке не загорится
    en_legacy: until the whole the Only One bursts into flame in man
  en:
    term: the One
    legacy: the Only One ≈36; One ≈43 (часто в составе Only One); по корпусу ч. III «of the Only One» 50 раз
    avoid:
    - the Only One
    status: proposed
  question: the One (рекомендация) или the Only One (старый EN)? Only One по-английски значит «единственный», а не «единый».
- id: velikaya-mat
  ru: Великая Мать
  sense: высшее женское начало, к которому обращены молитвы; в Общине Раданды — её часовня и статуя («часовня Звучащей Радости
    Великой Матери»); личные местоимения Она/Ее/Ты с прописной
  distinguish: см. mat-zhizni (Великая Мать Жизни / Мать Жизни); не путать с «мать Анна» (настоятельница Общины в оазисе,
    p3-c23-117 — characters.yml, mat-anna)
  tier: core
  first_seen: p2-c06-011
  counts:
    p1: 0
    p2: 2
    p3: 97
  evidence:
  - id: p3-c20-125
    ru: О, Великая Мать, сгореть в огне и отдать жизнь хочу я в этот миг
    en_legacy: Oh, Great Mother, in this moment I desire to burn down in Your fire
  - id: p3-c20-116
    ru: припадем к стопам дивной статуи Великой Матери
    en_legacy: we are going to embrace the feet of the wonderful statue of Great Mother
  en:
    term: the Great Mother
    legacy: the Great Mother (по корпусу ч. III «the Great Mother» ≈85) — последовательно, кроме «Матери Жизни»
    avoid: []
    status: proposed
- id: mat-zhizni
  ru: Мать Жизни (Великая Мать Жизни, Матерь Жизнь)
  sense: Великая Мать как сама Жизнь; «ожерелье Матери Жизни» (образ из ч. I, p1-c14-034, повторяется в ч. III)
  tier: core
  first_seen: p1-c14-034
  counts:
    p1: 1
    p2: 3
    p3: 7
  note: 'различать как в RU: «Мать Жизни» (родительный: «Милосердие Великой Матери Жизни» p2-c15-142) → the (Great) Mother
    of Life; приложение «Мать Жизнь / Матерь Жизнь» (Жизнь и есть Мать: «И Великая Мать Жизнь не осудит тебя» p3-c22-116)
    → the Great Mother Life, по модели Mother Earth, Mother Nature. Father — ошибка в любом случае.'
  evidence:
  - id: p3-c22-116
    ru: И Великая Мать Жизнь не осудит тебя
    en_legacy: and the Great Father Life won’t condemn you, he will give the shelter of his Kindness
  - id: p2-c15-142
    ru: Милосердие Великой Матери Жизни не похоже на милосердие людей
    en_legacy: compassion of the Great Father-Life doesn’t look like the one of people
  - id: p3-c32-108
    ru: вверьте себя Великой Матери Жизни, вберите в сознание Ее закон целесообразности
    en_legacy: Believe in the Great Father Life very strongly, put the law of Life’s accuracy into your consciousness
  - id: p2-c06-011
    ru: в любви неугасимой Великой Матери Жизни
    en_legacy: in the unquenchable love of the Great Mother – Life
  en:
    term: the Mother of Life (с эпитетом — the Great Mother of Life); приложение «(Великая) Мать/Матерь Жизнь» — the Great
      Mother Life
    legacy: 'ОШИБКА РОДА: Father Life / Great Father(-)Life — 7 раз (p2-c15-142, p3-c15-078, p3-c18-160, p3-c22-116, p3-c27-031,
      p3-c32-108, p3-c32-116) + «he/his» при нём; верно Mother-Life / Mother – Life — 4 раза (p1-c03-110, p2-c06-011, p3-c13-065,
      p3-c13-074); p1-c14-034 и p2-c04-029 («великая Матерь Жизнь» → life) — опущено'
    avoid:
    - Father Life
    - Great Father Life
    status: proposed
- id: vechnost
  ru: Вечность
  sense: вечность как высшая реальность («живая Вечность», «огонь Вечности», «стоять перед Вечностью на дежурстве»)
  distinguish: 'не путать с vechnoe («Вечное» — субстантив, the Eternal). В RU оба стоят рядом: «сердце ваше жило в Вечном…
    кроме той Вечности, что звучит в…» p2-c17-108. Строчная «вечность» (26 раз) — обиходное «целая вечность» p3-c01-080.'
  tier: core
  first_seen: p2-c01-307
  counts:
    p1: 0
    p2: 23
    p3: 80
  evidence:
  - id: p3-c01-066
    ru: чье сознание раскрыло человеку его живую Вечность, которую он в себе носит
    en_legacy: whose consciousness has comprehended the living Eternity within themselves
  - id: p3-c01-071
    ru: видеть в них каплю огня Вечности
    en_legacy: who see the sparkle of fire of Eternity in them
  en:
    term: Eternity
    legacy: Eternity ≈88; Eternal ≈7; eternity 2
    avoid: []
    status: proposed
- id: vechnoe
  ru: Вечное
  sense: субстантив «Вечное» — вечное начало, то, что вечно в человеке и мире («жить в Вечном», «читай в каждой форме ее Вечное»)
  distinguish: vechnost — Вечность (существительное); прилагательное «вечный» перед существительным — обычное eternal
  tier: core
  first_seen: p2-c05-003
  counts:
    p1: 0
    p2: 8
    p3: 77
  evidence:
  - id: p2-c17-108
    ru: зная, что сердце ваше жило в Вечном
    en_legacy: your heart was living in Eternity
  - id: p3-c04-202
    ru: Читай в каждой временной форме ее Вечное
    en_legacy: In every temporary form read her Eternity
  - id: p3-c09-060
    ru: жить только в творчестве Вечного
    en_legacy: (the Eternal — один из 4 случаев)
  en:
    term: the Eternal
    legacy: 'СЛИЯНИЕ: Eternity ≈70 из 85; the Eternal/Eternal ≈10'
    avoid:
    - Eternity (для «Вечного»)
    status: proposed
  question: 'Различать Вечное (the Eternal) и Вечность (Eternity), как RU? Рекомендация: да — в тексте они стоят рядом (p2-c17-108).'
- id: vechnoe-dvizhenie
  ru: Вечное Движение
  sense: закон непрерывного движения Жизни; «человек как единица Вечного Движения» (название книги Николая Т., p1-c14-098)
  tier: core
  first_seen: p1-c14-098
  counts:
    p1: 1
    p2: 1
    p3: 16
  evidence:
  - id: p3-c09-012
    ru: Он — единица Вечного Движения
    en_legacy: He is the little part of the Eternal Movement
  - id: p1-c14-098
    ru: «Человек, как единица Вечного Движения»
    en_legacy: “Man – a part of the eternal movement”
  en:
    term: Eternal Movement
    legacy: the Eternal Movement ≈15 в ч. III; movement со строчной в ч. I
    avoid:
    - Eternal Motion
    status: proposed
- id: svet#light-divine
  ru: Свет
  sense: высший, духовный свет («Свет Вечности», «путь Света», «Свет и Мир в человеке»); прописная
  distinguish: 'svet#light — физический свет (строчная, «свет луны»); svet#society — «высший свет» (общество); «на свете»,
    «тот свет», «весь свет» — svet#world. Прописная в RU различает: «видишь в человеке… его Свет и Мир» p3-c05-100.'
  tier: core
  first_seen: p1-c24-214
  counts:
    p1: 6
    p2: 30
    p3: 210
  evidence:
  - id: p3-c03-103
    ru: проникнуть в заложенные в человеке Свет и Мир
    en_legacy: to penetrate into the Light and Calm that are hidden within man
  - id: p3-c10-156
    ru: Твое же все растаяло, все превратилось в Свет
    en_legacy: everything has turned into the Light
  en:
    term: Light
    legacy: Light ≈184; light ≈20
    avoid: []
    status: proposed
- id: svet#light
  ru: свет
  sense: физический свет; также переносно без прописной («свет и тепло», «ленты света»)
  distinguish: духовный Свет — svet#light-divine; «на свете», «тот свет» — svet#world; «высший свет» — svet#society; при строчной
    в поучении сверять смысл
  tier: core
  first_seen: p1-c01-053
  counts:
    p1: 67
    p2: 66
    p3: 130
  evidence:
  - id: p2-c18-033
    ru: в которое лился мерцающий свет луны
    en_legacy: through which the colourless light of the moon was pouring
  en:
    term: light
    legacy: light ≈213 (все строчные «свет», кроме «на свете»)
    avoid: []
    status: proposed
- id: svet#society
  ru: свет (высший свет)
  sense: светское общество
  distinguish: не путать с svet#light, svet#light-divine и svet#world; «светский» — society
  tier: core
  first_seen: p1-c07-116
  counts:
    p1: 7
    p2: 10
    p3: 2
  evidence:
  - id: p2-c03-064
    ru: избранным представителям высшего света
    en_legacy: the chosen members of the high society
  en:
    term: society
    legacy: high society, society
    avoid:
    - light
    status: proposed
- id: svet#world
  ru: свет (на свете, тот свет)
  sense: 'мир, земная жизнь: «на свете», «по свету», «весь/белый свет», «тот свет» (загробный мир), «Свет объездил»'
  distinguish: svet#light — свет как освещение («свет луны» p2-c18-033); svet#society — «высший свет»; svet#light-divine —
    Свет с прописной. «Тот свет» бывает и светом («в тот свет, что сияет за дверью» p3-c12-005) — сверять по контексту. Синоним
    mir#world.
  tier: core
  first_seen: p1-c05-017
  counts:
    p1: 16
    p2: 29
    p3: 23
  note: обиходное значение, чаще в идиомах («забыл обо всём на свете», «больше всего на свете»)
  evidence:
  - id: p1-c06-118
    ru: на свете нет чудес
    en_legacy: There aren’t any secrets in the world
  - id: p1-c20-132
    ru: Свет объездил — забавней мальчонки не видал!
    en_legacy: I have travelled all over the world, but I haven’t met a more interesting lad!
  - id: p1-c17-011
    ru: забыв обо всём на свете
    en_legacy: having forgotten everything in the world
  - id: p2-c07-013
    ru: чтобы он преследовал нас и с того света
    en_legacy: follow us from another world
  en:
    term: world
    legacy: 'world — «на свете» → in the world ≈35 из 49 связей (остальное перефразировано или опущено: p1-c05-017, p1-c18-168);
      «на тот свет» → by killing me (p1-c22-042), from another world (p2-c07-013)'
    avoid:
    - light (для «на свете»)
    status: proposed
- id: svetly
  ru: Светлый (с прописной)
  sense: 'эпитет высшего мира: Светлое Братство, Светлые Братья, Светлые Силы, Светлая Община'
  distinguish: строчное «светлый» — обычное bright/light; «светлые силы» со строчной (12) — пара к temnye-sily
  tier: core
  first_seen: p3-c02-219
  counts:
    p1: 2
    p2: 0
    p3: 148
  note: bright о людях по-английски читается как «сообразительный, жизнерадостный» («Bright Brothers» — «смышлёные братья»),
    о силах — «яркий»; of Light передаёт «принадлежащий высшему Свету» и даёт пару к the dark powers (temnye-sily). Название
    Братства — отдельный вопрос (svetloe-bratstvo).
  evidence:
  - id: p3-c18-042
    ru: всего Светлого Братства
    en_legacy: the whole Bright Brotherhood
  en:
    term: of Light (the Brothers of Light, the Powers of Light, the Community of Light); «Светлое Братство» — svetloe-bratstvo
    legacy: Bright ≈129; Light 5; White 1
    avoid:
    - 'Bright (перед людьми и силами: Bright Brothers, Bright Powers)'
    status: proposed
- id: mir#peace
  ru: мир
  sense: покой, умиротворённость, отсутствие вражды — внутреннее состояние, которое «несут» людям; в формулах приветствия
    и благословения
  distinguish: 'не путать с mir#world (вселенная, человечество, «мир форм», «внутренний мир» = душевный мир человека) и mir-vselennaya.
    Признаки значения «покой»: «нести/хранить/лить мир», «мир в сердце», пары «мир и радость / любовь / доброта», «с миром»,
    «Мир тебе». Прописная «Мир» (16 раз) в ч. III — почти всегда покой: «Свет и Мир в человеке» p3-c05-100, «блаженство Мира»
    p3-c08-105 — но «Мир-Вселенная» — mir-vselennaya.'
  tier: core
  first_seen: p1-c02-016
  counts:
    p1: 33
    p2: 49
    p3: 178
  note: 'Одно из главных слов поучений: «Храни мир, носи его всюду» (p1-c14-068), «иди с миром».'
  evidence:
  - id: p1-c02-016
    ru: может быть только миром, утешением и радостью
    en_legacy: She could be only peace, comfort and joy
  - id: p1-c14-068
    ru: Я с тобой, мой друг. Храни мир, носи его всюду и встретишь меня
    en_legacy: I’m with you, my friend. Keep calm, spread your calm everywhere and you will meet me soon.
  - id: p3-c01-075
    ru: кто хочет жить для общего блага, для мира и радости людей
    en_legacy: who want to live for the common welfare, for the people’s calm and joy
  - id: p3-c01-078
    ru: каждую встречу сумеешь начать и кончить в радости и мире
    en_legacy: begin and to start your every meeting calmly and joyfully
  en:
    term: peace
    legacy: 'СИСТЕМАТИЧЕСКАЯ ОШИБКА (ч. III): из ≈178 размеченных «мир-покой» в ч. III — calm ≈104, tranquillity ≈25, peace
      ≈23, harmony 4; в ч. I — peace ≈17, calm ≈7; в ч. II — peace ≈18, calm ≈13. Гипотеза отчёта этапа 2 (§5) подтверждена:
      в ч. III «мир» → calm — норма старого перевода, а не случайность. «Мир тебе/вам» при этом → Peace to you (5 из 5, formula#mir-tebe).'
    avoid:
    - calm
    - tranquillity
    - calmness
    status: proposed
  question: 'Утвердить peace для всех «мир-покой», включая формулы и пары («в радости и мире» → in joy and peace)? Решать
    вместе со spokoistvie (calm) и pokoy (tranquillity): RU ставит эти слова рядом как разные («мир и спокойствие» 11 раз,
    p3-c04-094; «мир и покой» p3-c18-020, «Нет ни покоя, ни мира» p3-c16-016), а старый EN отдаёт «спокойствию» peace ≈43
    раза — после замены calm → peace для «мира» понятия сольются в обратную сторону, если у «спокойствия» и «покоя» не будет
    своих переводов. Рекомендация: мир-покой → peace, спокойствие → calm, покой → tranquillity (подробности — в тех записях).'
- id: mir#world
  ru: мир
  sense: 'мир как совокупность людей, вещей, сфера бытия: «в широкий мир», «мир форм», «весь мир», «внутренний мир»'
  distinguish: mir#peace — покой; mir-vselennaya; «на свете» — тоже world (svet#world)
  tier: core
  first_seen: p1-c02-101
  counts:
    p1: 33
    p2: 66
    p3: 245
  evidence:
  - id: p1-c02-126
    ru: чтобы уже больше не явиться в нашем мире
    en_legacy: so that nobody could see them again in this world
  - id: p1-c13-094
    ru: Приведите в такой же порядок свой внутренний мир
    en_legacy: Arrange your inner world exactly as you have tried to arrange your exterior.
  - id: p2-c06-111
    ru: только её внутренний мир, духовная высота и благородство важны
    en_legacy: only her inner calm, her spiritual height and nobility were important
  en:
    term: world
    legacy: world ≈218 из 245 размеченных; calm ≈32, peace ≈25 (часть — шум окна, часть — ошибки вроде «внутренний мир» →
      inner calm, p2-c06-111)
    avoid: []
    status: proposed
- id: mir-vselennaya
  ru: Мир-Вселенная
  sense: мир как вселенная — через дефис, в надписях на скрижалях и поучениях гл. 22, 26
  tier: core
  first_seen: p3-c22-119
  counts:
    p1: 0
    p2: 0
    p3: 5
  evidence:
  - id: p3-c26-122
    ru: Мир-Вселенная есть часть Истины
    en_legacy: The World-Universe is a part of the Truth
  - id: p3-c22-119
    ru: Думайте чаще и больше о Мире-Вселенной
    en_legacy: Think about the World, about the Universe more and more often
  en:
    term: the World-Universe
    legacy: 'The World-Universe в надписях на скрижалях (p3-c26-122, 136); the World, (into) the Universe — в прозе (p3-c22-119,
      p3-c26-075): распадается на два слова'
    avoid: []
    status: proposed
  question: 'Сохранить дефисную пару (the World-Universe) или передать одним словом (the Universe)? Рекомендация: the World-Universe
    в надписях на скрижалях (p3-c26-122, 136), где форма значима.'
- id: spokoistvie
  ru: спокойствие
  sense: 'ровное, невозмутимое состояние человека (внешнее и внутреннее): «величавое спокойствие» восточных людей, «полное
    спокойствие и самообладание»'
  distinguish: 'не путать с mir#peace и pokoy: RU ставит их рядом как разные слова — «мир и спокойствие» (11 раз: p3-c04-094,
    p2-c17-018), «спокойствие и мир» (p2-c06-009, p2-c17-134). Прилагательное «спокойный», наречие «спокойно» — calm/calmly
    по контексту, отдельно не заводятся.'
  tier: core
  first_seen: p1-c01-007
  counts:
    p1: 28
    p2: 44
    p3: 65
  note: пара к «самообладанию» (samoobladanie) и одно из постоянных требований к ученику; есть в пилотной главе (p1-c01-007)
  evidence:
  - id: p1-c01-007
    ru: И восточные люди, с их величавым спокойствием
    en_legacy: And all of these Eastern people with their grand calm
  - id: p1-c02-071
    ru: Полное спокойствие и самообладание
    en_legacy: I was feeling full of self-control and peace
  - id: p3-c04-094
    ru: Мое радужное счастье, мир и спокойствие
    en_legacy: My joyous happiness, peace and tranquillity
  - id: p2-c06-009
    ru: Удивительное спокойствие и мир нисходят в мою душу.
    en_legacy: A wonderful calm and tranquillity is descending into my soul
  en:
    term: calm
    legacy: calm ≈81, peace ≈43, tranquillity ≈26 (связи со «спокойствием» из 127; в связи бывает несколько слов)
    avoid:
    - peace
    status: proposed
  question: 'Утвердить calm для «спокойствия» вместе с mir#peace (peace) и pokoy (tranquillity)? Доводы: RU различает три
    слова в одних и тех же фразах («мир и спокойствие» p3-c04-094; «мир и покой» p3-c18-020); calm — вариант большинства старого
    EN; peace для «спокойствия» (≈43) после правки mir#peace даст обратное слияние («мир и спокойствие» → «peace and peace»).
    Рекомендация: calm; peace не использовать; tranquillity оставить «покою».'
- id: pokoy
  ru: покой
  sense: (1) внутренний покой, умиротворённость («неизреченный покой охватил Генри», «тот покой, тот благостный мир»); (2)
    отсутствие беспокойства, тишина, отдых («нарушать покой», больному «нужен только полный покой»); (3) идиомы «оставить
    в покое», «не давать покоя»
  distinguish: 'mir#peace и spokoistvie — RU ставит «покой» и «мир» рядом как разные: «мир и покой» p3-c18-020, «Нет ни покоя,
    ни мира» p3-c16-016, «тот покой, тот благостный мир» p3-c18-055, «покой и мир» p2-c11-185. «Покои» (комнаты) и «упокой»
    — другие слова.'
  tier: core
  first_seen: p1-c07-022
  counts:
    p1: 9
    p2: 19
    p3: 23
  note: 'критерий (правило 1): внутреннее состояние — tranquillity; тишина, отдых, «нарушать покой» — quiet или rest по контексту
    («the patient needs complete rest» p3-c11-072); идиомы — leave (someone) in peace / alone, give (someone) no peace: в
    устойчивых английских идиомах peace допустимо, это не «мир-покой» поучений'
  evidence:
  - id: p3-c18-055
    ru: Запомните навсегда тот покой, тот благостный мир
    en_legacy: Forever remember this peace, this pleasing calm
    note: покой и мир переставлены
  - id: p2-c14-120
    ru: Блаженство, мир, гармония, неизреченный покой охватили Генри
    en_legacy: Henry was covered with bliss, tranquillity, harmony, inexpressible calm
  - id: p3-c11-072
    ru: Больному нужен только полный покой
    en_legacy: The patient needs an absolute tranquillity
  - id: p2-c09-018
    ru: оставьте меня в покое
    en_legacy: leave me in peace
  en:
    term: tranquillity
    legacy: peace ≈24, calm ≈19, tranquillity ≈7, rest/repose 5 (связи с «покоем» из 51)
    avoid:
    - calm (для «покоя»)
    status: proposed
  question: 'tranquillity (внутреннее состояние), rest/repose или peace? Доводы: peace сольёт «покой» с «миром-покоем», а
    RU их различает (p3-c18-020, p3-c16-016, p3-c18-055); calm уже отдан «спокойствию»; rest/repose передают отдых, но не
    умиротворённость («неизреченный покой» p2-c14-120). Рекомендация: tranquillity для внутреннего покоя, quiet/rest для тишины
    и отдыха (критерий в note); peace — только если владелец сознательно сольёт «покой» с «миром».'
- id: vselennaya
  ru: вселенная
  sense: вселенная; в поучениях — «единица вселенной», «гармония вселенной»; с прописной — реже (48 раз в середине предложения)
  distinguish: прописная/строчная в RU колеблется без различия смысла (ч. II — Вселенная 28, ч. III — 15 при 183 всего)
  tier: core
  first_seen: p1-c03-107
  counts:
    p1: 23
    p2: 45
    p3: 183
  evidence:
  - id: p3-c07-064
    ru: частицей Единой Жизни, единицей всей вселенной
    en_legacy: the part of the entire universe
  en:
    term: universe
    legacy: universe ≈191; Universe ≈14; world ≈14
    avoid: []
    status: proposed
- id: lyubov
  ru: любовь / Любовь
  sense: любовь; с прописной — Любовь как высшее начало и «аспект» Единого («Любовь, Мир, Радость, Бесстрашие»)
  distinguish: 'прописная в RU (6/30/238) различает Любовь-начало и человеческое чувство (строчная, 1134 раза); строчная бывает
    и в поучениях. Отдельной записи на «Любовь» не заводим: слово одно, различие — прописной буквой (см. rule#capitalized-concepts).'
  tier: core
  first_seen: p1-c01-040
  counts:
    p1: 204
    p2: 375
    p3: 829
  evidence:
  - id: p3-c10-044
    ru: Да прольется Любовь моя к ранам его
    en_legacy: Let my Love pour into his wounds
  en:
    term: love / Love (как в RU)
    legacy: love ≈1001; Love ≈185 для прописной (Love ≈172 из 205 в ч. III), ≈56 для строчной
    avoid: []
    status: proposed
- id: radost
  ru: радость
  sense: радость — одно из главных требований учения («радость — масло» для двигателя жизни, p3-c01-076); с прописной — начало
    (Радость, «гонец Радости»)
  distinguish: не путать с «радостность» (34 раза, свойство характера — joyfulness) и «бодрость» (bodrost). Прописная различает
    Радость-начало (71 раз в середине предложения в ч. III); см. zvuchashchaya-radost.
  tier: core
  first_seen: p1-c01-006
  counts:
    p1: 100
    p2: 137
    p3: 512
  evidence:
  - id: p3-c01-076
    ru: Знание — двигатель жизни, и радость — масло для него.
    en_legacy: Knowledge – that’s the engine of life, while joy – that’s the lubricant for it.
  en:
    term: joy / Joy (как в RU)
    legacy: joy ≈925; happy ≈44; glad ≈26
    avoid: []
    status: proposed
- id: zvuchashchaya-radost
  ru: Звучащая Радость
  sense: имя-эпитет Великой Матери и название её часовни («часовня Звучащей Радости», p3-c27-024)
  tier: core
  first_seen: p3-c21-060
  counts:
    p1: 0
    p2: 0
    p3: 15
  evidence:
  - id: p3-c21-116
    ru: чтобы Ты, Звучащая Радость, послала им помощь и оправдание
    en_legacy: so that You, Ringing Joy, would send help and justification to them
  - id: p3-c27-024
    ru: 'великое название часовни… часовни Великой Матери: «Звучащая Радость»'
    en_legacy: 'the great name of the chapel of the Great Mother…: “The Ringing Joy”'
  en:
    term: Ringing Joy
    legacy: 'Ringing Joy (≈12 по корпусу ч. III: «chapel of Ringing Joy», «the Ringing Joy»)'
    avoid: []
    status: proposed
  question: 'Ringing Joy (старый EN, последовательно) или Sounding/Resounding Joy (ближе к «звучащая»)? Ошибки нет — рекомендация:
    Ringing Joy.'
- id: miloserdie
  ru: милосердие
  sense: милосердие — деятельная пощада и помощь; с прописной — Милосердие как высшее начало («ступени Милосердия», «братья
    Милосердия»)
  distinguish: 'не путать с sostradanie (сострадание), zhalost (жалость) и poshchada (пощада). RU различает их в одной фразе:
    «Ничье милосердие, ничье сострадание, ничья помощь…» p3-c04-136; «Пощада есть закон милосердия… в ней выражается не сострадание»
    p3-c32-028; перечень «милосердия, доброты, любви, жалости, сострадания» p3-c17-158. Идиома «сестра/брат милосердия» (сиделка,
    санитар) — nurse (p1-c15-027, p1-c26-221, p3-c02-071).'
  tier: core
  first_seen: p1-c06-031
  counts:
    p1: 30
    p2: 55
    p3: 147
  evidence:
  - id: p3-c01-079
    ru: начать и кончить каждую из них в мире, милосердии и доброте
    en_legacy: to begin and to start each of them calmly, with compassion and kindness
  - id: p3-c04-136
    ru: Ничье милосердие, ничье сострадание, ничья помощь не могут помочь
    en_legacy: Nobody’s compassion or help is able to help (одно из двух слов потеряно)
  - id: p3-c32-028
    ru: Пощада есть закон милосердия.
    en_legacy: Mercy – that’s the law of regret.
  - id: p2-c14-115
    ru: идти в вечной верности с братьями Милосердия
    en_legacy: to be for ever loyal to brothers of Compassion
  en:
    term: mercy
    legacy: 'compassion ≈178 из 232; mercy ≈4 (+ «Mercy» для «пощады» p3-c32-028); kind(ness) ≈11. Прилагательное: compassionate
      ≈53, merciful 2'
    avoid:
    - compassion (для «милосердия»)
    status: proposed
  question: 'mercy или compassion? Что меняется: старый EN отдаёт «милосердию» compassion в ≈178 местах из 232, то есть mercy
    — отказ от варианта большинства. Почему: «сострадание» — отдельное понятие, стоящее рядом (p3-c04-136 «Ничье милосердие,
    ничье сострадание…», p3-c17-158), и старый EN уже отдаёт ему compassion (≈41); если оба слова → compassion, различие исчезает
    — так и случилось в p3-c04-136. Это довод о различении понятий, а не вкус. Последствие: английское mercy прежде всего
    значит «пощада, помилование», а старый EN отдаёт mercy и «пощаде» (p3-c32-028, p3-c32-157), поэтому «пощада» получает
    своё слово (poshchada → clemency), иначе возникнет новое слияние «милосердие = пощада = mercy» там, где RU их различает
    («Пощада есть закон милосердия» p3-c32-028). Рекомендация: милосердие → mercy (Милосердие → Mercy, милосердный → merciful),
    сострадание → compassion, жалость → pity, пощада → clemency — утверждать четыре записи вместе.'
- id: sostradanie
  ru: сострадание
  sense: сострадание, со-чувствие чужой боли
  distinguish: miloserdie — милосердие; «жалость» — pity; «сочувствие» (если встретится) — sympathy
  tier: core
  first_seen: p1-c07-029
  counts:
    p1: 19
    p2: 25
    p3: 29
  evidence:
  - id: p3-c17-158
    ru: 'всех человеческих чувств: милосердия, доброты, любви, жалости, сострадания'
    en_legacy: all human feelings within himself – compassion, kindness, love, sympathy, pity (жалость и сострадание переставлены)
  - id: p1-c09-103
    ru: его сострадания к этой женщине
    en_legacy: his sympathy to the woman
  en:
    term: compassion
    legacy: compassion ≈41; sympathy ≈24
    avoid:
    - sympathy
    - pity
    status: proposed
- id: poshchada
  ru: пощада
  sense: 'пощада как закон и свойство высшей любви: «закон пощады», «закон мировой пощады», «закон Великой Пощады», «пощада
    Учителя»; в быту — «пощады не будет», «молить о пощаде»'
  distinguish: 'miloserdie — милосердие: «Пощада есть закон милосердия» p3-c32-028, «милосердия и пощады» p3-c31-135, p2-c18-112;
    zhalost — жалость, «жалостливость»: «жалостливость и пощада ничего общего между собой не имеют» p3-c32-028; sostradanie
    — «в ней выражается не сострадание» (там же).'
  tier: core
  first_seen: p1-c24-010
  counts:
    p1: 4
    p2: 12
    p3: 14
  note: 'критерий (правило 1): в поучениях («закон пощады», «пощада и милосердие») — clemency; в бытовых идиомах («пощады
    вам не будет» p2-c03-054, «молить его о пощаде» p3-c15-138) английское устойчиво mercy (no mercy, beg for mercy) — это
    идиома, а не понятие учения'
  evidence:
  - id: p3-c32-028
    ru: жалостливость и пощада ничего общего между собой не имеют. Пощада есть закон милосердия.
    en_legacy: regret and mercy don’t have anything in common. Mercy – that’s the law of regret.
  - id: p1-c24-150
    ru: силу мирового закона пощады
    en_legacy: the power of the universal law of compassion
  - id: p3-c32-157
    ru: закон Великой Пощады
    en_legacy: the Great law of Mercy
  - id: p3-c09-007
    ru: Милосердие бесконечно, пощада не знает предела и отказа
    en_legacy: compassion is endless and it never pushes him away
    note: два понятия слиты в одно
  en:
    term: clemency
    legacy: compassion ≈15, mercy ≈15, pity ≈8, прочее (sparing, forgiveness) 4 — в связях с «пощадой» (28)
    avoid:
    - compassion (для «пощады»)
    - regret
    status: proposed
  question: 'clemency / forbearance / sparing / mercy? Доводы: mercy уже предложено для «милосердия» (miloserdie), а RU ставит
    их рядом как разные («Пощада есть закон милосердия» p3-c32-028); compassion занято «состраданием». clemency — «пощада,
    отказ от кары» — точнее всего; forbearance ближе к «терпению, снисхождению»; sparing — только глагольное. Парадокс «закон
    мировой пощады требовал полного уничтожения гада» (p2-c14-089) с clemency сохраняется. Рекомендация: clemency; если владелец
    оставит compassion для «милосердия», пощада → mercy.'
- id: zhalost
  ru: жалость
  sense: жалость — человеческое чувство; в поучениях «жалостливость» противопоставлена пощаде как «предрассудок… сентиментальность»
    (p3-c32-028)
  distinguish: 'poshchada — пощада (p3-c32-028); sostradanie — сострадание, стоит рядом: «жалостью и состраданием» p3-c06-068,
    «жалость, сострадание» p3-c05-062, перечень «милосердия, доброты, любви, жалости, сострадания» p3-c17-158. «Какая жалость»
    (p2-c01-055) — идиома: what a pity.'
  tier: core
  first_seen: p1-c14-035
  counts:
    p1: 2
    p2: 4
    p3: 9
  note: «жалостливость» (p3-c32-028) — pity тоже (a pitying heart, sentimental pity по контексту), главное — не слить с пощадой
  evidence:
  - id: p3-c32-028
    ru: у тебя еще щемит сердце от жалости иногда
    en_legacy: your heart still aches with regret
  - id: p3-c06-068
    ru: Он залил их жалостью и состраданием
    en_legacy: He was pouring his compassion and sympathy into them
    note: 'жалость → compassion, сострадание → sympathy: оба сдвинуты'
  - id: p1-c17-099
    ru: всё же жалость к ней
    en_legacy: anyway I was feeling a pity for her
  en:
    term: pity
    legacy: compassion ≈10, pity ≈5, sympathy ≈4, regret 3 — в связях с «жалостью» (15)
    avoid:
    - compassion (для «жалости»)
    - regret
    status: proposed
- id: dobro#good
  ru: добро
  sense: добро как нравственное начало («добро и зло», «воля к добру», «платить добром»)
  distinguish: 'не путать с «доброта» (kindness, 387 раз), с кратким прилагательным «добра», «добром лице» (kind) и с «добро»
    = имущество, пожитки — другое значение, goods / belongings: «своего аккуратно сложенного добра» p3-c03-099, «немудрящее
    добро в мешок» p3-c14-122, «ворованного добра» p2-c20-073, «своего добра» p3-c06-051, «чужое добро» p3-c15-124.'
  tier: core
  first_seen: p1-c22-013
  counts:
    p1: 2
    p2: 9
    p3: 29
  evidence:
  - id: p3-c02-218
    ru: жертву борьбы страстей, борьбы добра и зла
    en_legacy: the victim of good and evil
  - id: p2-c15-176
    ru: ему пришлось встретиться с добром, превосходящим его силы
    en_legacy: he encountered the power of kindness that surpassed him
  - id: p3-c01-074
    ru: сжигая в человеке волю к добру
    en_legacy: they burn down the will for kindness within man
  en:
    term: good
    legacy: kindness ≈22 (смешение с «добротой»); good ≈17
    avoid:
    - kindness (для «добра»)
    status: proposed
- id: zlo
  ru: зло
  sense: зло как начало и как причинённый вред
  tier: core
  first_seen: p1-c09-044
  counts:
    p1: 31
    p2: 91
    p3: 73
  evidence:
  - id: p3-c06-018
    ru: нет ни зла, ни добра — есть временное закрепощение
    en_legacy: neither evil nor good exist – that there’s only a temporary slavery
  en:
    term: evil
    legacy: evil ≈148; anger ≈10; harm 5
    avoid: []
    status: proposed
- id: volya#will
  ru: воля
  sense: воля как сила души («упорство воли», «сила чистой любви и воли», «воля к добру/труду/победе»), воля другого лица
    («воля отца»)
  distinguish: 'volya#freedom — свобода, «на волю» (3 раза: p2-c12-103 «вырвавшийся на волю школьник», p3-c15-104 «хотим к
    себе, на волю»). Пара «любовь и воля» во всех прозаических местах — сила, а не свобода: «сила чистой любви и воли помогла
    мне защитить её» p1-c18-144; «приказ отца — закон для их собственной любви и воли» p3-c12-042.'
  tier: core
  first_seen: p1-c01-061
  counts:
    p1: 44
    p2: 78
    p3: 81
  evidence:
  - id: p1-c18-144
    ru: великая сила чистой любви и воли помогла мне защитить её
    en_legacy: great power of pure love and will has helped me to protect her
  - id: p1-c20-213
    ru: Пою я песнь любви и воли.
    en_legacy: From my love, will and power.
  en:
    term: will
    legacy: will ≈170; power ≈18; freedom 3
    avoid: []
    status: proposed
  question: 'В песне Ананды (p1-c20-213, повтор p2-c18-047/048) «песнь любви и воли» — will или freedom? В прозе вопроса нет:
    пара «любовь и воля» трижды = сила (p1-c18-144, p3-c12-042; «воля к добру»), «воля» → will. В песне по DEC-026 готовятся
    оба варианта (рифмованный и нерифмованный), и выбор слова делается при переводе песни: поэтическое «воля» = свобода возможно,
    но текст этого не подтверждает. Рекомендация: will; freedom — только если его потребует рифмованный вариант песни (verse-terms#cal-5).'
- id: volya#freedom
  ru: воля (на волю)
  sense: свобода, вольная жизнь
  distinguish: см. volya#will
  tier: core
  first_seen: p2-c12-103
  counts:
    p1: 0
    p2: 1
    p3: 2
  evidence:
  - id: p3-c15-104
    ru: хотим к себе, на волю, к нашим совам и змеям
    en_legacy: (freedom)
  en:
    term: freedom
    legacy: freedom
    avoid: []
    status: proposed
- id: volya-k-dobru
  ru: воля к добру
  sense: стремление, воля человека творить добро — то, что тёмные оккультисты «сжигают» гипнозом
  distinguish: 'часть ряда «воля к + существительное»: «воля к труду» p3-c20-082, «воля к победе» p3-c32-108; переводить единообразно.
    «Добро» здесь = dobro#good, а не «доброта».'
  tier: core
  first_seen: p3-c01-074
  counts:
    p1: 0
    p2: 0
    p3: 1
  evidence:
  - id: p3-c01-074
    ru: сжигая в человеке волю к добру своим тяжелым гипнозом
    en_legacy: they burn down the will for kindness within man with their hypnosis
  - id: p3-c20-082
    ru: в ком жива гибкая воля к труду
    en_legacy: within whom the flexible will for work is living
  en:
    term: will to good
    legacy: 'will for kindness (1): ошибка — kindness = «доброта», и предлог for; ряд: will for work'
    avoid:
    - will for kindness
    - will for good
    status: proposed
  question: 'will to good или will to do good? Доводы: RU-ряд «воля к добру / к труду / к победе» — существительные; will
    to good / will to work / will to victory сохраняет ряд. Рекомендация: will to good.'
- id: ya#self
  ru: Я («твоё Я», «личное «Я»», «высшее «Я»»)
  sense: '«Я» как существительное — личность человека: и эгоистическое («личное «Я»», «эгоистическое «Я»», «яд собственного
    «Я»»), и высшее («высшее духовное «Я»» p3-c19-101, «твое Я, освобожденное от страстей» p3-c01-077, «его Я есть Бог» p3-c12-170).
    Кавычки в RU не различают смысл.'
  distinguish: 'RU строит на этом игру местоимений: «где начиналось «Я» и где было «не Я»» p3-c05-027; «Не «Я» становится
    его бытом, но через меня» p3-c08-026; «нет «Я» и «меня», но… «через» меня» p3-c11-143 — перевод должен её сохранить. Не
    путать с «я»-местоимением и с «эгоизм/эгоистический» (отдельные слова RU).'
  tier: core
  first_seen: p2-c18-024
  counts:
    p1: 0
    p2: 3
    p3: 21
  evidence:
  - id: p3-c01-077
    ru: Осознай, что твое Я, освобожденное от страстей, может сдвигать горы
    en_legacy: Perceive that your I which is free from passions is able to move heaven and earth
  - id: p3-c12-170
    ru: что его Я есть Бог, неумирающий и вездесущий
    en_legacy: that his Self is God which cannot die
  - id: p3-c08-026
    ru: Не «Я» становится его бытом, но через меня.
    en_legacy: Not “I” becomes his mode of life, but “through me”.
  - id: p3-c19-101
    ru: его высшее духовное «Я»
    en_legacy: his highest spiritual “I”
  en:
    term: '“I” (в кавычках: the personal “I”, the higher “I”)'
    legacy: “I” ≈16; I без кавычек 2 (p3-c01-077); Self 1 (p3-c12-170); self (в других словах) ≈3
    avoid:
    - ego
    status: proposed
  question: 'self / Self / “I”? Варианты: (а) “I” в кавычках везде — сохраняет игру «Я / не Я / через меня» (p3-c05-027, p3-c08-026,
    p3-c11-143), так делал старый EN; (б) self/Self — естественнее в «твоё Я может сдвигать горы», но ломает игру местоимений;
    (в) смешанно: Self для высшего, “I” для личного — RU такого различия буквой не делает (высшее «Я» тоже в кавычках). Рекомендация:
    (а) “I” с кавычками во всех местах, включая p3-c01-077 и p3-c12-170 («his “I” is God»); ego не использовать.'
- id: sovershenstvovanie
  ru: совершенствование
  sense: путь (труд) совершенствования — непрерывное движение к совершенству («путь вечного совершенствования»)
  distinguish: 'sovershenstvo — совершенство (цель, состояние); «развитие» — отдельное RU-слово (development), они стоят рядом:
    «к совершенству и развитию» p3-c05-105'
  tier: core
  first_seen: p1-c04-011
  counts:
    p1: 6
    p2: 5
    p3: 25
  evidence:
  - id: p3-c01-067
    ru: все твои братья и сестры, идущие путем труда и совершенствования
    en_legacy: who are walking the path of their development and work
  - id: p1-c23-171
    ru: на пути вечного совершенствования человека
    en_legacy: along the path of man’s eternal improvement
  - id: p1-c21-089
    ru: что предела в совершенствовании нет
    en_legacy: there are no limits for perfection
  en:
    term: self-perfection
    legacy: development ≈25 (почти всё в ч. III); improvement ≈8 (ч. I–II); perfection 2; self-perfection 0
    avoid:
    - development
    - improvement
    status: proposed
  question: 'self-perfection / perfecting / self-improvement / perfection? Доводы: RU отличает «совершенствование» и от «развития»
    (development), и от «совершенства» (perfection); self-improvement звучит бытово. В тексте речь не всегда о себе: «совершенствование
    народа» (p3-c08-038 — «двигавшие его в целом к совершенствованию»). Рекомендация: self-perfection там, где речь о человеке
    и его пути («путь совершенствования» → the path of self-perfection); perfecting для народа/человечества — оставить на
    правку по контексту, но не development.'
- id: sovershenstvo
  ru: совершенство
  sense: совершенство как цель и степень («ступени совершенства», «радость совершенства»)
  distinguish: sovershenstvovanie — процесс; «совершенный» (прилагательное, 397 раз, чаще бытовое «совершенно») — не термин
  tier: core
  first_seen: p1-c14-061
  counts:
    p1: 6
    p2: 16
    p3: 54
  evidence:
  - id: p3-c01-071
    ru: стремящихся к радости совершенства людей
    en_legacy: who are striving for joy of knowledge
  - id: p3-c07-037
    ru: Нет на земле пути к совершенству без труда
    en_legacy: No such path to man’s development without activity exists on the Earth
  - id: p3-c09-074
    ru: превосходя знаниями и внутренним совершенством многих
    en_legacy: surpassing many others with his knowledge and inner perfection
  en:
    term: perfection
    legacy: 'perfection ≈35; development ≈28 (все в ч. III: системный сдвиг «совершенство» → development); knowledge 2 (p3-c01-071,
      p2-c19-050)'
    avoid:
    - development
    - knowledge
    status: proposed
- id: samoobladanie
  ru: самообладание
  sense: владение собой — одно из главных требований к ученику
  tier: core
  first_seen: p1-c02-071
  counts:
    p1: 39
    p2: 57
    p3: 156
  evidence:
  - id: p3-c06-069
    ru: в непоколебимом самообладании и верности
    en_legacy: has to keep an unshakable self-control and loyalty
  en:
    term: self-control
    legacy: self-control ≈219 (последовательно); calm ≈14
    avoid:
    - calm
    status: proposed
  question: 'self-control (старый EN, последовательно) или self-possession (ближе к «обладанию собой», без оттенка подавления)?
    Ошибки нет — рекомендация: self-control.'
- id: bodrost
  ru: бодрость
  sense: деятельная живость, прилив сил и духа, которую «несут», «подают» встречному; стоит в паре с «энергией» («пожатие
    бодрости и энергии» p1-c06-019) и отдельно от «радости» и «жизнерадостности»
  distinguish: 'RU различает: «радость и бодрость» p3-c01-161, «бодрость и радостность» p3-c20-115, «Бодрость ее, мужество
    и жизнерадостность» p3-c11-169 — значит, бодрость ≠ радость/жизнерадостность (cheerfulness). В p3-c31-018 текст отделяет
    ложную бодрость («показное, мнимо энергичное состояние») от истинной: «истинная бодрость есть благословение в себе и ближнем
    Божественной Энергии и гармоничный труд в Ней при забвении «я»» — связь с Энергией и трудом, а не с весельем. «бодрящий»
    (о конфетах Али, p1-c06-019) — invigorating.'
  tier: core
  first_seen: p1-c01-002
  counts:
    p1: 10
    p2: 3
    p3: 28
  note: 'критерий (правило 1): существительное — vigour («my inner vigour», «vigour and energy»); прилагательное и наречие
    — по контексту, не механически vigorous(ly): бодрый старик — hale / sprightly; бодрым голосом, бодро ответил — briskly,
    in a brisk voice; бодрое пожатие — a firm, vigorous handshake; «подать бодрость» — hearten, put heart into (give vigour
    не использовать); cheerily — только в бытовой речи'
  evidence:
  - id: p1-c06-019
    ru: Прими моё пожатие бодрости и энергии…
    en_legacy: Accept my handshake full of cheerfulness and energy…
  - id: p3-c01-078
    ru: Прими, друг, бодрое пожатие моей руки
    en_legacy: My friend, accept my energetic handshake
  - id: p3-c31-018
    ru: Есть бодрость — показное, мнимо энергичное состояние
    en_legacy: An artificial, demonstrative cheerfulness exists, an imaginary energetic state
  en:
    term: vigour
    legacy: cheerfulness/cheerful ≈47 (сущ. + прил.); energy/energetic 6; spirit 2
    avoid:
    - cheerfulness
    - give vigour
    status: proposed
  question: 'cheerfulness (старый EN) / vigour / good heart / buoyancy? Доводы из текста: бодрость стоит рядом с радостью
    и жизнерадостностью как отдельное качество (p3-c01-161, p3-c20-115, p3-c11-169), а истинная бодрость определена через
    Божественную Энергию и гармоничный труд (p3-c31-018) — cheerfulness сливает её с радостью. Рекомендация: vigour для существительного,
    формы — по критерию в note; нужна проверка носителем языка.'
- id: besstrashie
  ru: бесстрашие
  sense: бесстрашие — одно из четырёх «блаженств» (Любовь, Мир, Радость, Бесстрашие) и постоянное требование к ученику
  tier: core
  first_seen: p1-c02-108
  counts:
    p1: 14
    p2: 25
    p3: 80
  evidence:
  - id: p3-c01-071
    ru: Живи легко, бесстрашно и свободно.
    en_legacy: Live freely, easily and without any fear.
  en:
    term: fearlessness
    legacy: fearless(ness) ≈84; without fear ≈13; courage ≈9
    avoid:
    - courage
    status: proposed
- id: garmoniya
  ru: гармония
  sense: гармония (в себе, со вселенной); с прописной — начало («слит с Гармонией» p3-c10-072)
  tier: core
  first_seen: p1-c01-061
  counts:
    p1: 24
    p2: 35
    p3: 195
  evidence:
  - id: p3-c17-042
    ru: 'о неизбежной ступени в пути совершенствования каждого человека: о гармонии'
    en_legacy: 'an inevitable stage of development of every man’s path: harmony'
  en:
    term: harmony
    legacy: harmony ≈274 (последовательно)
    avoid: []
    status: proposed
- id: dukh#spirit
  ru: дух
  sense: дух человека («силы творческого духа», «очи духа»); «Дух» с прописной — 19 (все в ч. III, середина фразы)
  distinguish: 'dusha#soul — душа; dukh#beings — «духи» (существа: «духи Света», «духи стихии огня»). «Дух» = мужество — идиомы
    («падать духом» p1-c13-094, p3-c22-119; «не смущайся духом» p3-c15-078; ≈8): не spirit, а courage / heart по контексту
    (lose heart, take heart); старый EN — falling into a gloom, despair. «духи» = парфюм (p1-c11-048, p1-c25-107) — другое
    слово, perfume. «духовный» — spiritual.'
  tier: core
  first_seen: p1-c02-039
  counts:
    p1: 45
    p2: 98
    p3: 343
  evidence:
  - id: p3-c01-069
    ru: развернуло в тебе все силы творческого духа
    en_legacy: all your creative powers of spirit would open within yourself
  en:
    term: spirit
    legacy: spirit ≈441; mind ≈14; soul 8; courage 8
    avoid:
    - soul
    status: proposed
- id: dukh#beings
  ru: духи
  sense: 'духи — существа в видениях ч. III: «духи Света», «светлые духи», «братья-духи», «духи стихии огня», «духи-труженики»;
    почти всегда во мн. ч.'
  distinguish: dukh#spirit — дух человека (ед. ч.); «духи» = парфюм («аромат духов и сигар» p1-c11-048, «приторными духами»
    p1-c25-107) — perfume.
  tier: core
  first_seen: p3-c09-179
  counts:
    p1: 0
    p2: 0
    p3: 39
  evidence:
  - id: p3-c26-037
    ru: в них духи Света вносили будущие эмбрионы людей
    en_legacy: the spirits of Light were carrying the future people embryos
  - id: p3-c29-013
    ru: То духи стихии огня, труженики
    en_legacy: That’s the spirits of the fire element, her workers
  - id: p3-c26-081
    ru: встречают светлые братья-духи
    en_legacy: his brothers – the spirits of light meet him
  en:
    term: spirits
    legacy: spirits — 30 из 36 связей (последовательно); beings 2, angels 2
    avoid: []
    status: proposed
- id: dusha#soul
  ru: душа
  sense: душа
  distinguish: dukh#spirit — дух; «от души», «по душе» — идиомы
  tier: core
  first_seen: p1-c06-004
  counts:
    p1: 62
    p2: 84
    p3: 103
  evidence:
  - id: p1-c13-114
    ru: Из всех чувств, из всех впечатлений в душе господствовали два
    en_legacy: two of them were prevailing in my soul
  en:
    term: soul
    legacy: soul ≈150; heart ≈32; spirit ≈17
    avoid:
    - spirit
    status: proposed
- id: soznanie
  ru: сознание
  sense: сознание (раскрытие сознания, «высшее сознание»)
  tier: core
  first_seen: p1-c02-044
  counts:
    p1: 37
    p2: 51
    p3: 177
  evidence:
  - id: p3-c01-066
    ru: чье сознание раскрыло человеку его живую Вечность
    en_legacy: whose consciousness has comprehended the living Eternity (глагол «раскрыло» передан как comprehended)
  en:
    term: consciousness
    legacy: consciousness ≈101; (be) conscious/consciously ≈105 — в т. ч. для «сознавать»
    avoid:
    - mind
    status: proposed
- id: vernost
  ru: верность
  sense: верность ученика Учителю и делу — «единственный ключ ко всему знанию» (p3-c01-070); также супружеская верность
  distinguish: preданность — predannost (devotion); не сливать
  tier: core
  first_seen: p1-c02-041
  counts:
    p1: 46
    p2: 77
    p3: 207
  evidence:
  - id: p3-c01-070
    ru: Нужна твоя верность.
    en_legacy: Your loyalty is needed.
  en:
    term: loyalty
    legacy: loyalty/loyal ≈275; faithful(ness) ≈13
    avoid:
    - devotion
    status: proposed
  question: 'loyalty (старый EN, последовательно) или faithfulness (ближе к «верность» в духовном и супружеском смысле)? Рекомендация:
    loyalty как основной термин; faithfulness допустимо только в супружеском контексте — решить владельцу, т. к. это нарушает
    «один смысл — один перевод».'
- id: predannost
  ru: преданность
  sense: преданность (человеку, делу)
  distinguish: 'vernost — верность; в RU стоят рядом: «твою верность и преданность брату-отцу» p1-c02-107'
  tier: core
  first_seen: p1-c02-014
  counts:
    p1: 14
    p2: 16
    p3: 48
  evidence:
  - id: p1-c02-107
    ru: выказать на деле твою верность и преданность брату-отцу
    en_legacy: prove with your actions your loyalty and devotion to your brother-father
  - id: p1-c05-004
    ru: настало моё время выказать мужество и преданность
    en_legacy: the time came to show my fortitude and loyalty
  en:
    term: devotion
    legacy: devotion ≈48; loyalty ≈21 (смешение с «верностью»)
    avoid:
    - loyalty
    status: proposed
- id: trud
  ru: труд
  sense: труд — основа учения («путь труда и совершенствования», «труд любви и радости», «трудящееся небо»)
  distinguish: «работа» (202) — work/job; «деятельность» (72) — activity; «труженики неба» — в ЗАМЕТКАХ
  tier: core
  first_seen: p1-c01-035
  counts:
    p1: 102
    p2: 148
    p3: 774
  note: торжественное labour — вопрос стайлгайда (этап 4); до решения — work
  evidence:
  - id: p1-c07-098
    ru: как труд любви и радости
    en_legacy: as an activity of love and joy
  - id: p3-c01-067
    ru: идущие путем труда и совершенствования
    en_legacy: walking the path of their development and work
  en:
    term: work
    legacy: work ≈581; activity ≈240 (ч. III ≈196) — смешение с «деятельностью»; effort 14; labour 6
    avoid:
    - activity
    status: proposed
- id: obshchee-blago
  ru: общее благо
  sense: благо всех людей, ради которого живёт и трудится ученик
  tier: core
  first_seen: p1-c04-011
  counts:
    p1: 5
    p2: 12
    p3: 28
  evidence:
  - id: p3-c01-075
    ru: кто хочет жить для общего блага
    en_legacy: who want to live for the common welfare
  - id: p3-c02-219
    ru: а не для труда на общее благо
    en_legacy: not for the work for everybody’s general welfare
  - id: p1-c15-175
    ru: деятельность любви и мира на общее благо
    en_legacy: activity of love and calm for the people’s welfare
  en:
    term: the common good
    legacy: welfare (common/general/people’s) ≈24; well-being ≈10; the common good — 0
    avoid:
    - common welfare
    - general welfare
    - wellbeing
    status: proposed
- id: podvig
  ru: подвиг
  sense: 'подвиг — героическое усилие или самоотверженное служение: «подвиг любви и милосердия», «подвиг труда», «великий
    подвиг», «жить в подвиге»'
  distinguish: 'RU часто противопоставляет подвиг простому труду и радости — это противопоставление надо сохранить: «Дежурства
    не подвига, а простого счастья» p3-c06-018; «не как долг или подвиг, а как самое простое сотрудничество» p3-c08-020; «Подвигами
    как таковыми не движутся вперед наши ученики» p3-c10-005; «не подвиг тяжкий несу я» p3-c12-088. «подвижник» (1) — отдельное
    слово.'
  tier: core
  first_seen: p1-c11-020
  counts:
    p1: 8
    p2: 5
    p3: 58
  note: 'критерий (правило 1): feat — «подвиг любви/милосердия/труда» (the feat of love), «великий подвиг»; с глаголами «нести
    подвиг», «жить в подвиге» — описательно (carry the heroic labour of…, live heroically); «героического подвига» (p3-c15-090)
    — heroic feat'
  evidence:
  - id: p1-c25-039
    ru: очищенный его подвигом любви и милосердия
    en_legacy: purified by the feat of his love and compassion
  - id: p3-c26-117
    ru: подвигом милосердия и самоотвержения
    en_legacy: the feat of incomprehensible compassion and self-sacrifice
  - id: p3-c18-100
    ru: Он взял на себя великий подвиг любви
    en_legacy: He took a great deed of love upon himself
  - id: p3-c08-020
    ru: не как долг или подвиг, а как самое простое сотрудничество
    en_legacy: which isn’t as a duty or a deed for him, but as the most ordinary communication with his Teacher
  en:
    term: feat
    legacy: 'deed ≈34, heroic/heroism ≈30, feat ≈11, (self-)sacrifice ≈7 — в связях с «подвигом» (54; в связи бывает несколько):
      разнобой'
    avoid: []
    status: proposed
  question: 'feat / heroic deed / deed / heroism? Доводы: deed теряет «героическое» (подвиг ≠ «дело»), heroism — свойство,
    а не поступок; heroic deed точно, но тяжело в сочетаниях («heroic deed of love and mercy»); feat — прямое соответствие
    («подвиг, требующий мужества») и легко сочетается («the feat of love»). Рекомендация: feat, формы по критерию в note.'
- id: sotrudnik
  ru: сотрудник
  sense: 'тот, кто трудится вместе с Учителем, Братством, Жизнью: «круг моих сотрудников» (Али), «сотрудник живого неба»,
    «сотрудники Великой Матери», «Владыка этого луча… своих сотрудников»'
  distinguish: 'sotrudnichestvo — сотрудничество; «помощник» — другое слово, стоит рядом: «друга и помощника, и сотрудника
    тоже» p1-c16-105. Служебное «сотрудник» (юрист у адвоката, «вашему сотруднику и племяннику» p2-c08-017) — colleague по
    контексту.'
  tier: core
  first_seen: p1-c16-105
  counts:
    p1: 1
    p2: 3
    p3: 60
  evidence:
  - id: p3-c01-053
    ru: я приму тебя в круг моих сотрудников
    en_legacy: I will accept you to the circle of my co-workers
  - id: p3-c05-009
    ru: Вы сотрудник живого неба
    en_legacy: you are worker of the living heaven
  - id: p1-c16-105
    ru: в Али молодом обретёшь друга и помощника, и сотрудника тоже
    en_legacy: young Ali will be your friend and assistant
    note: «сотрудник» опущен
  - id: p3-c32-008
    ru: признание вас сотрудниками
    en_legacy: your recognition as Life’s coworkers
  en:
    term: co-worker
    legacy: 'colleague ≈21, assistant ≈16, associate ≈13, worker/helper ≈15, co-worker/coworker ≈5 — в связях с «сотрудником»
      (54): разнобой'
    avoid:
    - assistant (для «сотрудника»)
    status: proposed
  question: 'co-worker / fellow worker / collaborator / colleague? Доводы: assistant сливает «сотрудника» с «помощником» (p1-c16-105);
    colleague и associate — служебные и деловые; collaborator двусмысленно (коллаборационист). Рекомендация: co-worker (так
    и в старом EN в p3-c01-053); colleague — только в служебном значении.'
- id: sotrudnichestvo
  ru: сотрудничество / сотрудничать
  sense: 'совместный труд человека с Учителем, Жизнью, Богом: «сотрудничество с Жизнью», «места моего с Ним сотрудничества»,
    «войти в сотрудничество с Учителем»'
  distinguish: sotrudnik — сотрудник (лицо)
  tier: core
  first_seen: p2-c04-075
  counts:
    p1: 0
    p2: 2
    p3: 38
  note: старый EN в основном последователен (cooperation); написание без дефиса — как у большинства старого EN (§9.2 п.6)
  evidence:
  - id: p3-c32-006
    ru: Ваше сотрудничество с Жизнью состоит в помощи строительства
    en_legacy: Your cooperation with Life – that’s to take part in His construction
  - id: p3-c29-073
    ru: места моего с Ним сотрудничества для блага людей земли
    en_legacy: His and my cooperation is taking place for the prosperity of the people of the Earth
  - id: p3-c08-020
    ru: как самое простое сотрудничество
    en_legacy: as the most ordinary communication with his Teacher
    note: 'ошибка: communication'
  - id: p3-c07-038
    ru: И ты привлек к сотрудничеству
    en_legacy: you drew closer … to yourself to collaborate with you
  en:
    term: cooperation
    legacy: cooperation/cooperate ≈25 (написание cooperat- 28 во всём тексте, co-operat- 7); assist/help ≈18; collaborate
      2
    avoid:
    - communication
    status: proposed
- id: put#path
  ru: путь
  sense: путь человека, ученика («путь труда», «путь Света», «путь освобождения», «путь любви»)
  distinguish: буквальная дорога, поездка — way/journey/road по контексту (≈230)
  tier: core
  first_seen: p1-c02-132
  counts:
    p1: 122
    p2: 196
    p3: 812
  evidence:
  - id: p3-c01-071
    ru: ключ к такому пути
    en_legacy: the key to such path
  en:
    term: path
    legacy: path ≈772; way ≈222; journey ≈24
    avoid: []
    status: proposed
- id: stupen
  ru: ступень
  sense: ступень пути, совершенства, знания («новая ступень», «ступени Милосердия», «первая ступень»)
  distinguish: буквальная ступенька (лестница, вагон) — step
  tier: core
  first_seen: p1-c14-081
  counts:
    p1: 12
    p2: 25
    p3: 200
  note: 'критерий (правило 1): stage — ступень пути, совершенства, знания; step / rung — там, где образ лестницы явный («начиная
    с самых низших ступеней» p1-c22-179 — from the lowest rungs); level не запрещён в идиомах, где он естественен («возводит
    человека на новую ступень внутренней силы» p1-c14-081 — a new level of inner strength); буквальная ступенька — step'
  evidence:
  - id: p1-c14-081
    ru: возводит человека на новую ступень внутренней силы
    en_legacy: leading him upstairs onto the new level of strength
  - id: p1-c22-179
    ru: начиная с самых низших ступеней
    en_legacy: by starting from the lowest stages
  en:
    term: stage
    legacy: level ≈96; stage ≈62; step ≈48 (часть — буквальные ступеньки); degree 1 — непоследовательно
    avoid: []
    status: proposed
  question: 'stage / step / level? Старый EN непоследователен (level ≈96, stage ≈62, step ≈48). Рекомендация: stage как рабочий
    вариант, step/rung — по образу лестницы, level — только в идиомах (критерий в note); решить владельцу с носителем.'
- id: osvobozhdenie
  ru: освобождение (освобожденность, раскрепощение)
  sense: освобождение от страстей, условностей, личного — цель пути («путь освобождения»)
  distinguish: «свобода» (66) — freedom; «раскрепощённость/раскрепощение» (72) — старый EN тоже liberation/freedom
  tier: core
  first_seen: p1-c14-079
  counts:
    p1: 29
    p2: 49
    p3: 267
  evidence:
  - id: p3-c01-077
    ru: В полной освобожденности от бытовых тягот
    en_legacy: While being completely liberated from your private burden
  en:
    term: liberation
    legacy: liberation ≈206; free/freedom ≈100
    avoid: []
    status: proposed
- id: karma
  ru: карма
  sense: карма; «кармические пути», «кольцо кармы»; мн. ч. «карм» (владыки карм)
  tier: core
  first_seen: p1-c22-012
  counts:
    p1: 1
    p2: 15
    p3: 95
  evidence:
  - id: p3-c06-022
    ru: кольцо кармы, которое… передвигали владыки освобождающих карм
    en_legacy: the wheel of karma which the lords…
  en:
    term: karma
    legacy: karma ≈96 (мн. ч. karmas)
    avoid: []
    status: proposed
  question: 'Множественное «карм» (владыки карм, «прежних карм человека») — karmas (старый EN) или karma без мн. ч.? Рекомендация:
    karma, мн. ч. только где RU явно различает несколько карм.'
- id: temnye-sily
  ru: тёмные силы
  sense: силы зла; в паре со «светлыми силами»
  tier: core
  first_seen: p1-c22-122
  counts:
    p1: 3
    p2: 4
    p3: 22
  evidence:
  - id: p3-c18-054
    ru: Вы долго боролись с темными силами, которым когда-то послужили
    en_legacy: You were fighting against the dark powers for a long time to whom you served once
  - id: p3-c04-148
    ru: платя тебе только старый долг спасения жизни от темных сил
    en_legacy: by repaying you for saving my life from the dark powers
  en:
    term: dark powers
    legacy: the dark powers — последовательно во всех проверенных (≈9 по окну + p3-c04-148, p3-c17-085, p3-c17-118, p3-c21-058,
      p3-c25-085); black 2
    avoid:
    - black powers
    status: proposed
  question: 'dark powers (старый EN, последовательно; согласуется с sila#power → Power) или dark forces (идиоматичнее)? Ошибки
    нет — рекомендация: dark powers.'
- id: temnye-okkultisty
  ru: тёмные оккультисты
  sense: люди, приобретающие «особые знания» ради власти и порабощения людей; «тёмный оккультизм», «дугпа»
  tier: core
  first_seen: p3-c01-073
  counts:
    p1: 0
    p2: 0
    p3: 15
  evidence:
  - id: p3-c01-073
    ru: Этими делами занимаются темные оккультисты.
    en_legacy: The black occultists are engaged in these affairs.
  - id: p3-c17-082
    ru: что перед вами темный оккультист?
    en_legacy: that the dark occultist is before you?
  en:
    term: dark occultists
    legacy: dark occultist(s)/occultism ≈26 по корпусу; black occultists 4 (p3-c01-073, 074, p3-c02-219 ×2)
    avoid:
    - black occultists
    status: proposed
- id: znanie
  ru: знание
  sense: знание («двигатель жизни», «ключ ко всему знанию»)
  tier: core
  first_seen: p1-c05-004
  counts:
    p1: 50
    p2: 53
    p3: 253
  evidence:
  - id: p3-c01-076
    ru: Знание — двигатель жизни
    en_legacy: Knowledge – that’s the engine of life
  en:
    term: knowledge
    legacy: knowledge ≈290 (последовательно)
    avoid: []
    status: proposed
- id: blagoslovenie
  ru: благословение
  sense: благословение (Учителя, Братства); «благословлять день», «Будь благословен» — formula#bud-blagosloven
  tier: core
  first_seen: p1-c17-010
  counts:
    p1: 3
    p2: 7
    p3: 48
  evidence:
  - id: p3-c28-040
    ru: Прими мое благословение, друг и брат.
    en_legacy: Accept my blessing, my friend and brother.
  en:
    term: blessing
    legacy: blessing ≈32; bless ≈9
    avoid: []
    status: proposed
- id: edinenie
  ru: единение
  sense: единение (с людьми, с Учителем, с трудом) — «единение вечное с его трудом и путями» (о верности)
  tier: core
  first_seen: p1-c17-161
  counts:
    p1: 8
    p2: 15
    p3: 63
  evidence:
  - id: p3-c01-070
    ru: Это единение вечное с его трудом и путями.
    en_legacy: That is his eternal unity with his work and his paths.
  en:
    term: union
    legacy: unite ≈40; unity ≈19; union ≈7
    avoid: []
    status: proposed
  question: 'union (действие, связь) или unity (состояние)? В RU «единение» — действие/связь, «единство» — отдельное слово.
    Рекомендация: union.'
- id: tvorchestvo
  ru: творчество
  sense: творчество (творческий труд, творческие силы духа); «творчество Учителей», «творчество в искусстве»
  tier: core
  first_seen: p1-c08-036
  counts:
    p1: 18
    p2: 43
    p3: 106
  note: для свойства — creative power(s), the creative spirit; creativity (известно с 1870-х, но широко — с середины XX в.)
    имеет психологический и деловой оттенок и в речи рассказчика и Учителей звучит современно; устойчивая пара «труд и творчество»
    (3 места) — labour and creative work (не «work and creative work», так как «труд» здесь — labour, см. trud) («the stormy
    flame of your Teachers’ creative work», p3-c01-070)
  evidence:
  - id: p3-c01-070
    ru: ты сольешься с бурным пламенем творчества твоих Учителей
    en_legacy: you will unite with the intensive flame of your Teachers’ creation
  en:
    term: creative work
    legacy: creation ≈99; art ≈35; work ≈15
    avoid:
    - creativity
    - creation (для «творчества»)
    status: proposed
- id: samootverzhennost
  ru: самоотверженность (самоотвержение)
  sense: самоотверженность, забвение себя ради других
  distinguish: «самопожертвование» (7) — self-sacrifice; «самоотвержение» (46) — то же гнездо
  tier: core
  first_seen: p1-c03-110
  counts:
    p1: 13
    p2: 26
    p3: 70
  evidence:
  - id: p1-c08-033
    ru: откуда у этих людей столько самоотверженности и самообладания?
    en_legacy: from where these people had so much selflessness and self-control?
  en:
    term: selflessness
    legacy: selfless(ness) ≈86; self-sacrifice ≈40 (в т. ч. для «самоотвержения»)
    avoid:
    - self-sacrifice (для «самоотверженности»)
    status: proposed
- id: luch#ray
  ru: луч (семь лучей)
  sense: 'один из семи лучей, по которым идут люди и которыми руководят Великие Учителя: «Путь освобождения проходит по всем
    лучам, коих семь» p3-c04-121, «Учитель пятого луча» p3-c26-083, «башни лучей» p3-c29-024'
  distinguish: физический луч (солнца, света) — beam/ray по контексту
  tier: core
  first_seen: p3-c04-121
  counts:
    p1: 14
    p2: 15
    p3: 204
  evidence:
  - id: p3-c26-125
    ru: ты видел горящую башню седьмого луча
    en_legacy: you could see the burning tower of the seventh ray
  en:
    term: ray
    legacy: ray ≈155 (почти всё в ч. III); beam ≈58 (физический свет)
    avoid:
    - beam (для лучей учения)
    status: proposed
- id: uslovnost
  ru: условность
  sense: условности (быта, земли) — то, от чего освобождается ученик; «условное разъединение»
  tier: core
  first_seen: p1-c09-013
  counts:
    p1: 8
    p2: 11
    p3: 63
  evidence:
  - id: p1-c10-039
    ru: оторванный от земли и всех её условностей
    en_legacy: having broken away from the earth and all its conditionality
  - id: p1-c19-042
    ru: не слишком стеснять себя всякими условностями
    en_legacy: pay less attention to all kinds of conditionalities
  en:
    term: conventions
    legacy: conditionality/conditionalities ≈49 (калька); conditional 5
    avoid:
    - conditionality
    status: proposed
  question: 'conventions (рекомендация: так по-английски называют «условности» быта и общества) или сохранить conditionality
    для философского оттенка «обусловленности»? В бытовых местах (p1-c19-042) conditionality явно ошибочно.'
- id: predrassudok
  ru: предрассудок
  sense: предрассудок (воспитания, религии, неравенства, «жизни и смерти») — одно из препятствий на пути
  distinguish: «суеверие» (37) — отдельное слово RU, superstition; старый EN сливает оба в superstition
  tier: core
  first_seen: p1-c02-021
  counts:
    p1: 19
    p2: 34
    p3: 98
  evidence:
  - id: p1-c02-021
    ru: разделённых предрассудками воспитания, религии, обычаев
    en_legacy: broken by the national, family and religious superstitions
  - id: p2-c01-113
    ru: Смейся, дитя, над всеми предрассудками мира
    en_legacy: laugh at all the superstitions of the world
  - id: p3-c18-042
    ru: Если сердце человека свободно от предрассудка неравенства
    en_legacy: If the man’s heart is free from the superstition of inequality
  en:
    term: prejudice
    legacy: 'СИСТЕМАТИЧЕСКАЯ ОШИБКА: superstition ≈128 из 151; prejudice 6 (только ч. I)'
    avoid:
    - superstition (для «предрассудка»)
    status: proposed
- id: tselesoobraznost
  ru: целесообразность
  sense: целесообразность — один из двух законов движения вселенной («закономерность и целесообразность»), «закон целесообразности»
  distinguish: zakonomernost — закономерность; всегда в паре или рядом
  tier: core
  first_seen: p1-c04-003
  counts:
    p1: 4
    p2: 6
    p3: 26
  note: 'закон — the law of purposefulness; наречие — purposefully / to good purpose («act not only fearlessly but to good
    purpose», p1-c05-028); пара с zakonomernost — «conformity to law and purposefulness». expediency по-английски — «выгода,
    беспринципное удобство» (political expediency): «закон expediency» прочтётся как «закон выгоды»'
  evidence:
  - id: p3-c05-129
    ru: 'единственные законы движения вселенной: закономерность и целесообразность'
    en_legacy: 'the only laws of the movement of the universe: accuracy and regularity'
  - id: p3-c09-022
    ru: 'живет по мировому закону: Целесообразности'
    en_legacy: is living according to the universal law of Accuracy
  - id: p1-c05-028
    ru: действовать надо не только бесстрашно, но и целесообразно
    en_legacy: you have to act not only bravely, but also accurately
  en:
    term: purposefulness
    legacy: 'ОШИБКА: accuracy/accurately ≈21 из 36; expediency 4; purpose 6'
    avoid:
    - accuracy
    - expediency
    - expediently
    status: proposed
- id: zakonomernost
  ru: закономерность
  sense: закономерность — второй закон движения вселенной (в паре с целесообразностью)
  tier: core
  first_seen: p1-c04-003
  counts:
    p1: 3
    p2: 2
    p3: 20
  note: наречие — in accordance with law; lawfulness для общего читателя — «законность, правомерность» (юридическое), conformity
    to law однозначно отсылает к закономерности природы и вселенной
  evidence:
  - id: p3-c05-129
    ru: закономерность и целесообразность
    en_legacy: accuracy and regularity
  - id: p1-c04-003
    ru: гармония всегда закономерно и целесообразно действующих сил
    en_legacy: harmony of the powers… which is always working naturally and accurately
  en:
    term: conformity to law
    legacy: naturally ≈7; accuracy ≈6; regularity ≈5; law 3 — непоследовательно
    avoid:
    - accuracy
    - lawfulness
    status: proposed
- id: seryi-den
  ru: серый день
  sense: обычный, будничный день как поле труда ученика («в делах простого и серого дня», «путь к Учителю ведет через серый
    день»)
  tier: core
  first_seen: p1-c02-016
  counts:
    p1: 10
    p2: 3
    p3: 52
  note: 'образ сохраняем, но не одной формой: голое «the grey day» читается как погода; нужна опора — plain, ordinary, workaday:
    «in the affairs of the plain, grey day»; мн. ч. — grey, ordinary days; допустимо the grey everyday round'
  evidence:
  - id: p1-c06-019
    ru: героика чувств и мыслей живёт… в делах простого и серого дня
    en_legacy: simply it is your daily activity
  - id: p2-c18-112
    ru: Будем стараться жить среди серого дня
    en_legacy: Let’s try to walk… during our grey daily routine
  - id: p3-c04-128
    ru: к великому руководству в простом сером дне труда
    en_legacy: as the landmarks of your grey daily routine
  en:
    term: the plain grey day
    legacy: grey daily routine / daily routine ≈24; everyday ≈13; grey (другие сочетания) ≈15; образ часто теряется
    avoid: []
    status: proposed
- id: gonets
  ru: гонец
  sense: гонец (Радости, мира, Братства) — роль ученика, несущего людям помощь Учителей
  tier: core
  first_seen: p1-c23-029
  counts:
    p1: 1
    p2: 3
    p3: 68
  evidence:
  - id: p3-c13-184
    ru: идете по дню гонцом мира и Света людям
    en_legacy: walking every day as the messenger of Calm and Light for people
  en:
    term: messenger
    legacy: messenger ≈57; herald ≈8
    avoid:
    - herald
    status: proposed
- id: zakalyat#temper
  ru: закалять(ся) (о сердце, характере, духе)
  sense: закалять — делать крепким в испытаниях (сердца, характеры, волю)
  distinguish: 'физическое «закалять организм/здоровье» — harden (p1-c20-191, p1-c24-145) — допустимо. Для сердца и характера
    harden = «ожесточать»: смысл обратный.'
  tier: core
  first_seen: p1-c03-043
  counts:
    p1: 14
    p2: 10
    p3: 42
  evidence:
  - id: p3-c01-075
    ru: Здесь закаляются сердца тех, кто хочет жить для общего блага
    en_legacy: The hearts of those become hardened here
  - id: p3-c01-002
    ru: закалило не только мое здоровье, но и весь мой характер
    en_legacy: not only hardened my organism, but also changed my character
  - id: p3-c28-008
    ru: Тех, кого Истина посылает Своими гонцами, Она закаляет в единении с Нею.
    en_legacy: She hardens with unity with Herself
  en:
    term: temper
    legacy: harden ≈34; temper ≈22; strengthen 5
    avoid:
    - harden (о сердце/характере)
    status: proposed
- id: muzhestvo
  ru: мужество
  sense: мужество (нередко в паре с бесстрашием); «Мужайся, друг» — обращение в письмах
  tier: core
  first_seen: p1-c02-041
  counts:
    p1: 23
    p2: 47
    p3: 94
  evidence:
  - id: p3-c01-082
    ru: Мужайся, друг.
    en_legacy: Don’t lose your courage, my friend.
  en:
    term: courage
    legacy: courage ≈71; brave ≈22; fortitude ≈19
    avoid: []
    status: proposed
- id: sila#power
  ru: Сила / Силы (с прописной)
  sense: 'высшая сила: Божественная Сила, Единая Сила, Сила Света, Высшие/Великие/Светлые Силы'
  distinguish: строчные «силы» (физические, душевные, «силы духа») — strength/powers по контексту; тёмные силы — temnye-sily
  tier: core
  first_seen: p3-c06-062
  counts:
    p1: 0
    p2: 0
    p3: 45
  evidence:
  - id: p3-c26-117
    ru: в море золотого Света, промчавшегося … от Божественной Силы, охраняющей, защищающей, созидающей и правящей Землей
    en_legacy: the golden Light which poured out of the Divine Power that protects, defends, creates and rules the Earth
  - id: p3-c18-042
    ru: Единой Сущности, проливающей во вселенную свои Силу, Свет и Мир
    en_legacy: who pours his Power, Light and Calm into the entire universe
  en:
    term: Power
    legacy: Power ≈34; power ≈5
    avoid:
    - Force
    status: proposed
- id: bozhestvennyi
  ru: божественный / Божественный
  sense: божественный; с прописной в титулах и именованиях (Божественные Владыки, Божественная Сила, Божественная Мать)
  tier: core
  first_seen: p1-c22-185
  counts:
    p1: 8
    p2: 26
    p3: 119
  evidence:
  - id: p3-c21-068
    ru: мешает осуществляться плану Божественной Силы
    en_legacy: impedes to fulfil the plan of the Divine Power
  en:
    term: divine / Divine (как в RU)
    legacy: divine ≈79; Divine ≈48; God 7
    avoid: []
    status: proposed
- id: istina
  ru: истина / Истина
  sense: истина; с прописной — Истина как начало («слуга Истины», «Истина одна — путей к Ней много» p3-c26-122)
  tier: core
  first_seen: p1-c05-004
  counts:
    p1: 9
    p2: 15
    p3: 101
  evidence:
  - id: p3-c04-207
    ru: Чтобы дойти до живой в себе Истины, надо развить в себе любовь к человеку.
    en_legacy: In order for you to achieve the living Truth within yourself, you need to develop your love for man
  - id: p3-c07-033
    ru: в порыве самого пылкого искания путей к Истине
    en_legacy: flight of your searching for the path to the Truth
  en:
    term: truth / Truth (как в RU)
    legacy: Truth ≈61 для прописной; truth ≈116 всего
    avoid: []
    status: proposed
- id: ogon
  ru: Огонь (с прописной)
  sense: высший Огонь (священный Огонь на алтаре, «Огонь Вечного», «Огонь Радости»); «чаша Огня»
  distinguish: строчный огонь — fire; «капля огня Вечности» p3-c01-071 — drop, не spark
  tier: core
  first_seen: p2-c02-022
  counts:
    p1: 0
    p2: 3
    p3: 58
  evidence:
  - id: p3-c04-168
    ru: перед Огнем Вечного
    en_legacy: before the Fire of Eternity
  en:
    term: Fire
    legacy: Fire ≈55; fire ≈7
    avoid:
    - Flame
    status: proposed
- id: zemlya#planet
  ru: Земля (с прописной)
  sense: 'планета Земля как поле труда Учителей и Братства: «Владыки Земли», «на Земле»'
  distinguish: 'строчная «земля» (≈723): земная жизнь и земной мир — zemlya#earth («жизнь на земле», «пока земля нуждается
    в тебе»); почва, страна — ground, land по контексту. Прописная появляется только с p3-c19 (13 глав).'
  tier: core
  first_seen: p3-c19-042
  counts:
    p1: 0
    p2: 0
    p3: 207
  evidence:
  - id: p3-c21-073
    ru: вся сила вашей жизни дней на Земле и весь их смысл — в труде для Вечного
    en_legacy: the entire energy of your days on the Earth and their whole meaning – that’s the work for Eternity
  en:
    term: the Earth
    legacy: Earth ≈145; earth ≈45
    avoid: []
    status: proposed
- id: zemlya#earth
  ru: земля (строчная)
  sense: 'земная жизнь, земной мир как поле труда человека: «жить на земле», «уйти с земли», «жизнь земли и неба», «условности
    земли», «пока земля нуждается в тебе»'
  distinguish: zemlya#planet — «Земля» с прописной (планета, ч. III с p3-c19); почва, пол, страна — ground, land («опустил
    меня на землю» p1-c02-084, «лежавших на земле» p1-c25-207).
  tier: core
  first_seen: p1-c09-099
  counts:
    p1: 25
    p2: 77
    p3: 253
  note: 'сквозное понятие поучений: земная жизнь как место труда ученика; противопоставление «земли и неба»'
  evidence:
  - id: p1-c09-099
    ru: вы не можете понять счастья жить на земле
    en_legacy: you cannot even understand what happiness it is to live on the earth
  - id: p2-c01-327
    ru: Мы должны жить на земле, для земли, для людей.
    en_legacy: We must live on earth for the sake of the earth, for people.
  - id: p3-c11-143
    ru: Не стремись выше, пока земля нуждается в тебе.
    en_legacy: Don’t force your way up until the earth needs you
  - id: p1-c26-034
    ru: восприятия жизни земли и неба как единой живой жизни
    en_legacy: perception of the visible life of the earth and heaven as the only living life
  en:
    term: earth
    legacy: the earth / earth (строчная) — «the earth» 36/137/354 во всём тексте (все значения, включая почву); the Earth
      0/14/216 — в основном zemlya#planet
    avoid:
    - Earth (с прописной для строчной «земли»)
    status: proposed
  question: 'on earth (без артикля, как в английской идиоме «on earth») или on the earth (как чаще в старом EN)? Рекомендация:
    «на земле» — on earth; «жизнь земли», «условности земли» — of the earth.'
- id: bog
  ru: Бог / Господь
  sense: Бог; «Господь», «Господи» — в молитвах и восклицаниях
  distinguish: «Божий», «Божественный» — bozhestvennyi; «Владыко» в молитве — vladyka#god (тоже Lord); местоимения Он/Его/Ты
    с прописной — rule#capital-pronouns
  tier: core
  first_seen: p1-c01-080
  counts:
    p1: 46
    p2: 67
    p3: 305
  evidence:
  - id: p1-c02-023
    ru: И во что выливается религия, зовя к Богу
    en_legacy: which as though is leading us to God
  - id: p1-c04-067
    ru: мои молитвы хорошо доходят до Бога
    en_legacy: my prayers were always reaching God
  en:
    term: God; Lord (Господь)
    legacy: God ≈343; Lord ≈33 (для «Господь»)
    avoid: []
    status: proposed
- id: formula#mir-tebe
  ru: Мир тебе / Мир вам
  sense: приветствие посланцев Братства и Учителей, также прощание («Прощайте, мир вам»)
  tier: core
  first_seen: p3-c02-240
  counts:
    p1: 0
    p2: 0
    p3: 8
  evidence:
  - id: p3-c02-240
    ru: — Мир тебе, брат мой милый, неси людям радость.
    en_legacy: “Peace to you, my dear brother, carry joy for people.
  - id: p3-c17-165
    ru: — Мир тебе, Раданда.
    en_legacy: “Peace to you, Radanda.
  - id: p3-c10-156
    ru: Мир тебе, друг мой, передавай мой мир каждому
    en_legacy: Peace to you, my dear friend, give my calm to everybody
  - id: p3-c19-027
    ru: — Мир тебе, брат мой Всеволод.
    en_legacy: “Peace to you, my brother Vsevolod.
  en:
    term: Peace to you
    legacy: Peace to you (5 из 5 проверенных); но «мой мир» в той же фразе → my calm (p3-c10-156)
    avoid:
    - calm
    status: proposed
  question: Peace to you (старый EN, 5 из 5, дословно и не ошибка) или Peace be with you (устойчивая английская формула)?
    По §9.2 п.6 рабочий вариант — старый; Peace be with you — предложение владельцу, довод только идиоматичность. «Мир вам»
    — Peace to you all / Peace to you по контексту.
- id: formula#privet-i-mir
  ru: Прими мой привет и мир
  sense: концовка письма Учителя (Али); с ней же — «Примите привет Светлого Братства»
  distinguish: мир#peace (покой) ≠ мир#world
  tier: core
  first_seen: p3-c01-083
  counts:
    p1: 0
    p2: 0
    p3: 2
  note: в английской концовке письма устойчиво мн. ч. greetings; «Примите привет Светлого Братства» (p3-c25-085) — Accept
    the greetings of the Bright Brotherhood
  evidence:
  - id: p3-c01-083
    ru: Прими мой привет и мир.
    en_legacy: Accept my regards and calm.
  en:
    term: Accept my greetings and my peace.
    legacy: Accept my regards and calm. (calm — ошибка; regards — бытовой регистр)
    avoid:
    - calm
    - regards
    status: proposed
- id: formula#pozhatie
  ru: Прими моё пожатие (бодрости и энергии); бодрое пожатие руки
  sense: 'концовка писем Али: рукопожатие как передача бодрости'
  tier: core
  first_seen: p1-c06-019
  counts:
    p1: 1
    p2: 0
    p3: 1
  note: '«handshake of vigour and energy» натянуто: «handshake of X» естественно только с отношением (of friendship); full
    of передаёт родительный качества RU. «друг» во вставке — my friend (drug#address). Допустимая альтернатива для p3-c01-078
    — the vigorous clasp of my hand (личная теплота, отчёт §6.5)'
  evidence:
  - id: p1-c06-019
    ru: Жму твою руку. Прими моё пожатие бодрости и энергии…
    en_legacy: I am squeezing your hand. Accept my handshake full of cheerfulness and energy…
  - id: p3-c01-078
    ru: Прими, друг, бодрое пожатие моей руки
    en_legacy: My friend, accept my energetic handshake
  en:
    term: p1-c06-019 — I clasp your hand. Accept my handshake, full of vigour and energy…; p3-c01-078 — Accept, my friend,
      the vigorous clasp of my hand
    legacy: handshake full of cheerfulness and energy; energetic handshake
    avoid: []
    status: proposed
- id: formula#drug-brat-syn
  ru: «Друг, брат и милый сын!» / «Друг и брат» / «мой друг и брат»
  sense: обращение Учителя в письме и речи; «друг и брат» — устойчивое обращение между Учителями и к ученикам (14 раз во всех
    частях)
  tier: core
  first_seen: p1-c02-119
  counts:
    p1: 4
    p2: 4
    p3: 7
  evidence:
  - id: p3-c01-066
    ru: «Друг, брат и милый сын!»
    en_legacy: My friend, my brother and dear son!
  - id: p1-c02-119
    ru: «Друг и брат, — начиналось оно, —…»
    en_legacy: “My friend and brother,” the letter started
  - id: p3-c28-040
    ru: Прими мое благословение, друг и брат.
    en_legacy: Accept my blessing, my friend and brother.
  en:
    term: Friend and brother; Friend, brother and dear son!
    legacy: my friend and brother (последовательно, с добавленным my); My friend, my brother and dear son!
    avoid: []
    status: proposed
  question: 'Сохранять ли добавленное старым EN «my» (My friend and brother) там, где RU без «мой»? Рекомендация: без my,
    как в RU (Friend and brother), с my — где RU «мой друг и брат».'
- id: formula#bud-blagosloven
  ru: Будь благословен(на) / Будьте благословенны
  sense: благословение-прощание Учителя в конце речи или письма; часто продолжается «Иди, любимая и любящая…»
  tier: core
  first_seen: p2-c06-162
  counts:
    p1: 0
    p2: 4
    p3: 45
  note: 'мн. ч. — то же («May you be blessed in the name of the Bright Brotherhood — peace to you», p3-c18-056); для тёплой
    личной интонации допустимо Blessings on you. Bless you британскому читателю — ответ на чихание или снисходительное «bless
    you, dear»; Be blessed звучит как современное американское церковное прощание, и повелительное наклонение здесь неестественно:
    быть благословлённым не зависит от адресата. Формула — 49 раз'
  evidence:
  - id: p3-c06-069
    ru: Будь благословенна. Иди любимая и любящая, радующая и радующаяся, творящая и двигающая к творчеству.
    en_legacy: Be blessed. Go loved and loving, glad and gladdening, creating and encouraging creation.
  - id: p3-c18-056
    ru: Будьте благословенны именем Светлого Братства — мир вам.
    en_legacy: Be blessed on behalf of the Bright Brotherhood – peace to you.
  en:
    term: May you be blessed
    legacy: Be blessed (≈64 для «благословен*»)
    avoid:
    - Bless you
    status: proposed
  question: Be blessed (старый EN, ≈64, последовательно) или May you be blessed? По итогам языкового ревью рабочий вариант
    — May you be blessed (желательный оборот, торжественно и без архаики); Be blessed — старый вариант, остаётся на выбор
    владельца.
- id: formula#lyubimyi-i-lyubyashchii
  ru: Иди, любимая и любящая (любимые и любящие)
  sense: продолжение благословения при отпускании ученика (p2-c06-164, p2-c17-012, p3-c06-069)
  tier: core
  first_seen: p2-c06-164
  counts:
    p1: 0
    p2: 2
    p3: 2
  evidence:
  - id: p2-c17-012
    ru: Будь благословенна. Иди, любимая и любящая, и храни в мире всех тех, кто тебе повстречается.
    en_legacy: Be blessed. Go being loved and loving others, protect all of those whom you meet.
  en:
    term: Go, loved and loving
    legacy: Go loved and loving; Go being loved and loving others; p2-c06-164 — “I bless you one more time, live in harmony,
      go with joy day after day, loving and loved.” (порядок причастий обратный, «благословенны» → I bless you)
    avoid: []
    status: proposed
- id: formula#idi-s-mirom
  ru: Иди(те) с миром
  sense: отпускание с благословением
  tier: core
  first_seen: p3-c10-054
  counts:
    p1: 0
    p2: 0
    p3: 3
  evidence:
  - id: p3-c10-054
    ru: Иди с миром, мой пес дорогой, все благополучно.
    en_legacy: Go calmly, my dear dog, everything is all right.
  - id: p3-c21-180
    ru: Идите с миром отсюда и внесите его в каждое новое дело и встречу.
    en_legacy: Leave this place with calm and spread it in your every…
  - id: p3-c22-051
    ru: «Иди с миром, сын мой»
    en_legacy: “Go with peace, my son,”
  en:
    term: Go in peace
    legacy: Go calmly; with calm; Go with peace — три разных варианта на 3 вхождения
    avoid:
    - calmly
    - with calm
    - with peace
    status: proposed
- id: formula#blazhenstvo
  ru: Блаженство Любви, блаженство Мира, блаженство Радости, блаженство Бесстрашия
  sense: формула благословения четырьмя «блаженствами» (аспектами Любви) — произносится при крестном знамении, при исцелении
  distinguish: те же четыре начала — «Любовь, Мир, Радость и Бесстрашие» (p3-c13-006), «четырёх блаженств» (p3-c08-075)
  tier: core
  first_seen: p3-c08-105
  counts:
    p1: 0
    p2: 0
    p3: 7
  evidence:
  - id: p3-c08-105
    ru: «Блаженство Любви, блаженство Мира, блаженство Радости, блаженство Бесстрашия, летите Гармонией моей верности…»
    en_legacy: “bliss of Love, bliss of Calm, bliss of Joy, bliss of Fearlessness, fly with the wings of harmony of my loyalty…
  - id: p3-c19-095
    ru: «Блаженство Любви, Блаженство Мира, Блаженство Радости, Блаженство Бесстрашия да обнимут тебя»
    en_legacy: “Let the Bliss of Love, the Bliss of Calm, the Bliss of Joy and the Bliss of Fearlessness cover you.”
  - id: p3-c14-152
    ru: блаженство Любви, мира, радости и бесстрашия
    en_legacy: the bliss of Love, Calm, Joy and Fearlessness
  en:
    term: the bliss of Love, the bliss of Peace, the bliss of Joy, the bliss of Fearlessness
    legacy: Мир → Calm во всех проверенных (4 из 4); «летите Гармонией» → fly with the wings of harmony (добавлено «крыльев»)
    avoid:
    - Calm
    status: proposed
- id: formula#svet-i-mir
  ru: Свет и Мир (в человеке)
  sense: то, что ученик должен видеть и «нести» в каждом встречном
  tier: core
  first_seen: p3-c03-103
  counts:
    p1: 0
    p2: 0
    p3: 6
  evidence:
  - id: p3-c05-100
    ru: видишь в человеке не его личные качества, и его Свет и Мир
    en_legacy: you can see not the personal man’s characteristics, but his Light and Calm
  - id: p3-c10-044
    ru: «Да раскроются очи духа моего к Свету и Миру, что в человеке живут.»
    en_legacy: “Let my eyes of spirit open for the Light and Calm that is living within man.
  en:
    term: Light and Peace
    legacy: Light and Calm (4 из 4 проверенных)
    avoid:
    - Calm
    status: proposed
- id: formula#nikto-ne-drug
  ru: «Никто тебе не друг, никто тебе не враг (брат), но всякий (каждый) человек тебе (великий) Учитель»
  sense: изречение-завет ученику; в ч. III названо «поговоркой у нашего народа» (p3-c07-034) и «первым изречением, даваемым
    ученикам» (p3-c22-089)
  distinguish: 'в RU две редакции: «не враг» — p1-c23-070, p2-c01-358, p2-c10-128, p3-c20-166; «не брат» — p3-c07-034, p3-c09-036,
    p3-c22-089. Их нельзя унифицировать при переводе. «Учитель/учитель» и «великий» — колеблются.'
  tier: core
  first_seen: p1-c23-070
  counts:
    p1: 1
    p2: 2
    p3: 4
  note: 'варианты RU передаются по месту: «не брат» → no one is your brother (p3-c07-034, p3-c09-036, p3-c22-089 — сам RU
    даёт эту редакцию в 3 из 7 мест); «великий» → great; «Учитель/учитель» — по прописной RU. Замена «враг» → brother в старом
    EN (3 из 4) может быть гармонизацией или следом другой редакции RU (вопрос D14 о канонической редакции); правку по нашему
    RU это не ослабляет'
  evidence:
  - id: p1-c23-070
    ru: никто тебе не друг, никто тебе не враг, но всякий человек тебе Учитель
    en_legacy: nobody is a friend to you, nobody is a brother to you, but every man is a Teacher to you
  - id: p2-c01-358
    ru: «Никто тебе не друг, никто тебе не враг, но всякий человек тебе учитель»
    en_legacy: “No one is a friend or a brother to you, but every man is a Teacher to you”
  - id: p2-c10-128
    ru: «Никто тебе не друг, никто тебе не враг, но каждый человек тебе учитель»
    en_legacy: “Nobody is a friend for you, nobody is a brother for you, but every man is your teacher.”
  - id: p3-c20-166
    ru: 1. Никто тебе не друг, никто тебе не враг, но каждый человек тебе великий Учитель.
    en_legacy: 1. No one is a friend for you, no one is an enemy for you, but every man is a great Teacher for you.
  en:
    term: No one is your friend, no one is your enemy, but every man is your Teacher.
    legacy: 'ОШИБКА: «не враг» → brother в 3 из 4 случаев (p1-c23-070, p2-c01-358, p2-c10-128); верно enemy только в p3-c20-166.
      Также Teacher/teacher и формы (nobody / no one; to you / for you) разнятся.'
    avoid: []
    status: proposed
  question: 'Утвердить одну английскую форму изречения с вариантами по RU (enemy / brother, great)? Прописная: RU пишет «Учитель»
    4 раза (p1-c23-070, p3-c07-034, p3-c09-036, p3-c20-166) и «учитель» 3 раза (p2-c01-358, p2-c10-128, p3-c22-089) — это
    не единичное колебание, а изречение может значить и обычного учителя (каждый человек тебя чему-то учит). Рекомендация:
    зеркалить прописную RU по месту (rule#capitalized-concepts); унификация Teacher везде — только решением владельца.'
- id: formula#muzhaysya
  ru: Мужайся (мужайтесь), друг.
  sense: формула ободрения у Учителей (И., Али)
  tier: core
  first_seen: p1-c12-038
  evidence:
  - id: p3-c01-082
    ru: Мужайся, друг.
    en_legacy: Don’t lose your courage, my friend.
  - id: p1-c15-072
    ru: — Мужайтесь, друг, — услышал я голос И.
    en_legacy: “Be strong, my friend,”
  - id: p1-c12-038
    ru: — Мужайтесь. Мать должна быть примером своим детям.
    en_legacy: “Be strong. A mother must be an example to her children.
  en:
    term: Be strong, my friend.
    legacy: Be strong, my friend / Don’t lose your courage, my friend
    avoid: []
    status: proposed
  question: Be strong (старый EN, вариант большинства и не ошибка) или Take courage (ближе к одному слову «мужайся»)? По §9.2
    п.6 рабочий вариант — Be strong; Take courage — предложение, довод только стилистический. «Don’t lose your courage» (p3-c01-082)
    привести к той же формуле.
- id: formula#zovi-imya
  ru: зови имя моё «Али», и я отвечу тебе немедленно
  tier: core
  first_seen: p3-c01-083
  evidence:
  - id: p3-c01-083
    ru: крепко и уверенно думай обо мне, зови имя мое «Али», и я отвечу тебе немедленно
    en_legacy: think about me strongly and firmly, call me by name, and I will respond to you immediately
    note: 'annot.: имя «Али» опущено'
  en:
    term: call my name, ‘Ali’, and I will answer you at once
    legacy: call me by name (имя опущено)
    avoid: []
    status: proposed
- id: podpis#tvoy-drug
  ru: твой друг Али Махоммет
  sense: подпись письма (RU здесь пишет «Махоммет», в p1-c01 — «Мохаммед»; форма имени — characters.yml)
  tier: core
  first_seen: p3-c01-084
  evidence:
  - id: p3-c01-084
    ru: твой друг Али Махоммет"
    en_legacy: '*Your friend Ali Mahomet*'
  en:
    term: Your friend, Ali … (имя по characters.yml)
    legacy: Your friend Ali Mahomet
    avoid: []
    status: proposed
- id: rule#capitalized-concepts
  ru: прописные буквы у понятий (Жизнь, Любовь, Свет, Мир, Радость, Истина, Вечность, Вечное, Мудрость, Милосердие, Огонь,
    Сила, Гармония…)
  sense: в части III (реже во II) слова-понятия пишутся с прописной, когда означают высшее начало, и со строчной в обычном
    значении; иногда колеблется без различия смысла (Вселенная/вселенная, Учитель/учитель в изречении)
  tier: core
  first_seen: p1-c14-034
  counts:
    p1: 0
    p2: 0
    p3: 0
  note: 'Старый EN в основном сохраняет прописную (Life ≈265/320, Love ≈185/209, Light ≈184/210, Joy ≈57/77), но не везде.
    «Мудрость» отдельной записи не имеет: старый EN последователен (wisdom ≈199 на ≈185 «мудрост*»), прописная — по этому
    правилу.'
  evidence:
  - id: p3-c04-207
    ru: Чтобы дойти до живой в себе Истины
    en_legacy: to achieve the living Truth within yourself
  - id: p3-c21-073
    ru: в труде для Вечного
    en_legacy: the work for Eternity
  en:
    term: сохранять прописную RU у понятий-начал; строчную — в обычном значении
    legacy: в основном сохраняет; потери — ≈10–20% (напр., Жизнь → life ≈55)
    avoid: []
    status: proposed
  question: Зеркалить прописные RU у понятий в EN (рекомендация) или ввести собственный список понятий, всегда пишущихся с
    прописной? Колебания RU без различия смысла (Вселенная) — выравнивать по большинству.
- id: rule#capital-pronouns
  ru: прописные местоимения Вы/Вам/Ваш; Он/Его/Ему/Им; Она/Ее/Ей; Ты/Тебе/Твой; Свой, Сам(а)
  sense: '(1) Вежливое «Вы/Вам/Ваш» с прописной (1 515 раз в середине предложения в ч. III против 2 263 строчных): в ч. I–II
    — почти только в письмах (капитан Джемс p1-c22-053…056, Левушка p1-c24-160…162, Флорентиец p2-c07-029…032, p2-c10-039…040);
    в ч. III — и в обычных диалогах целых глав (p3-c01 78 прописных / 4 строчных; p3-c05 163/10; p3-c11 277/35), причём непоследовательно
    даже внутри фразы: «Вас вместе с Вашим приятелем приглашает дедушка. Он желает угостить вас» p3-c17-010; так говорят и
    незнакомые девушки (p3-c17-007), и Левушка с Ясcой (p3-c01-018). Это вежливая форма издания/рукописи, а не знак благоговения.
    (2) Он/Его/Ее/Ты/Твой/Свой с прописной (≈470) — о Боге (p2-c01-295, p3-c31-140), Великой Матери (p3-c33-044, p3-c32-129),
    Жизни (p3-c23-007, p2-c04-073), Истине (p3-c27-009), Вечном/Вечном Движении (p3-c27-023, p3-c30-020), в молитвах «Ты/Твой»
    (p3-c08-086, p3-c26-115); изредка — об Учителях-людях: Али (p3-c14-027 «послать Ему»), Франциск (p3-c17-051 «Его освобожденная
    Любовь»), Учитель вообще (p3-c15-173 «Его доброта»).'
  tier: core
  first_seen: p1-c22-053
  counts:
    p1: 37
    p2: 308
    p3: 1939
  evidence:
  - id: p3-c17-010
    ru: Вас вместе с Вашим приятелем, приглашает дедушка. Он желает угостить вас нашим…
    en_legacy: (you — со строчной)
  - id: p3-c20-125
    ru: О, Великая Мать… ибо я видел Тебя
    en_legacy: Oh, Great Mother, in this moment I desire to burn down in Your fire and to give my life to You, because I saw
      You
  - id: p3-c21-081
    ru: Не передышки посылает Жизнь… но Сама оживает
    en_legacy: but Life Himself comes to life
  - id: p3-c28-008
    ru: Тех, кого Истина посылает Своими гонцами, Она закаляет в единении с Нею.
    en_legacy: Those whom the Truth is sending as her messengers, She hardens with unity with Herself.
  en:
    term: вежливое Вы → you (строчная, как всегда в старом EN); местоимения о Боге (He/His/Him, You/Your в молитве) и Великой
      Матери (She/Her, You/Your) — с прописной; о Жизни — it/its (не Himself); об Учителях-людях — he/his со строчной
    legacy: 'вежливое Вы — всегда you (прописных You вне молитв в ч. III нет: 14 You/19 Your с прописной — только обращения
      к Богу/Великой Матери, p3-c08-086, p3-c20-125). Для божества прописная непоследовательна: в Vol3 224 прописных He/His/Him/Her/She/Himself/Herself
      в середине фразы на 424 прописных RU-местоимения ч. III; p3-c28-006 «as her messengers, She…» — в одной фразе обе. «Life
      Himself/himself» — 18 раз (ошибка рода).'
    avoid:
    - Life Himself
    - You (для вежливого Вы)
    status: proposed
  question: 'Как передавать? Варианты: (а) рекомендация: вежливое Вы — you без прописной (англ. норма не знает вежливой прописной;
    старый EN так и делал); прописные He/She/You — только для Бога и Великой Матери (и в молитвах), для Жизни/Истины/Вечного
    — it/its без прописной, для Учителей-людей — he; (б) сохранять прописные для всех случаев, где они есть в RU (включая
    Жизнь → She/Her, Истину → She, Али → He) — ближе к RU, но в EN непривычно и RU сам непоследователен; (в) вообще без прописных
    местоимений. Доводы за She для Жизни — в zhizn#life-divine (там рекомендация помечена как стилистическая). Нужен выбор
    владельца: влияет на тон всей ч. III.'
```

# Журнал решений (для справки)

````markdown
# Журнал решений

Каждое решение — один раз и навсегда, пока владелец его не изменит. Ссылаться: `DEC-003`.
Новые решения добавлять в конец. Изменённое решение не удалять, а пометить «заменено DEC-0xx».

| ID | Дата | Решение | Кто |
|---|---|---|---|
| DEC-001 | 2026-09-26 | Делаем **свою версию** проекта (не продолжение форка `gorodnichy/two-lives-book`): сайт для чтения, PDF/EPUB, EN → затем PL | владелец |
| DEC-002 | 2026-09-26 | Глоссарий — **первый шаг**, до пилота. Схема утверждения — **вариант Б**: `core`-термины (понятия учения, имена, титулы, обращения, формулы) утверждает только владелец. `secondary` утверждаются автоматически, если внешние ревьюеры не возразили. Правила «первый вариант держится» и «дубли по русской лемме запрещены» (TRANSLATION-PROCESS §9). *Уточнено: объём до пилота — DEC-011; значения, раздельное утверждение по языкам и явное подтверждение — DEC-015* | владелец |
| DEC-003 | 2026-09-26 | **Старый английский перевод — основа** для EN (режим «редактура»), а не просто справочник. До пилота — внимательный анализ: стиль, качество, систематические ошибки, выводы. Владелец исходит из того, что перевод вычитывался под руководством Дмитрия Городничего. Владелец не носитель английского и полагается на эту вычитку плюс внешние ревью. Заново переводим только отсутствующее (часть III с гл. 10, часть IV). *Уточнено DEC-010: с полным Vol3 заново — только часть IV* | владелец |
| DEC-004 | 2026-09-26 | Вариант английского — **предварительно британский**, как в старом переводе (там последовательно британская орфография с оксфордским *-ize*: colour, honour, grey, theatre, но recognize, realize). Окончательно — по итогам анализа стиля (PLAN, этап 2). *Утверждено окончательно — DEC-024* | владелец (предв.) |
| DEC-005 | 2026-09-26 | **Внешних ревьюеров запускает владелец вручную.** Агент на контрольной точке коммитит, пушит, кладёт `request.md` и даёт в чат стартовый промпт (что ревьюим, цель, формат ответа), затем останавливается (TRANSLATION-PROCESS §7.1). *Дополнено DEC-013: перед внешним — внутреннее ревью агентами* | владелец |
| DEC-006 | 2026-09-26 | Коммиты **без трейлеров соавторства** (`Co-Authored-By`, `Claude-Session` и т. п.) | владелец |
| DEC-007 | 2026-09-26 | Технологии — на усмотрение исполнителя («главное, чтобы работало»). Выбрано: Astro (статический сайт), ~~Cloudflare Pages~~ (хостинг — см. DEC-009), позиция чтения в `localStorage`, PDF — Typst, EPUB — Pandoc (ARCHITECTURE.md) | владелец делегировал |
| DEC-008 | 2026-09-26 | Работа по этапам начинается **только по команде владельца** | владелец |
| DEC-009 | 2026-09-26 | Сайт **сначала работает локально** и **деплоится куда угодно**: сборка — обычная папка `dist/` со статикой (включая PDF/EPUB и поиск). Сначала — любой сервис статических сайтов, потом — свой сервер (Docker + Caddy или nginx). Никаких платформенных функций в основе сайта. Будущий сервис синхронизации — самостоятельный (Node + SQLite), в том же docker compose, необязательный | владелец |
| DEC-010 | 2026-09-26 | Новый **Vol3** (`sources/en-legacy/New/TwoLives-Vol3.pdf`) принят как источник старого перевода части III: проверено — все 33 главы и окончание присутствуют, признаков крупных пропусков не обнаружено; полнота уточняется при выравнивании. Вся часть III идёт в **редактуру**, на английский заново переводится только часть IV. Vol1/Vol2 в `New/` идентичны прежним. Для гл. 1–9 при извлечении используется чистый PDF 2022 года (текст тот же, в новом PDF часть фрагментов извлекается слитно). *Способ восстановления — DEC-020* | владелец |
| DEC-011 | 2026-09-26 | **Полный цикл сначала на одной главе**, потом массовая обработка. До пилота утверждаем только **ядро глоссария** (сквозные core-термины, главные персонажи) и термины выбранных глав и отрывков. Дальше глоссарий растёт поглавно. *Уточнено DEC-019* | владелец |
| DEC-012 | 2026-09-26 | **Основная модель-редактор выбирается слепым сравнением** на 4–5 характерных отрывках (калибровочный набор), а не закрепляется за Claude заранее. Потом держим единый голос. Смена модели — только через калибровку на том же наборе | владелец |
| DEC-013 | 2026-09-26 | **Два уровня ревью:** сначала внутреннее — агенты со свежим контекстом, можно того же семейства, что редактор; затем внешнее — владелец вручную отдаёт подготовленный пакет независимым моделям **другого семейства**, чем редактор (например, Grok или OpenAI). Внутреннее не заменяет внешнее. Внешних запускает только владелец. *Состав внутренних проходов — DEC-021* | владелец |
| DEC-014 | 2026-09-26 | Работа со старым переводом — **три отдельных шага**: неизменённое извлечение (только техническая чистка) → выравнивание по ID оригинала (1:1, 1:N, N:1, N:M, пропуски, лишнее) → литературная редактура. Правила ID: буквенный суффикс (`012a`) — новый абзац **оригинала**; суффикс через точку (`012.2`) — часть абзаца **в переводе**; ~~диапазон (`012..014`) — склейка в переводе~~ (заменено DEC-022). Инвариант: каждый ID оригинала покрыт ровно один раз и по порядку (ARCHITECTURE §3) | владелец |
| DEC-015 | 2026-09-26 | Глоссарий: **разные значения одного слова — отдельные записи** (`ru#sense`); **утверждение раздельно по языкам** (EN и PL); **явное подтверждение ревьюером** — молчание или `unsure` не означает согласия. `secondary` утверждается автоматически, только если хотя бы один внешний ревьюер ответил `agree` и никто не ответил `object` | владелец |
| DEC-016 | 2026-09-26 | Ревью **привязано к версии**: пакет содержит коммит (текст + правила), хеш главы и хеш источника. После исправлений принятые `critical`/`major` **перепроверяются**. Метрики считаются по **подтверждённым** ошибкам. Статусы глав — **только** в `translation/status.yml` | владелец |
| DEC-017 | 2026-09-26 | Для пилота — **локальный просмотр** RU \| старый EN \| новый EN с подсветкой изменений (`npm run compare`) и **пробная сборка главы** в EPUB/PDF. Полноценный сайт — после пилота | владелец |
| DEC-018 | 2026-09-26 | **Первый внутренний круг — на Claude** (модель текущих сессий Claude Code, по выбору владельца): подготовка, редактура пилота, внутреннее ревью, первый кандидат в сравнении моделей. Внешние модели подключает и ведёт владелец: есть Grok, дальше модели GPT и другие по его выбору. Пока редактор — Claude, внешние ревьюеры — не из семейства Claude | владелец |
| DEC-019 | 2026-09-26 | **Пилотный трек:** этапы 1–6 проходятся на `p1-c01` плюс отрывках для сравнения моделей. Массовая подготовка корпуса (этап 1 на все главы) делается, когда удобно, но **не блокирует пилот**; обязательна перед этапом 7 | владелец |
| DEC-020 | 2026-09-26 | Слитный текст при извлечении — **сначала диагностика**: визуальный просмотр страниц, сравнение нескольких способов извлечения, восстановление пробелов **по координатам символов**. Словарь — только вспомогательный способ, каждое сомнительное место сверяется со страницей | владелец |
| DEC-021 | 2026-09-26 | Внутреннее ревью: **на пилоте все три прохода** (точность, терминология, язык), меряем вклад каждого в подтверждённые замечания, затем фиксируем достаточную схему (например, один общий ревьюер для обычных глав + отдельные проходы для сложных). Языковой ревьюер читает только английский, но его правки перед принятием сверяются с RU | владелец |
| DEC-022 | 2026-09-26 | Соответствие ID: блок перевода перечисляет покрываемые канонические ID **явным списком**, диапазонов нет. При сборке строится таблица «канонический ID → блок», у блока есть якорь на каждый ID; переключение языка, ссылки и позиция чтения работают через канонические ID. Литературные границы абзацев сохраняются | владелец |
| DEC-023 | 2026-09-27 | **Выводы этапа 2 утверждены** (`translation/analysis/legacy-en-report.md`): старый EN редактируем, а не переводим заново; вся проза сверяется с RU сплошь; норма — построчная редактура (L2), переписывание фраз (L3) — везде, где нарушен смысл, в поучениях Учителей без ограничения доли; песня Ананды (p1-c20-213) — перевод заново (L4). Проценты уровней из выборки — описание, **не норматив вмешательства** | владелец |
| DEC-024 | 2026-09-27 | Английский — **британский с оксфордским -ize** (colour, honour, grey, theatre; recognize, realize), окончательно. Американизмы старого перевода приводим к норме **в контексте предложения**, без слепой массовой замены (*gotten* → *got*, где это верно) | владелец |
| DEC-025 | 2026-09-27 | **Речевые характеристики персонажей сохраняем.** Ломаная речь торговца и подобные — умеренная стилизация: отличие от речи рассказчика сохраняется, но не усиливается до карикатуры. Правило закрепляется **несколькими утверждёнными образцами реплик** (стайлгайд, этап 4; реплики торговца — p1-c01-014, 029), а не только абстрактной формулировкой | владелец |
| DEC-026 | 2026-09-27 | **Стихи:** смысл и образы обязательны, ритм желателен, рифма — не любой ценой. Для песни Ананды (p1-c20-213, пять строк) готовим рифмованный и нерифмованный варианты и выбираем по результату. Это решение **не означает**, что любые другие стихи автоматически переводятся заново: для каждого стихотворения глубина правки решается по его разбору | владелец |
| DEC-027 | 2026-09-27 | **Критерий готовности главы:** все подтверждённые `critical` и `major` исправлены (и перепроверены, DEC-016) — независимо от плотности. Порог «0 critical и не больше 1 major на 1 000 слов» — показатель качества **первого** ревью отредактированного текста (насколько хорошо работает редактура), а не разрешение оставлять ошибки. Подтверждённые `minor` исправляются, отклонённые — с причиной в `resolution.md` | владелец |
| DEC-028 | 2026-09-27 | **Спорные термины и восстановление имён решаем на этапе 3 по контексту романа** (как персонаж представлен, происхождение, прямые указания текста), а не по последовательности старого перевода. Каждое решение — с цитатами и ID. «Так естественнее по-английски» **недостаточно** для восстановления имени персонажа: нужны основания в тексте; без них имя остаётся предложением для проверки (например, *Wadsworth* для «Уодсворд») | владелец |
````
