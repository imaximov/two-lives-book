---
unit: glossary-core
part: 3
lang: en
commit: 574498a2318e
files:
  - {path: translation/glossary.yml, sha256: bf090295a2ab0577bd73a4870a3b062cd80e00f17ce1d2030dddfc9429c39070}
  - {path: translation/characters.yml, sha256: 8a9d2382df2b304942ed13a9ce996a07aa4ab895fce4f0524c9e51c5c13e8682}
  - {path: translation/analysis/merchant-speech-draft.md, sha256: c0910da5419f0dff4a929eccf1dfa40535fa65fb1108c2c05bf3c3d88bc3deb1}
  - {path: translation/decisions.md, sha256: 9b04a201112dbd7974c3b4cdac3cf30cdd40ed630f30bcb8e0d28669653f6dad}
---

# Запрос на внешнее ревью: ядро глоссария, пакет 3 из 3 (этап 3)

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

64 id (по каждому — agree / object / unsure):

`kupets`, `torgovets`, `khozyain#shopkeeper`, `denshchik`, `dvornik`, `pomeshchik`, `uchenyy#scholar`, `bryunet`, `russkiy-soldat`, `vostochnye-lyudi`, `arab`, `khalat`, `chalma`, `pokryvalo`, `kitel`, `kaloshi`, `brosh`, `brilliant`, `dragotsennosti#pilot`, `byuro`, `papirosnaya-bumaga`, `grim`, `ryazhenyy`, `bazar`, `mechet`, `zala`, `vannaya-v-sadu`, `ekipazh`, `vorota`, `sgovor`, `sovershennoletie`, `religioznyy-pokhod`, `versta`, `rezhisser`, `moy-bog#interjection`, `pomilui#interjection`, `srednyaya-aziya`, `toponyms#p1-c01`, `allusions#arabian-nights`, `m-skiy-polk`, `kapitanskiy-mostik`, `rubka`, `shturval`, `nos-sudna`, `bort-korma`, `kren`, `pomoshnik-kapitana`, `parokhod-sudno`, `matros-verzila`, `nyanka-matros`, `korobochka-pilyuli`, `posazhennaya-mat`, `podruzhki`, `vizitnye-kartochki`, `gostinaya`, `kamin`, `zapad-vostok`, `venetsianka`, `papa#address`, `dama-sveta`, `reverans`, `zamorskaya-krasavitsa`, `realia#cal-4`, `verse-terms#cal-5`

# Термины пилотной главы p1-c01 и калибровочных отрывков (glossary.yml)

