# Разбор замечаний: ядро глоссария (этап 3)

Проверялся коммит `12fea09`. Внутреннее ревью (DEC-013, DEC-021) — три агента со свежим контекстом:
- `internal-evidence-20260927.json` — точность доказательств: сверены **все** 390 цитат glossary.yml и 100 characters.yml,
  ≈300 пар «цитата — ID» в тексте полей, 46 частот старого EN (34 замечания: 4 major, 30 minor);
- `internal-terminology-20260927.json` — согласованность и решения (20 замечаний: 9 major, 11 minor);
- `internal-language-20260927.json` — английский язык (35 замечаний: 7 major, 28 minor).

Выдуманных цитат нет; происхождение, на котором держатся вопросы об именах, подтверждено текстом (Флорентиец —
из Флоренции, Жанна — француженка, Лиза — русская, Бронский — чех, Игоро — румын, Уодсворды — англичане, Катарина —
венецианка). Разобрал: Claude (координатор). Решения: `accept`, `accept-modified`, `reject` — с причиной.

## Общие правила, введённые по итогам

1. **Рабочий вариант однозначен.** В `en.term` / `en.name` — ровно один вариант, равный рекомендации; альтернативы и
   сомнения — только в `question` или `note`; где выбор зависит от контекста — явный критерий в `note` (§9.2 п.2: «первый
   вариант держится», поэтому рабочий вариант должен быть проверяемым).
2. **По умолчанию — вариант старого перевода, если он не ошибочен** (§9.2 п.6). Где запись сама признаёт «не ошибка» или
   довод только вкусовой, `en.term` = старый вариант, новое — в `question`. Исключения — только с доводом о различении
   понятий (например, «купец» ≠ «торговец»).
3. **Имя без оснований в тексте не становится рабочим** (DEC-028): в `en.name` — вариант старого EN, предложение — в
   `question` (так уже было для Katherine, Obersvode, Saintger, Amedeo; теперь и для Wodsword).
4. **Имена в примерах glossary.yml — только по characters.yml.** Проверка `tools.glossary.check` теперь ловит форму из
   `en.avoid` персонажа в `en.term` глоссария.
5. **Цитаты сверяются с текстом абзаца автоматически.** `tools.glossary.check` ищет каждую RU-цитату `evidence` в тексте
   её абзаца по epub (куски между «…», «[…]», « / » — по отдельности). Это ловит систематический сдвиг ID на соседний
   абзац, который дало автовыравнивание (11 цитат).
6. **`first_seen` — первое вхождение именно этого значения**, а не первое совпадение основы слова.

## internal-evidence

| # | ID | Суть | Решение | Что сделать |
|---|---|---|---|---|
| e0 | anna | «мать Анна» (настоятельница, p3-c23…c33) слита с Анной Строгановой | accept | новая запись `mat-anna` (обращение «мать» → Mother, связь с nastoyatel#title); пересчитать anna |
| e1 | bodrost | цитата p3-c31-018 описывает ложную бодрость | accept | переписать довод: истинная — «благословение … Божественной Энергии и гармоничный труд» |
| e2 | svet | нет записи «свет» = мир («на свете», «тот свет») | accept | новая запись `svet#world` (world), вычесть из svet#light; «высший свет» — svet#society |
| e3–e13 | 11 записей | цитата на соседнем ID | accept | исправить ID (проверка теперь ловит) |
| e14 | — | нужна автоматическая сверка цитат с epub | accept | сделано в `tools.glossary.check` |
| e15–e18 | doktor, temnye-sily, stupen, osvobozhdenie, bozhestvennyi, brat#fellow | first_seen по основе, не по значению | accept | исправить (правило 6) |
| e19, e20 | zhizn#life-divine, formula#lyubimyi | старый EN есть, но не приведён | accept | добавить |
| e21–e25 | olga, andreeva, levushka, florentiets, illofillion | фактические неточности | accept | исправить; частоты I.’s и «I. I» — по пересчёту |
| e26 | nikolay | нет «Николушка», «брат-отец» | accept | добавить aliases |
| e27 | brat#sibling | И. — не двоюродный брат (легенда) | accept | исправить |
| e28 | vladyka#master | «лорд Бенедикт» ≈575, не ≈270 | accept | исправить |
| e29 | obshchina | цитата о «семье» переносная | accept | заменить опору (p3-c20-206 и др.) |
| e30 | dukh#spirit | счёт прописной 19; нет значений «духи» и «дух = мужество» | accept-modified | счёт исправить; `dukh#beings` (spirits) — отдельная запись; «дух = мужество» — идиома, в distinguish с вариантами (courage, heart) |
| e31 | zemlya | нет значения «земля» = земная жизнь | accept | новая запись `zemlya#earth` (earth, строчная) |
| e32 | dobro | «добро» = имущество посчитано в good | accept | distinguish, вычесть |
| e33 | verse-terms#cal-5 | противоречит volya#will | accept | в прозе «воля» → will; в песне — оба варианта по DEC-026, решение при переводе песни; противоречие снять |

## internal-terminology

| # | ID | Суть | Решение | Что сделать |
|---|---|---|---|---|
| t0 | vladyki-karm | довод «строчная в RU» неверен (прописная 18 из 25); lords сталкивается с «лордом» | accept | `Masters of karma` (старый EN), факты исправить; см. l8 |
| t1 | mat-anna | пропущен главный персонаж ч. III | accept | = e0 |
| t2 | mir#peace | правило не работает без «спокойствия» и «покоя» | accept | новые core-записи `spokoistvie` (calm) и `pokoy` (по значению; peace — только если владелец сольёт), решать вместе с mir#peace |
| t3 | miloserdie | mercy = прежде всего «пощада» | accept | новые записи `poshchada`, `zhalost`; в question — что mercy меняет ≈178 compassion и почему |
| t4 | wodsword | Wadsworth в en.name — рабочий вариант вопреки DEC-028 | accept | en.name = Wodsword; Wadsworth — только в question (правило 3) |
| t5 | knyaz#title и др. | имена в примерах ≠ characters.yml | accept | правило 4; исправить Senjer, Rettedly, Wodsword, Doctor I., Lisa, Tendly |
| t6 | tselesoobraznost | term противоречит рекомендации | accept | = l2 |
| t7 | bodrost, stupen, edinenie, tvorchestvo, zakonomernost, seryi-den, formula#bud-blagosloven | несколько вариантов или «(?)» в term | accept | правило 1 |
| t8 | formula#mir-tebe, muzhaysya, druzhok | верный старый вариант заменён по вкусу | accept | en.term = старый вариант (Peace to you, Be strong, my friend); новое — в question |
| t9 | kupets и др. | то же для реалий | accept | правило 2; kupets — довод о различении |
| t10 | zhizn#life-divine | рекомендация it/itself без доводов из текста за She | accept | добавить доводы (RU «Она» с прописной), рекомендацию пометить как стилистическую |
| t11 | vladyka#master | «выше Учителя» — толкование; Lord отвергнут выборочно | accept | обоснование лексическое (два слова RU — два слова EN; старый EN ≈350); согласовать с bog/vladyka |
| t12 | formula#nikto-ne-drug | прописная «Учитель» 4 : 3; вариант «не брат» | accept | зеркалить RU по месту или вопрос владельцу; note о «не брат» и D14 |
| t13 | podvig, nastavnik, sotrudnik | пропущены сквозные понятия | accept | новые core-записи |
| t14 | — | нет Санат Кумары, Маха-Чохана, Кумар, сестры Александры | accept | новые записи (имена — в characters.yml или glossary по виду) |
| t15 | olga | эпизодическая → secondary | accept | tier: secondary |
| t16 | vladyka#lord | два значения в одной записи | accept | `vladyka#ruler` (lord) и `vladyka#god` (Lord, связь с bog) |
| t17 | obersvoud, tendl и др. | разные правила для сходных случаев | accept | один общий вопрос владельцу о принципе «буквенное несоответствие RU»; варианты, включая Tendle (l18) |
| t18 | ali-mohammed | в реплике рассказчика «Магометы» — европейская форма | accept | note: в p1-c01-016 “both Mahomets?” |
| t19 | luch#ray | first_seen | accept | p3-c04-121 |

## internal-language

| # | ID | Суть | Решение | Что сделать |
|---|---|---|---|---|
| l0 | formula#bud-blagosloven | «Bless you» — ответ на чихание; «Be blessed» — американское церковное | accept | en.term `May you be blessed`; Bless you — в avoid; старый вариант — в question |
| l1 | svetly | Bright о людях и силах читается как «смышлёные» | accept-modified | эпитет перед людьми и силами — `of Light` (Brothers of Light, Powers of Light); название Братства — старое `Bright Brotherhood` с вопросом владельцу (vs Brotherhood of Light), §9.2 п.6 |
| l2 | tselesoobraznost | expediency = выгода | accept | `purposefulness`; expediency — в avoid |
| l3 | illofillion | Il.: I/l в рубленых шрифтах, «Doctor Ill» | accept | риски — в question; проверить в шрифтах пробной сборки (этап 4) до утверждения |
| l4, l5, l32, l33 | речь торговца | «one tall dark people» — расовое прочтение; «plenty people» — пиджин; в 034 сломаны правильные в RU фразы; «know him good» — американское просторечие; «Oy» — идишское | accept | переделать образцы: ошибки согласования, артикля, связки, инверсия; правильные фразы RU — правильные; Ay-ya; рекомендация — умеренная плотность |
| l6 | bodrost | vigorous нельзя делать обязательным для всех форм | accept | term vigour (сущ.); прилагательное и наречие — по контексту, критерий в note |
| l7 | seryi-den | «the grey day» читается как погода | accept | term `the plain grey day`; мн. ч. и варианты — в note |
| l8 | vladyki-karm | lords of karma — устоявшееся выражение | reject | сталкивается с «лордом» (t0); старый вариант последователен и не ошибочен; привычность в теософской литературе — не довод из текста романа |
| l9 | formula#privet-i-mir | greeting → greetings | accept | `Accept my greetings and my peace.` |
| l10 | formula#pozhatie | «handshake of vigour» натянуто | accept | `full of vigour and energy`; в p3-c01-078 — my friend |
| l11 | velikaya-zhizn | без артикля читается как имя | accept | `the Great Life` |
| l12 | mat-zhizni | «Мать Жизнь» (приложение) ≠ «Мать Жизни» | accept | разделить в note: the Mother of Life / the Great Mother Life |
| l13 | tvorchestvo | creativity — анахронизм | accept | `creative work` |
| l14 | zakonomernost | lawfulness = законность | accept | `conformity to law` |
| l15 | stupen | запрет level вредит беглости | accept-modified | term `stage` (ступень пути); step/rung — где образ лестницы; level не запрещать в идиомах — критерий в note |
| l16–l18 | address#ty-vy, knyaz#title, mister#title | имена ≠ characters.yml | accept | = t5; Tendle — в общий вопрос t17 |
| l19 | ledi#title | milady — Дюма | accept | `my lady` |
| l20 | sinyor#title | мн. ч. signore не узнается | accept | `the Galdoni ladies` |
| l21 | titul#honorific-styles | громоздко | accept | `I, a Serene Highness, demand …` |
| l22 | denshchik | batman — не разговорное | accept | исправить пометку; term orderly |
| l23 | zala | toilette room ≈ уборная | accept | `robing-room` |
| l24 | vannaya-v-sadu | washroom ≈ уборная | accept | `bathroom` |
| l25 | kren | крен на волне — roll | accept | `roll` |
| l26 | bort-korma | broadside — залп | accept | `broadside on` |
| l27 | matros-verzila | lanky 70 раз — комично и «тощий» | accept | `strapping` (рослый и крепкий) |
| l28 | ali-mahmud | the young Ali = «Али в молодости» | accept | `young Ali` без артикля |
| l29 | eta | Eta читается как греческая буква | accept-modified | en.name Eta (старый EN), Età — в question владельцу |
| l30 | sandra | Sandra — женское имя для англ. читателя | accept | note для стайлгайда (однозначные he/his при первых упоминаниях) |
| l31 | zeyhed | -ogly ≈ ugly | accept-modified | в общий вопрос о «х»: вариант -oglu; решает владелец |
| l34 | rezhisser | producer = продюсер | accept | `stage director` |
| — | общее | оксфордская запятая — отдельный вопрос | accept | в открытые вопросы стайлгайда (этап 4) |

## Что остаётся на внешнее ревью

- Независимая оценка английских вариантов (обе внутренние проверки — модели того же семейства).
- Вердикт по каждому термину (`agree` / `object` / `unsure`) — только внешние засчитываются для `secondary` (DEC-015);
  `core` после ревью утверждает владелец.