```yaml
- id: kupets
  ru: купец
  sense: торговец (сословие купцов); в p1-c01 — хозяин лавки, а также Али Мохаммед в его описании («большая важная купец»)
  distinguish: 'torgovets — «торговец» (родовое, чаще пренебрежительно: «восточный торговец» p1-c01-071)'
  tier: secondary
  first_seen: p1-c01-003
  counts:
    p1: 35
    p2: 0
    p3: 1
  note: 'довод о различении понятий, а не вкус: RU различает «купец» (сословие, крупная торговля с Персией и Россией, 029)
    и «торговец» (родовое, чаще пренебрежительно: «восточный торговец» p1-c01-071); trader уже занят «торговцем» (torgovets),
    поэтому оба слова в trader сольются. famous — ошибка (важный ≠ знаменитый).'
  evidence:
  - id: p1-c01-003
    ru: Изредка проедет шагом на осле купец на базар.
    en_legacy: From time to time, a trader would ride by slowly to the market on his donkey
  - id: p1-c01-029
    ru: Я же сказал, — большая важная купец.
    en_legacy: I have already told you. Hi is a great famous trader.
  - id: p1-c01-089
    ru: и ты сможешь сойти за важного купца
    en_legacy: and you will look like a famous trader
  en:
    term: merchant (важный купец — an important merchant)
    legacy: trader — 34 из 36 в связях; «важный» → famous (p1-c01-029, 089)
    avoid:
    - famous (для «важный»)
    status: proposed
    note: для «большая важная купец» допустимо a wealthy merchant, если важен достаток, а не положение
  question: 'merchant для «купец», trader для «торговец» — развести? Рекомендация: да; если владелец за минимальную правку
    — оставить trader, исправив только famous.'
- id: torgovets
  ru: торговец
  sense: торговец вообще (в p1-c01-071 — восточный торговец, обманывающий солдат)
  tier: secondary
  first_seen: p1-c01-071
  counts:
    p1: 10
    p2: 1
    p3: 0
  evidence:
  - id: p1-c01-071
    ru: восточный торговец зачастую расплачивался за свой обман
    en_legacy: if an Eastern trader would deceive a Russian soldier, he would have to pay dearly for that
  en:
    term: trader
    legacy: trader 7, seller/dealer 2 (в связях)
    avoid: []
    status: proposed
- id: khozyain#shopkeeper
  ru: хозяин (лавки)
  sense: владелец лавки — торговец из p1-c01 (012–034)
  tier: secondary
  first_seen: p1-c01-012
  note: the owner понятно и не ошибка (запись признаёт), но без дополнения звучит обрывочно; the shopkeeper — точнее.
  evidence:
  - id: p1-c01-012
    ru: и, наконец, решился спросить хозяина
    en_legacy: until I dared to speak to the owner
  en:
    term: the owner
    legacy: the owner (p1-c01-012, 016, 018, 021, 029)
    avoid: []
    status: proposed
  question: the owner (старый EN, p1-c01-012…029, не ошибка) или the shopkeeper (точнее, без обрывочности)? По §9.2 п.6 рабочий
    вариант — the owner; the shopkeeper — предложение владельцу, довод стилистический.
- id: denshchik
  ru: денщик
  sense: солдат-слуга при офицере (у брата Николая)
  tier: secondary
  first_seen: p1-c01-004
  counts:
    p1: 23
    p2: 0
    p3: 0
  note: 'ОШИБКА старого EN: messenger (посыльный) — 21 из 23 в связях. В p1-c01-075 «как важно зовёт денщик» опущено вместе
    с шуткой.'
  evidence:
  - id: p1-c01-004
    ru: жил в нём один со своим денщиком
    en_legacy: he was living alone with his messenger
  - id: p1-c07-021
    ru: что это денщик капитана Т.
    en_legacy: that he was the messenger of captain T.
  en:
    term: orderly
    legacy: messenger — 21 из 23
    avoid:
    - messenger
    status: proposed
  question: 'orderly или batman? batman — стандартный британский армейский термин (не разговорное слово); orderly принято
    в английских переводах русской классики и понятнее за пределами армейского словаря. Рекомендация: orderly.'
- id: dvornik
  ru: дворник
  sense: слуга при доме, открывающий ворота и следящий за двором (у Али)
  tier: secondary
  first_seen: p1-c01-045
  counts:
    p1: 8
    p2: 2
    p3: 0
  evidence:
  - id: p1-c01-045
    ru: распахнулись настежь ворота дома Али, и дворник вышел на дорогу
    en_legacy: The yard-keeper went on the road
    note: 'annot. p1-c01-045: калька; fix — porter'
  en:
    term: porter (при воротах — gatekeeper)
    legacy: yard-keeper — 8 из 10
    avoid:
    - yard-keeper
    status: proposed
- id: pomeshchik
  ru: помещик
  sense: 'землевладелец (о семье Али: «Они наша большой, богатый помещики»)'
  tier: secondary
  first_seen: p1-c01-015
  counts:
    p1: 1
    p2: 2
    p3: 0
  evidence:
  - id: p1-c01-015
    ru: Они наша большой, богатый помещики. Виноградники
    en_legacy: He is our great rich landlord. Vineyards
  en:
    term: landowner
    legacy: landlord (p1-c01-015); landowner (2, ч. II)
    avoid:
    - landlord (сдающий жильё внаём)
    status: proposed
- id: uchenyy#scholar
  ru: учёный
  sense: образованный, книжный человек (о «купце» Али и о брате-книжнике), не естествоиспытатель
  distinguish: в других местах романа «учёный» может значить scientist — проверять по контексту
  tier: secondary
  first_seen: p1-c01-030
  counts:
    p1: 9
    p2: 26
    p3: 0
  note: в сказуемом («Он, наверное, учёный») допустимо a learned man
  evidence:
  - id: p1-c01-030
    ru: Не похоже, чтобы он был купец. Он, наверное, учёный
    en_legacy: He doesn’t look like a trader. He must be a scientist
  - id: p1-c01-031
    ru: Учёный он есть такой, что и у твоя брат все книги знает.
    en_legacy: He is such a scientist that he knows all your brother’s books.
  en:
    term: scholar
    legacy: scientist — 28 из 35 в связях
    avoid:
    - scientist (для p1-c01-030, 031)
    status: proposed
- id: bryunet
  ru: брюнет
  sense: темноволосый мужчина (Али Мохаммед)
  tier: secondary
  first_seen: p1-c01-009
  counts:
    p1: 3
    p2: 0
    p3: 4
  note: brunette в английском — почти только о женщине; «чёрный люди» купца (p1-c01-014) → black man — в английском понимается
    как раса.
  evidence:
  - id: p1-c01-009
    ru: Высокий брюнет и юноша, оба были в белых чалмах
    en_legacy: The tall brunette and the youth were wearing white turbans
  - id: p1-c01-014
    ru: а один высокий чёрный люди?
    en_legacy: but about one tall black man, right?
  en:
    term: dark-haired man; «чёрный» о волосах — dark
    legacy: brunette 7 из 7; black man (p1-c01-014)
    avoid:
    - brunette
    - black man (о брюнете)
    status: proposed
- id: russkiy-soldat
  ru: русский солдат
  sense: солдаты русского гарнизона (рассказы брата, p1-c01-071–072)
  tier: secondary
  first_seen: p1-c01-071
  note: 'В том же блоке старый EN добавил «between the Russian soldiers and local Muslims» — «мусульман» в RU нет (RU: «в
    здешнем быту»). Добавление убрать.'
  evidence:
  - id: p1-c01-071
    ru: восхищался сметливостью русского солдата и его остроумием
    en_legacy: He was delighted with the quickness of wit and ingenuity of the Russian soldiers.
  en:
    term: the Russian soldier(s)
    legacy: Russian soldiers
    avoid: []
    status: proposed
- id: vostochnye-lyudi
  ru: восточные люди / восточный
  sense: жители Востока; «восточный» — о людях, обычаях, халатах
  tier: secondary
  first_seen: p1-c01-007
  evidence:
  - id: p1-c01-007
    ru: И восточные люди, с их величавым спокойствием
    en_legacy: And all of these Eastern people with their grand calm
  - id: p1-c01-096
    ru: приложив, по восточному обычаю, руку ко лбу и сердцу
    en_legacy: according to the Eastern customs, having touched his forehead and heart with his hand
  en:
    term: Eastern (люди, обычаи); oriental — допустимо для предметов (oriental silks)
    legacy: Eastern, oriental, Oriental — разнобой
    avoid: []
    status: proposed
- id: arab
  ru: араб
  sense: этноним (Левушка в гриме видит в зеркале «смуглого араба-старика»)
  tier: secondary
  first_seen: p1-c01-132
  evidence:
  - id: p1-c01-132
    ru: снова увидел в нём смуглого араба-старика
    en_legacy: again I saw that old dark-skinned Arab
  en:
    term: Arab
    legacy: Arab
    avoid: []
    status: proposed
- id: khalat
  ru: халат
  sense: восточный халат — верхняя распашная одежда (носят по нескольку сразу, p1-c01-079); ключевая реалия главы
  tier: secondary
  first_seen: p1-c01-007
  counts:
    p1: 69
    p2: 22
    p3: 10
  note: 'Отчёт §6.5 называет «халат» среди реалий. Старый EN: oriental robe — 63 раза в части I (в p1-c01 — 36 при 30 «халат»
    RU), в частях II–III — robe. Повтор oriental robe в каждой фразе утяжеляет текст; dressing-gown было бы ошибкой (домашний
    халат).'
  evidence:
  - id: p1-c01-018
    ru: — Что смотришь? Халат хочешь?
    en_legacy: “What are you looking for? Do you want an oriental robe?”
  - id: p1-c01-079
    ru: здесь носят сразу семь халатов, начиная с ситцевого и кончая шёлковым
    en_legacy: it is usual here to wear seven oriental robes at once, starting with the cotton one and ending with the silk
      one
  en:
    term: oriental robe
    legacy: oriental robe 63 (ч. I), robe 41, gown 2 (в связях)
    avoid:
    - dressing-gown (для восточного халата)
    status: proposed
    note: в ч. II–III старый EN сам пишет robe — там так и оставить
  question: '(1) Сокращать ли oriental robe до robe после первого упоминания? Старый EN в ч. I последовательно пишет oriental
    robe (не ошибка), довод за сокращение — только тяжеловесность повтора (стилистический), поэтому по §9.2 п.6 рабочий вариант
    — oriental robe; robe после первого упоминания — предложение владельцу. (2) Ввести заимствование khalat? Рекомендация:
    нет — robe понятно; khalat малоизвестно англоязычному читателю.'
- id: chalma
  ru: чалма
  sense: длинное полотнище, которым обматывают голову; и сам головной убор из него
  distinguish: 'turban — «тюрбан»: в p1-c01-091 различены: «нет второй белой чалмы, чтобы сделать тебе белый тюрбан» (чалма
    — ткань, тюрбан — намотанный убор)'
  tier: secondary
  first_seen: p1-c01-009
  counts:
    p1: 45
    p2: 1
    p3: 2
  evidence:
  - id: p1-c01-009
    ru: оба были в белых чалмах
    en_legacy: were wearing white turbans
  - id: p1-c01-091
    ru: у меня нет второй белой чалмы, чтобы сделать тебе белый тюрбан
    en_legacy: I don’t have another white turban.
  - id: p1-c01-116
    ru: брат развернул чалму, оказавшуюся длиннее, чем я предполагал
    en_legacy: My brother uncoiled the turban that seemed to me much longer than I could imagine.
  en:
    term: turban; где важна ткань (p1-c01-091, 094, 097, 116) — turban cloth
    legacy: turban (чалма и тюрбан одинаково; в 091 различие потеряно)
    avoid: []
    status: proposed
- id: pokryvalo
  ru: покрывало / чёрная сетка / паранджа
  sense: 'женские покровы: «покрывало» — накидка на голову и тело (у Наль — откидывается с лица); «чёрная сетка» — сетчатая
    волосяная завеса на лицо; «паранджа» — среднеазиатский халат-накидка'
  tier: secondary
  first_seen: p1-c01-003
  note: покрывало-накидка на голову и тело — где важен покрой, допустимо описательно (a cloak-like veil)
  evidence:
  - id: p1-c01-003
    ru: укутанных в чёрные сетки и белые или тёмные покрывала, подобно плащу скрадывающие формы тела
    en_legacy: who cover their faces with black nettings and even wrap themselves up in white and black cloaks
  - id: p1-c01-052
    ru: маленькая белая очаровательная женская ручка подняла покрывало с лица
    en_legacy: a small, white, wonderful hand of a woman drew the mantle off her face
  - id: p1-c01-050
    ru: две женщины с закрытыми чёрной сеткой лицами
    en_legacy: Two women with their faces covered
    note: 'annot. p1-c01-050: «чёрной сеткой» опущено; fix — black veils'
  - id: p1-c01-068
    ru: ходят дома без паранджи
    en_legacy: they are walking without their burqas at home
  en:
    term: покрывало — veil; чёрная сетка — black mesh veil; паранджа — veil
    legacy: cloaks (003, 033), mantle (052, 053), black nettings (003), burqas (068)
    avoid:
    - burqa (другой, афганский покров)
    - nettings
    status: proposed
  question: 'паранджа → veil или paranja? Рекомендация: veil (заимствование редкое; burqa — неточно).'
- id: kitel
  ru: китель / пижама
  sense: военная куртка офицера; пижама
  tier: secondary
  first_seen: p1-c01-020
  evidence:
  - id: p1-c01-020
    ru: ни в чём другом, как в кителе или пижаме, пока ещё не видел его
    en_legacy: because I had seen him only in his tunic or pyjamas
  en:
    term: tunic; pyjamas (британское написание)
    legacy: tunic; pyjamas
    avoid: []
    status: proposed
- id: kaloshi
  ru: калоши / чулки / туфли
  sense: кожаные калоши поверх туфель, оставляемые у дверей; «в одних чулках» — без обуви
  tier: secondary
  first_seen: p1-c01-086
  evidence:
  - id: p1-c01-086
    ru: надо надеть кожаные калоши, которые оставляются у дверей. Иначе придется идти в одних чулках.
    en_legacy: We’ll only have to put leather galoshes on them … Otherwise, we would have to stay in our bare feet
  - id: p1-c01-117
    ru: Надевай эти длинные чулки и туфли
    en_legacy: Put on these long socks and shoes
  en:
    term: galoshes; stockings (в одних чулках — in our stockinged feet); shoes
    legacy: galoshes; bare feet (ошибка); socks
    avoid:
    - bare feet (для «в одних чулках»)
    - socks (для «длинные чулки»)
    status: proposed
- id: brosh
  ru: брошь / булавка
  sense: драгоценная брошь-булавка, которой закалывают чалму над лбом (подарки Али)
  tier: secondary
  first_seen: p1-c01-098
  evidence:
  - id: p1-c01-098
    ru: Прекрасной работы брошь с крупным выпуклым рубином и несколькими бриллиантами
    en_legacy: A fastener of excellent work with a prominent, large ruby and several brilliants
  - id: p1-c01-105
    ru: Этими булавками мы заколем наши чалмы над самым лбом.
    en_legacy: We will buckle these fasteners on our turbans above our foreheads.
  - id: p1-c01-123
    ru: большая бриллиантовая брошь, изображавшая павлина
    en_legacy: the brilliant fastener which portrayed the peacock
  en:
    term: brooch (брошь); turban pin (булавка)
    legacy: 'fastener (p1-c01: 5 раз; ч. II — 8)'
    avoid:
    - fastener
    status: proposed
- id: brilliant
  ru: бриллиант
  sense: огранённый алмаз
  tier: secondary
  first_seen: p1-c01-098
  counts:
    p1: 26
    p2: 25
    p3: 4
  note: brilliants не ошибка (устар. «бриллиант»), но звучит как калька; diamonds — естественно. Вкусовая правка — на усмотрение
    редактора.
  evidence:
  - id: p1-c01-102
    ru: Оттуда сверкнули крупные бриллианты в форме треугольника
    en_legacy: Large brilliants laid out in a triangle began to glitter in it
  en:
    term: brilliants
    legacy: brilliants 40, diamonds 5 (в связях)
    avoid: []
    status: proposed
  question: brilliants (старый EN, 40; устар. «бриллиант», не ошибка) или diamonds (естественнее)? Запись признаёт правку
    вкусовой, поэтому по §9.2 п.6 рабочий вариант — brilliants; diamonds — предложение владельцу.
- id: dragotsennosti#pilot
  ru: рубин / изумруд / жемчуг / перстень / платиновая оправа / футляр / свёрток
  sense: подарки Али (p1-c01-094–103)
  tier: secondary
  first_seen: p1-c01-094
  evidence:
  - id: p1-c01-103
    ru: перстень с таким же овальным выпуклым изумрудом в простой платиновой оправе
    en_legacy: a ring lying in the smaller case, which had the same emerald set in the platinum frame
  - id: p1-c01-094
    ru: и он подал мне свёрток и футляр
    en_legacy: and he gave me a packet and a case
  en:
    term: ruby; emerald; pearls; ring; platinum setting; case; parcel
    legacy: ruby, emerald, pearls, ring, platinum frame, case, packet
    avoid:
    - frame (для оправы)
    status: proposed
- id: byuro
  ru: бюро
  sense: письменный стол-конторка с ящиками
  tier: secondary
  first_seen: p1-c01-102
  counts:
    p1: 2
    p2: 0
    p3: 0
  note: writing-table не ошибка; bureau точнее (у бюро ящики, что и важно в сцене).
  evidence:
  - id: p1-c01-108
    ru: брат выдвинул ящик бюро
    en_legacy: he pulled out one of the drawers of his writing-table
  en:
    term: writing-table
    legacy: writing-table — 2
    avoid: []
    status: proposed
  question: writing-table (старый EN, не ошибка) или bureau (у бюро ящики, что важно в сцене p1-c01-108)? У writing-table
    тоже бывают ящики, довод слабый; по §9.2 п.6 рабочий вариант — writing-table, bureau — предложение владельцу.
- id: papirosnaya-bumaga
  ru: папиросная бумага
  sense: тончайшая бумага (сравнение для ткани халата)
  tier: secondary
  first_seen: p1-c01-100
  evidence:
  - id: p1-c01-100
    ru: похожей на белую замшу, но по тонкости равной папиросной бумаге
    en_legacy: similar to the white suede and it was finer than the paper of cigarettes
  en:
    term: cigarette paper
    legacy: the paper of cigarettes
    avoid:
    - the paper of cigarettes
    status: proposed
- id: grim
  ru: грим / гримёр / любительские спектакли / любитель-актёр / артист
  sense: театральные реалии сцены переодевания
  tier: secondary
  first_seen: p1-c01-090
  evidence:
  - id: p1-c01-109
    ru: что играешь в любительских спектаклях
    en_legacy: that you were playing in amateurish performances
  - id: p1-c01-112
    ru: как заправский гримёр
    en_legacy: like an experienced make-up man
  - id: p1-c01-131
    ru: — Вы отличный артист, — едва улыбнувшись, сказал Али.
    en_legacy: “You are an excellent artist,” Ali told me
  en:
    term: make-up; make-up artist; amateur theatricals; amateur actor; actor (для «артист» о сцене)
    legacy: make-up man; amateurish performances; artist
    avoid:
    - amateurish (пренебрежительно)
    - artist (для «артист» — актёр)
    status: proposed
- id: ryazhenyy
  ru: ряженый
  sense: переодетый в маскарадный костюм («разве мы пойдём туда ряжеными?»)
  tier: secondary
  first_seen: p1-c01-076
  evidence:
  - id: p1-c01-076
    ru: — Как, — вскричал я с удивлением, — разве мы пойдём туда ряжеными?
    en_legacy: “Are we going there like to a masquerade?”
  en:
    term: in fancy dress (ряженый — someone in fancy dress)
    legacy: like to a masquerade (076, 077, 081)
    avoid:
    - like to a masquerade
    status: proposed
- id: bazar
  ru: базар / лавка / торговые ряды / торговые галереи / прилавок
  sense: восточный рынок и его лавки
  tier: secondary
  first_seen: p1-c01-003
  counts:
    p1: 12
    p2: 1
    p3: 6
  evidence:
  - id: p1-c01-007
    ru: бродил один в огромных торговых галереях с расписными столбами и маленькими восточными ресторанами-кухнями
    en_legacy: walk about the huge trade galleries with their many-coloured pillars and little Eastern restaurants-kitchens
  - id: p1-c01-008
    ru: бродя рассеянно от лавки к лавке
    en_legacy: I was lounging about from one shop to another
  - id: p1-c01-024
    ru: И купец достал из-под прилавка чудесный розового тона халат
    en_legacy: The trader pulled an excellent oriental robe with reddish hues out of his stall.
  en:
    term: market; лавка — shop; торговые галереи — covered arcades; торговые ряды — the market rows; прилавок — counter; ресторан-кухня
      — eating-house; расписные — painted
    legacy: market (19 из 19); shop 3 / stall 1; trade galleries; stall (для «прилавка»); restaurants-kitchens
    avoid:
    - restaurants-kitchens
    - stall (для «прилавок»)
    status: proposed
  question: 'базар — market (старый EN, не ошибка) или bazaar (колорит Средней Азии)? Рекомендация: оставить market по §9.2
    п.6; bazaar — если владелец хочет колорит.'
- id: mechet
  ru: мечеть
  tier: secondary
  first_seen: p1-c01-007
  evidence:
  - id: p1-c01-007
    ru: брат водил меня по городу, базару, мечетям
    en_legacy: my brother was taking me to the city, market and mosques
  en:
    term: mosque
    legacy: mosque
    avoid: []
    status: proposed
- id: zala
  ru: «зала» / гардеробная / «туалетная»
  sense: громкие названия комнат в скромном доме брата — авторская ирония (спальня «носила громкое название «зала»»; денщик
    «важно зовёт» гардеробную «туалетной»)
  tier: secondary
  first_seen: p1-c01-005
  note: 'toilette room — не английское сочетание, читатель услышит toilet room (уборную): ложная шутка, которой нет в RU;
    robing-room — пышное название (комнаты облачения судей и духовенства), ирония сохраняется'
  evidence:
  - id: p1-c01-005
    ru: которая носила громкое название «зала»
    en_legacy: although up to now it was loudly called the sitting-room
  - id: p1-c01-075
    ru: заглянем-ка в «туалетную», как важно зовёт денщик гардеробную
    en_legacy: let’s go to my dressing-room
    note: шутка про денщика опущена
  en:
    term: «зала» — the grand name ‘the salon’; гардеробная — dressing-room; «туалетная» — ‘the robing-room’, as my orderly
      grandly calls the dressing-room
    legacy: sitting-room (ирония потеряна); dressing-room (шутка опущена)
    avoid:
    - loudly called
    - toilette room
    status: proposed
- id: vannaya-v-sadu
  ru: ванная комната (в саду, из циновок и брезента)
  sense: самодельная купальня/душевая во дворе
  tier: secondary
  first_seen: p1-c01-069
  evidence:
  - id: p1-c01-069
    ru: умылись в ванной комнате, устроенной прямо в саду из циновок и брезента
    en_legacy: we washed ourselves in the lavatory which was made of mats and tarpaulin in the yard
  en:
    term: bathroom («we washed in the bathroom, rigged up right in the garden out of matting and canvas»)
    legacy: lavatory
    avoid:
    - lavatory (в британском — уборная)
    - washroom (эвфемизм уборной)
    status: proposed
- id: ekipazh
  ru: экипаж / пролётка / бричка / телега
  sense: конные повозки процессии у дома Али (p1-c01-046–055) и пролётка незнакомцев (011)
  distinguish: пролётка — лёгкий открытый рессорный экипаж (у Али — «изящная», с вороным конём); бричка — лёгкая полуоткрытая
    повозка («старая»); телега — простая крестьянская повозка; экипаж — общее
  tier: secondary
  first_seen: p1-c01-011
  counts:
    p1: 11
    p2: 0
    p3: 0
  evidence:
  - id: p1-c01-011
    ru: незнакомцы уже были в пролётке и отъезжали от базара
    en_legacy: were already sitting in their light carriage and moving away from the market
  - id: p1-c01-050
    ru: Это была изящная пролётка, запряжённая прекрасным вороным конём
    en_legacy: It was an elegant calash, harnessed by an excellent black horse.
  - id: p1-c01-047
    ru: в какой-то старой бричке, ехал старик
    en_legacy: An old man was bringing two elegant suitcases in the old light carriage after them.
  - id: p1-c01-046
    ru: Первой шла простая телега.
    en_legacy: The first a simple cart was rolling.
  en:
    term: экипаж — carriage; пролётка — droshky; бричка — britzka; телега — cart
    legacy: 'пролётка: light carriage / calash / coach (разнобой в одной сцене: 011, 050, 052, 055); бричка: light carriage
      5 из 8; телега: cart'
    avoid:
    - calash
    - light carriage (одинаково для пролётки и брички)
    status: proposed
  question: 'droshky / britzka (точные заимствования) или описательные open carriage / old trap? Рекомендация: droshky и britzka
    — обе есть в англ. словарях и в переводах русской классики; главное — развести два вида повозок, которые старый EN путает.'
- id: vorota
  ru: ворота / калитка / сад, обнесённый стеной
  tier: secondary
  first_seen: p1-c01-032
  evidence:
  - id: p1-c01-032
    ru: очень большой сад, обнесённый высокой кирпичной стеной … даже ворота никогда не открываются
    en_legacy: a big garden, fenced with a high brick wall … and even the gates didn’t open at least once
  en:
    term: gates; wicket gate; a garden enclosed by a high brick wall
    legacy: gates
    avoid: []
    status: proposed
- id: sgovor
  ru: сговор
  sense: сватовство, договорённость о браке («Будет сговор, пойдёт замуж»)
  tier: secondary
  first_seen: p1-c01-033
  evidence:
  - id: p1-c01-033
    ru: Приедет сестра Али Махмуд. Будет сговор, пойдёт замуж.
    en_legacy: Ali Machmed’s sister is coming. She has agreed to marry somebody.
  en:
    term: betrothal (there will be a betrothal)
    legacy: She has agreed to marry somebody (смысл сдвинут)
    avoid: []
    status: proposed
- id: sovershennoletie
  ru: совершеннолетие
  sense: достижение возраста зрелости (подарки «от Наль в день её совершеннолетия»)
  tier: secondary
  first_seen: p1-c01-094
  note: в p1-c01-104 старый EN ломает синтаксис («this is some Nal’s majority») — это правка фразы, а не термина
  evidence:
  - id: p1-c01-094
    ru: принять их как подарок от Наль в день её совершеннолетия
    en_legacy: to accept it as the present on the occasion of Nal’s majority
  - id: p1-c01-104
    ru: — Вот так совершеннолетие Наль!
    en_legacy: “Well, this is some Nal’s majority!”
  en:
    term: majority (Nal’s majority)
    legacy: majority
    avoid: []
    status: proposed
  question: majority (старый EN, юридически точное «совершеннолетие», не ошибка) или coming of age (естественнее в речи)?
    Довод за замену — только естественность, поэтому по §9.2 п.6 рабочий вариант — majority; coming of age — предложение владельцу.
- id: religioznyy-pokhod
  ru: религиозный поход
  sense: организованная травля/кампания фанатиков против Али
  tier: secondary
  first_seen: p1-c01-068
  note: 'В том же блоке старый EN добавил «fighting against the enslavement of women and the entire nation» — в RU: «Но он
    всё так же ведёт свою линию». Добавление.'
  evidence:
  - id: p1-c01-068
    ru: против него теперь собираются поднять религиозный поход
    en_legacy: I heard that a massacre is being organized against him
  en:
    term: a religious campaign (a holy war against him — сильнее, не рекомендую)
    legacy: massacre
    avoid:
    - massacre (резня — преувеличение)
    status: proposed
- id: versta
  ru: верста
  sense: русская мера длины (≈1,07 км)
  tier: secondary
  first_seen: p1-c01-067
  evidence:
  - id: p1-c01-067
    ru: как я устал, точно прошёл вёрст двадцать!
    en_legacy: as if I had walked twenty versts.
  en:
    term: verst
    legacy: versts
    avoid: []
    status: proposed
- id: rezhisser
  ru: режиссёр
  tier: secondary
  first_seen: p1-c01-071
  evidence:
  - id: p1-c01-071
    ru: что любой режиссёр мог бы позавидовать их фантазии
    en_legacy: that any artistic director could envy their fantasies
  en:
    term: stage director
    legacy: artistic director
    avoid:
    - producer (современный читатель поймёт как «продюсер»)
    status: proposed
- id: moy-bog#interjection
  ru: Мой Бог / Боже / Господи
  sense: восклицание
  tier: core
  first_seen: p1-c01-080
  counts:
    p1: 8
    p2: 13
    p3: 9
  evidence:
  - id: p1-c01-080
    ru: — Мой Бог, — сказал я
    en_legacy: “Oh, my god,” I was unable to remain still
  - id: p2-c01-143
    ru: — Господи, как вы прекрасны
    en_legacy: “God, how beautiful you are,”
  en:
    term: «Мой Бог», «Боже» — My God; «Господи» — Good Lord (с прописной)
    legacy: Oh, my god (строчная, p1-c01-080); «Господи» → Lord 23, God 11 (в связях)
    avoid:
    - god со строчной в восклицании
    status: proposed
- id: pomilui#interjection
  ru: помилуй
  sense: разговорное «сделай милость, пожалей» (Левушка брату)
  tier: secondary
  first_seen: p1-c01-088
  evidence:
  - id: p1-c01-088
    ru: Помилуй, Николушка, иди уж лучше один
    en_legacy: Have pity on me. Nikolushka, you better go alone
  en:
    term: have pity (Have pity on me)
    legacy: Have pity on me
    avoid: []
    status: proposed
  question: 'Have pity on me (старый EN, не ошибка — исправить только разрыв «Have pity on me. Nikolushka») или for pity’s
    sake (разговорнее)? Рекомендация по §9.2 п.6 — старый вариант. have mercy не брать как рабочий вариант: в поучениях mercy
    — «милосердие»; в бытовых идиомах (poshchada) mercy допустимо, но здесь старый вариант верен.'
- id: srednyaya-aziya
  ru: Средняя Азия (среднеазиатский торговый город)
  tier: secondary
  first_seen: p1-c01-003
  evidence:
  - id: p1-c01-003
    ru: в среднеазиатский большой торговый город
    en_legacy: to one big industrial city in the Central Asia
  en:
    term: Central Asia (a large trading city in Central Asia)
    legacy: the Central Asia; «торговый» → industrial
    avoid:
    - the Central Asia
    - industrial (для «торговый»)
    status: proposed
- id: toponyms#p1-c01
  ru: Багдад / Петербург / Персия / Россия / Англия / Азия / Европа / Восток / Гималаи / Везувий
  sense: топонимы p1-c01 (Багдад — в мечтах рассказчика 007; Петербург 023; Персия, Россия 029; Англия 015; Азия и Европа
    068; Восток 105; Гималаи 105; Везувий 080)
  tier: secondary
  first_seen: p1-c01-007
  counts:
    p1: 25
    p2: 4
    p3: 1
  evidence:
  - id: p1-c01-023
    ru: Наверное, друзьям в Петербурге посылал.
    en_legacy: He must have sent them to his friend to Petersburg.
  - id: p1-c01-105
    ru: сам он родом откуда-то из глубин Гималаев
    en_legacy: He is descended from somewhere deep in the Himalayas
  - id: p1-c01-080
    ru: можно почувствовать себя в жерле Везувия
    en_legacy: you can feel like being in the crater of Vesuvius
  en:
    term: Baghdad; Petersburg (как в RU и старом EN, 29 из 30); Persia; Russia; England; Asia; Europe; the East; the Himalayas;
      Vesuvius
    legacy: совпадает
    avoid: []
    status: proposed
- id: allusions#arabian-nights
  ru: Алладин с волшебной лампой / Гарун-аль-Рашид
  sense: аллюзии на «Тысячу и одну ночь» (RU пишет «Алладин» — авторская орфография)
  tier: secondary
  first_seen: p1-c01-007
  evidence:
  - id: p1-c01-007
    ru: проходит Алладин с волшебной своей лампой или бродит никем неузнаваемый Гарун-аль-Рашид
    en_legacy: Aladdin with his magic lamp would come out from somewhere, or not recognized by anybody Harun al-Rashid would
      march past
  en:
    term: Aladdin; Harun al-Rashid
    legacy: Aladdin; Harun al-Rashid
    avoid: []
    status: proposed
- id: m-skiy-polk
  ru: М-ский полк
  sense: полк брата, скрытый под буквой
  tier: secondary
  first_seen: p1-c01-003
  note: см. initials#abbreviated
  evidence:
  - id: p1-c01-003
    ru: капитану М-ского полка
    en_legacy: the captain of the regiment N
  en:
    term: the M— Regiment
    legacy: the regiment N (буква заменена)
    avoid:
    - regiment N
    status: proposed
- id: kapitanskiy-mostik
  ru: капитанский мостик
  tier: secondary
  first_seen: p1-c12-040
  counts:
    p1: 4
    p2: 0
    p3: 17
  note: the captain’s bridge (старый EN, p1-c12-040) — тоже допустимо, не ошибка
  evidence:
  - id: p1-c12-040
    ru: Мы добрались до капитанского мостика с огромным трудом.
    en_legacy: We reached the captain’s bridge with great difficulty.
  en:
    term: the bridge
    legacy: captain’s bridge; bridge 17 в связях
    avoid: []
    status: proposed
- id: rubka
  ru: (капитанская) рубка
  sense: надстройка на мостике с рулевым колесом
  tier: secondary
  first_seen: p1-c12-042
  counts:
    p1: 4
    p2: 0
    p3: 1
  evidence:
  - id: p1-c12-042
    ru: нас прижало к стенкам капитанской рубки
    en_legacy: It pressed us to the walls of the wheelhouse
  - id: p1-c12-045
    ru: Я был прижат к рубке таким сильным ветром
    en_legacy: I was squeezed into the corner by the strong wind
    note: 'annot. p1-c12-045: рубка → угол'
  en:
    term: wheelhouse
    legacy: wheelhouse 3; corner (p1-c12-045)
    avoid:
    - corner
    status: proposed
- id: shturval
  ru: штурвал / рулевое колесо / руль
  sense: колесо управления рулём (в тексте три слова об одном предмете)
  tier: secondary
  first_seen: p1-c12-043
  evidence:
  - id: p1-c12-043
    ru: И. с матросом бросились к рулевому колесу
    en_legacy: I. and the sailor dashed to the wheel
  - id: p1-c12-053
    ru: налёг всем телом на руль … который двинул штурвал так, как хотел капитан
    en_legacy: leant on the wheel with his entire body … he turned the wheel exactly so as the captain wanted it to
  en:
    term: the wheel (the helm — для разнообразия, где уместно)
    legacy: wheel
    avoid: []
    status: proposed
- id: nos-sudna
  ru: нос (судна)
  tier: secondary
  first_seen: p1-c12-053
  note: Отчёт §6.3 п.9, §6.6 (L2 p1-c12-054).
  evidence:
  - id: p1-c12-053
    ru: И пароход послушно повернулся носом вправо.
    en_legacy: And now the steamer turned obediently with its front to the right.
    note: 'annot.: fix — swung her bow to starboard'
  - id: p1-c12-054
    ru: судно вздрогнуло, нос задрался вверх, точно на качелях
    en_legacy: the ship trembled, its spike rose upward as on the swing
  en:
    term: bow
    legacy: front (053), spike (054 — дважды)
    avoid:
    - front
    - spike
    status: proposed
- id: bort-korma
  ru: борт / корма (кормовая часть) / палуба
  tier: secondary
  first_seen: p1-c12-054
  note: существительное broadside значит бортовой залп орудий; корректно только наречное broadside (on)
  evidence:
  - id: p1-c12-054
    ru: Если бы вся эта масса ударила нам в борт … вся тяжесть обрушилась на его кормовую часть
    en_legacy: If this mountain had hit the ship’s side … the whole weight of the water fell on its stern
  en:
    term: side (удар в борт — had struck us broadside on); stern; deck
    legacy: ship’s side; stern; deck
    avoid: []
    status: proposed
- id: kren
  ru: крен / «пароход ляжет»
  sense: наклон судна на борт; «ляжет, чтобы уже не встать» — опрокинется
  tier: secondary
  first_seen: p1-c12-049
  note: 'в морском английском list — устойчивый крен от смещения груза или воды, мгновенный наклон на волне в шторм — roll
    (или heel): «One more roll like that and she’ll go over and never right herself.»'
  evidence:
  - id: p1-c12-049
    ru: — Ещё один такой крен, и пароход ляжет, чтобы уже не встать
    en_legacy: “One more such heeling over of the ship, and the steamer will fall on its side, so that it would never rise
      again,”
    note: 'annot. fix: One more list like that and she’ll go over and never right herself'
  en:
    term: roll; «ляжет» — go over, never right herself
    legacy: heeling over; fall on its side
    avoid: []
    status: proposed
- id: pomoshnik-kapitana
  ru: помощники (капитана)
  tier: secondary
  first_seen: p1-c12-042
  note: officers — где речь о командном составе в целом
  evidence:
  - id: p1-c12-043
    ru: которое капитан и помощники уже не могли удерживать втроём
    en_legacy: because the captain with his assistants were unable to hold it
    note: 'annot. fix: the captain and his two mates'
  en:
    term: mates (the first / second mate)
    legacy: assistants (87 в связях со всеми «помощник*», не только морскими)
    avoid:
    - assistants (о помощниках капитана)
    status: proposed
- id: parokhod-sudno
  ru: пароход / судно
  sense: морской пароход; в английском судно — she/her
  tier: secondary
  first_seen: p1-c12-043
  evidence:
  - id: p1-c12-054
    ru: судно неминуемо опрокинулось бы … пароход прорезал брюхо водяной горы
    en_legacy: then it would have capsized inevitably … the steamer pierced through the gigantic mass of the water with its
      spike
    note: 'отчёт §6.6: судно везде her'
  en:
    term: steamer (пароход); ship (судно); местоимение she/her
    legacy: steamer, ship; it/its
    avoid:
    - it/its (о судне)
    status: proposed
- id: matros-verzila
  ru: матрос-верзила
  sense: рослый, здоровенный матрос (постоянное обозначение персонажа в части I)
  tier: secondary
  first_seen: p1-c11-075
  counts:
    p1: 70
    p2: 0
    p3: 0
  note: 'текст подчёркивает рост и ловкость: «Возле меня выросла высокая тень — это был наш матрос-верзила» (p1-c11-101),
    «этот верзила так же летал по лестницам» (p1-c11-076); lanky («долговязый и нескладный») и hulking («громоздкий, неуклюжий»)
    этому противоречат, а lanky, повторённое 70 раз, станет комичным; strapping — рослый и крепкий, слегка старомодно. Допустимо
    разнообразить: our big sailor, the giant of a sailor'
  evidence:
  - id: p1-c12-042
    ru: как матрос-верзила что-то крикнул, рванул меня вперёд
    en_legacy: how the clumsy sailor screamed something and yanked me forward
    note: annot. p1-c12-042; отчёт §5
  en:
    term: the strapping sailor
    legacy: clumsy — 67 из 70 в связях (78 clumsy в тексте ч. I)
    avoid:
    - clumsy
    - lanky
    - hulking
    status: proposed
- id: nyanka-matros
  ru: нянька-матрос
  sense: шутливое — матрос, опекающий Левушку
  tier: secondary
  first_seen: p1-c12-041
  evidence:
  - id: p1-c12-041
    ru: валился на свою няньку-матроса
    en_legacy: I fell on my “nurse”
  en:
    term: my “nurse”
    legacy: my “nurse”
    avoid: []
    status: proposed
  question: my “nurse” (старый EN, шутка сохранена, «матрос» ясен из контекста) или my sailor-nursemaid (ближе к составному
    RU)? Довод за замену стилистический; по §9.2 п.6 рабочий вариант — старый.
- id: korobochka-pilyuli
  ru: коробочка (Флорентийца) / пилюли
  tier: secondary
  first_seen: p1-c12-044
  evidence:
  - id: p1-c12-044
    ru: из зелёной коробочки Флорентийца, пилюли всем
    en_legacy: quickly pull a pill for everybody out of the green Florentian’s box
  - id: p1-c12-046
    ru: Я вынул пилюли
    en_legacy: I pulled the pills out of my first-aid kit easily
    note: 'annot. p1-c12-046 major: подмена предмета'
  en:
    term: the little green box; pills
    legacy: box; first-aid kit (ошибка, 046)
    avoid:
    - first-aid kit
    status: proposed
- id: posazhennaya-mat
  ru: посаженная мать / посаженный отец
  sense: в свадебном обряде — заменяющие родителей невесты/жениха (у Наль нет матери; посаженный отец ведёт невесту в церковь,
    p2-c18-087)
  distinguish: 'не подружка невесты и не сват: matron of honour = замужняя подружка; matchmaker = сват'
  tier: secondary
  first_seen: p2-c01-256
  counts:
    p1: 0
    p2: 4
    p3: 1
  evidence:
  - id: p2-c01-256
    ru: А жена будет посаженной матерью, как полагается по здешним обычаям.
    en_legacy: while my wife would become the matron of honour according to our custom
    note: annot. major; отчёт §4.2
  - id: p2-c18-087
    ru: по русскому обычаю невесту в церковь везёт посаженный отец
    en_legacy: according to the Russian custom, the bride goes to the orthodox church with her matchmaker
  en:
    term: stand in for the bride’s mother / father; посаженный отец, ведущий невесту — give the bride away
    legacy: matron of honour (1); matchmaker (3)
    avoid:
    - matron of honour
    - matchmaker
    status: proposed
- id: podruzhki
  ru: подружки (невесты) / венчаться / свадьба / невеста / жених
  sense: свадебная лексика эпизода
  tier: secondary
  first_seen: p2-c01-256
  evidence:
  - id: p2-c01-256
    ru: решили немедленно обновить свои белые платья и быть вам завтра подружками
    en_legacy: they decided to renew their white dresses instantly and to become the bridesmaids
  - id: p2-c01-265
    ru: Я не могу понять, кто из вас отец, а кто жених. Вы оба женихи, по-моему
    en_legacy: I cannot understand who of you is her father and who is her fiancé. According to me, both of you are grooms
  en:
    term: bridesmaids; be married; wedding; bride; bridegroom (накануне свадьбы; fiancé — до неё)
    legacy: bridesmaids; wed; wedding; bride; fiancé / grooms
    avoid: []
    status: proposed
- id: vizitnye-kartochki
  ru: визитные карточки
  tier: secondary
  first_seen: p2-c01-252
  evidence:
  - id: p2-c01-252
    ru: Взяв визитные карточки гостей, слуга ввёл их в гостиную
    en_legacy: Having taken the visiting-cards from the guests, the servant invited them to the sitting-room
  en:
    term: visiting-cards
    legacy: visiting-cards
    avoid: []
    status: proposed
    note: написание через дефис — старое британское, не ошибка (§9.2 п.6); visiting cards — допустимо по решению стайлгайда
- id: gostinaya
  ru: гостиная
  sense: парадная комната для приёма гостей (в английском доме пастора)
  tier: secondary
  first_seen: p2-c01-252
  counts:
    p1: 7
    p2: 11
    p3: 2
  evidence:
  - id: p2-c01-252
    ru: слуга ввёл их в гостиную, тоже старинную, с огромным камином
    en_legacy: the servant invited them to the sitting-room which also was old-fashioned, with the big fireside
  en:
    term: sitting-room
    legacy: sitting-room 19 из 20
    avoid: []
    status: proposed
  question: 'drawing-room для гостиной пастора — правка по эпохе, не по ошибке: по §9.2 п.6 рабочий вариант — sitting-room
    (старый EN, 19 из 20). Предложение владельцу: drawing-room в части II (парадная комната английского дома того времени).'
- id: kamin
  ru: камин
  tier: secondary
  first_seen: p1-c02-101
  counts:
    p1: 24
    p2: 24
    p3: 4
  note: fireside = место у огня; «сидеть у камина» — by the fire / at the fireside допустимо.
  evidence:
  - id: p2-c01-252
    ru: с огромным камином
    en_legacy: with the big fireside
    note: annot. p2-c01-252; отчёт §6.3 п.9
  en:
    term: fireplace
    legacy: fireside 41, hearth 8 (в связях); fireplace 0
    avoid:
    - fireside (для самого камина)
    status: proposed
- id: zapad-vostok
  ru: западный / на Востоке
  sense: противопоставление Запада и Востока в речи Наль и Флорентийца
  tier: secondary
  first_seen: p2-c01-253
  evidence:
  - id: p2-c01-253
    ru: Удивительно, как красиво в западных домах. … не то, что у нас на Востоке, отец.
    en_legacy: It is amazing how it is beautiful inside of European houses … not like in our Oriental families, father.
  en:
    term: Western (houses); in the East
    legacy: European; Oriental families
    avoid:
    - European (для «западный»)
    status: proposed
- id: venetsianka
  ru: венецианка / венецианское происхождение
  tier: secondary
  first_seen: p2-c01-259
  evidence:
  - id: p2-c01-259
    ru: Моя жена венецианка … не имеет никакой возможности претендовать на венецианское происхождение
    en_legacy: My wife is descended from Venice … she doesn’t have any possibility to claim her Venetian descent
  en:
    term: a Venetian; Venetian descent
    legacy: descended from Venice; Venetian descent
    avoid: []
    status: proposed
- id: papa#address
  ru: папа / мамаша / папаша / отец
  sense: семейные обращения и шутливые «в мамашу», «в папашу»; Наль называет Флорентийца «отец»
  tier: core
  first_seen: p2-c01-253
  note: 'для шутливого тона «в мамашу» допустимо her mama / her papa. Довод о различении: в одной сцене RU различает «папа»
    (Алиса пастору, p2-c01-260) и «отец» (Наль Флорентийцу, p2-c01-253), а старый EN даёт father обоим — поэтому Papa, а не
    father.'
  evidence:
  - id: p2-c01-260
    ru: — О папа, — заразительно засмеялась младшая
    en_legacy: “Oh, father,” the girl was laughing infectiously
  - id: p2-c01-262
    ru: — Папа был прав.
    en_legacy: “My father was right
  - id: p2-c01-259
    ru: не только вся в мамашу … вся в папашу
    en_legacy: she’s not only like her mummy … she’s all like her daddy
  - id: p2-c01-253
    ru: не то, что у нас на Востоке, отец.
    en_legacy: not like in our Oriental families, father.
  en:
    term: Papa (обращение дочери, британское начала XX в.); «в мамашу / в папашу» — takes after her mother / her father; отец
      (Наль → Флорентийцу) — Father
    legacy: father / my father / mummy / daddy
    avoid:
    - mummy, daddy (детская речь; звучит в устах пастора неуместно)
    status: proposed
  question: 'Papa или Father для «папа» Алисы? Рекомендация: Papa — передаёт домашнюю нежность RU и эпоху.'
- id: dama-sveta
  ru: дамы света
  sense: светские дамы (свет = высшее общество)
  distinguish: свет#society ≠ свет#light — многозначное слово (TRANSLATION-PROCESS §9.2 п.4)
  tier: secondary
  first_seen: p2-c01-261
  evidence:
  - id: p2-c01-261
    ru: всё же походили на дам света, радушно принимающих приятных, но чужих людей
    en_legacy: they looked more like the society ladies who were accepting kind, but strange people with hospitality
  en:
    term: society ladies
    legacy: society ladies
    avoid: []
    status: proposed
- id: reverans
  ru: реверанс
  tier: secondary
  first_seen: p2-c01-264
  evidence:
  - id: p2-c01-264
    ru: низко присела в реверансе
    en_legacy: made a deep curtsy to both men
  en:
    term: curtsy
    legacy: curtsy
    avoid: []
    status: proposed
- id: zamorskaya-krasavitsa
  ru: заморская красавица
  tier: secondary
  first_seen: p2-c01-260
  evidence:
  - id: p2-c01-260
    ru: ты приехал таким влюблённым в заморскую красавицу
    en_legacy: you came back so in love with the beauty from oversea
  en:
    term: the beauty from overseas
    legacy: the beauty from oversea
    avoid:
    - from oversea
    status: proposed
- id: realia#cal-4
  ru: дом на Востоке / кров Общины / балкон / пальмы / свирель / розы и гвоздики
  tier: secondary
  first_seen: p3-c01-067
  note: pinks — старый EN, не ошибка (§9.2 п.6); carnations — допустимая замена по решению владельца
  evidence:
  - id: p3-c01-084
    ru: очень отдаленный звук свирели, аромат роз и гвоздик
    en_legacy: a very distant voice of the little pipe, the aroma of roses and pinks
  - id: p3-c01-067
    ru: Сегодня ты вступил в мой дом на Востоке.
    en_legacy: Today you entered my home in the East.
  en:
    term: my home in the East; the shelter of the Community; balcony; palms; reed pipe; roses and pinks
    legacy: home in the East; shelter/roof; balcony; palms; little pipe; pinks
    avoid:
    - little pipe
    status: proposed
- id: verse-terms#cal-5
  ru: странник / счастливая доля / святыня / красота / песнь любви и воли / гимн торжествующей любви / русская песня
  sense: образы песни (p1-c20-213 — перевод заново, DEC-026) и обрамления
  tier: secondary
  first_seen: p1-c20-212
  note: 'образы одной песни (перевод заново, DEC-026: рифмованный и нерифмованный варианты). В песне допустимы варианты по
    рифме (a blessed lot; my holy of holies; freedom вместо will) — окончательно при переводе песни; «воля» в прозе — will
    (volya#will), так что противоречия с volya#will нет.'
  evidence:
  - id: p1-c20-213
    ru: Я только странник на земле.
    en_legacy: I’m only a wanderer of this earth.
  - id: p1-c20-213
    ru: Избранник я счастливой доли.
    en_legacy: 'My destiny is going like this:'
    note: строка утрачена (отчёт §4.2)
  - id: p1-c20-213
    ru: Моей святыне — красоте / Пою я песнь любви и воли.
    en_legacy: I’m weaving my song only for the saint Beauty / From my love, will and power.
    note: святыня → saint — ошибка
  - id: p1-c20-214
    ru: То была не просто песнь, а гимн торжествующей любви…
    en_legacy: That wasn’t a song anymore, but a hymn of victorious love…
  en:
    term: wanderer (on earth); a happy lot; my shrine — Beauty; a song of love and will; a hymn of triumphant love; a Russian
      song
    legacy: wanderer; —; saint Beauty; love, will and power; victorious love; sing in Russian
    avoid:
    - saint (для «святыня»)
    status: proposed
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
