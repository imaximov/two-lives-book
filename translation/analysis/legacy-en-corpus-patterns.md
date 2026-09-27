# Закономерности по корпусу старого EN (генерируется)

Файл создан `python -m tools.analysis.legacy_patterns`; не править вручную. Числа — вхождения в томе и на 10 000 слов
английского текста тома. RU — вхождения в оригинале соответствующей части (для сопоставления имён и титулов).
Для Vol3 — нижняя оценка (≈1% текста извлекается слитно). Примеры: страница PDF (с 1) и фрагмент.

| Том | Файл | sha256 | Слов EN |
|---|---|---|---|
| Vol1 (ч. I) | `sources/en-legacy/TwoLives-Vol1-2018-part1.pdf` | `7c96176a2c0cd47e…` | 235489 |
| Vol2 (ч. II) | `sources/en-legacy/TwoLives-Vol2-2021-part2.pdf` | `58329193cfbf7810…` | 231188 |
| Vol3 (ч. III) | `sources/en-legacy/New/TwoLives-Vol3.pdf` | `7b80b0a37d561663…` | 404048 |

## Имена и титулы

| Закономерность | Vol1 (ч. I) | Vol2 (ч. II) | Vol3 (ч. III) | RU (ч. I / II / III) |
|---|---|---|---|---|
| князь → duke | 319 (13.5) | 32 (1.4) | 3 (0.1) | 279 / 25 / 3 |
|  | Vol1 с.97: «…visited at one or another countess and which duke had invited them for tomorrow. I had never h…»<br>Vol1 с.141: «…ll about your behaviour to His Majesty grand duke Vladimir who will board our ship in the next…»<br>Vol2 с.157: «…s elegant and light step, his manners of the duke – and he seemed to himself to be a sickly, g…» | | | |
| князь → prince | 25 (1.1) | 7 (0.3) | 3 (0.1) | — |
|  | Vol1 с.105: «…m so intensely as though he was a fairy-tale prince and she was Cinderella. Having turned my eye…»<br>Vol1 с.106: «…re the huge ship, the eminent English “Black Prince” went down. Most of all I wanted to see the…»<br>Vol2 с.19: «…ly, he used to call the captain T. to be the prince of the fairy-tale. So long, uncle! I’m your…» | | | |
| Левушка → Lovushka | 284 (12.1) | 31 (1.3) | 212 (5.2) | 280 / 30 / 340 |
|  | Vol1 с.6: «…cast to my feet and suddenly I heard a cry. “Lovushka, where have you been? I was already about to…»<br>Vol1 с.7: «…inued. “You remind me of the little stubborn Lovushka who loved stunning everybody with his riddle…»<br>Vol2 с.6: «…for her in the corridor. The thoughts about Lovushka – his only close brother in arms of his life…» | | | |
| Левушка → Levushka/Lyovushka | 0 (0.0) | 0 (0.0) | 125 (3.1) | — |
|  | Vol3 с.302: «…which was coming nearer to us. “Here it is, Lyovushka, the first test about which I. was telling u…»<br>Vol3 с.303: «…er and said to me very silently. “Thank you, Lyovushka. A protest and dissatisfaction rose within m…» | | | |
| Флорентиец → Florentian | 358 (15.2) | 490 (21.2) | 146 (3.6) | 351 / 461 / 141 |
|  | Vol1 с.29: «…uest said. “I can assure you that I’m really Florentian, although I have been living in the East for…»<br>Vol1 с.31: «…I am the lord Benedict, but you can call me Florentian, like everyone is doing.”…»<br>Vol2 с.7: «…o be my friend and helper, but until we meet Florentian and we marry, I cannot tell you anything, ev…» | | | |
| Флорентиец → Florentine | 0 (0.0) | 0 (0.0) | 0 (0.0) | — |
|  |  | | | |
| Уоми → Vomi | 257 (10.9) | 83 (3.6) | 34 (0.8) | 253 / 81 / 34 |
|  | Vol1 с.160: «…e older, self-confident and restrained. “Sir Vomi, may your friends come in already?” the girl…»<br>Vol1 с.160: «…th. I was feeling totally ashamed, while sir Vomi, as Chava called my new friend, added, smili…»<br>Vol2 с.71: «…arrived to B., he became acquainted with sir Vomi and he found out from him that you were writ…» | | | |
| Уоми → Uomi/Oomi/Womi | 0 (0.0) | 0 (0.0) | 0 (0.0) | — |
|  |  | | | |
| Жанна → Joan | 429 (18.2) | 0 (0.0) | 6 (0.1) | 417 / 0 / 7 |
|  | Vol1 с.138: «…at your young heart will hear my entreaty, I Joan Moranjer remain always thankful to you.” I w…»<br>Vol1 с.138: «…couple of times, and I saw the face of poor Joan with the tears pouring from her eyes like pe…»<br>Vol3 с.94: «…li, dear captain James, Anna and Stroganoff, Joan, her children, the kind duke, the Turks, Cha…» | | | |
| Жанна → Jeanne/Jane | 0 (0.0) | 0 (0.0) | 0 (0.0) | — |
|  |  | | | |
| Алиса → Alyssa | 0 (0.0) | 869 (37.6) | 2 (0.0) | 0 / 814 / 2 |
|  | Vol2 с.23: «…exact her copy. Here’s the number two, Miss Alyssa Wodsword, she’s all like her daddy and, acco…»<br>Vol2 с.24: «…ng eyes, then one had to take a good look at Alyssa in order to evaluate her beauty. Her ash-col…»<br>Vol3 с.35: «…my story from him. He saw Nal and her friend Alyssa by whose beauty he was so surprised and capt…» | | | |
| Алиса → Alice | 0 (0.0) | 0 (0.0) | 0 (0.0) | — |
|  |  | | | |
| Али старший → the elder Ali | 0 (0.0) | 0 (0.0) | 3 (0.1) | 20 / 0 / 8 |
|  | Vol3 с.6: «…ing next to Florentian. I was thinking about the elder Ali with great gratitude not only because now I…»<br>Vol3 с.10: «…warrior, the creator of life who was next to the elder Ali and who’s already forgotten about himself fo…» | | | |
| Али старший → the older Ali | 7 (0.3) | 0 (0.0) | 0 (0.0) | — |
|  | Vol1 с.7: «…thes. It seemed to me that the black eyes of the older Ali pierced through the tree behind which we wer…»<br>Vol1 с.7: «…oaching calash intently. One more moment and the older Ali went up to the stopped coach. And … a small,…» | | | |
| Али старший → the old Ali | 1 (0.0) | 0 (0.0) | 0 (0.0) | — |
|  | Vol1 с.8: «…ad been asked – and I saw the huge figure of the old Ali, standing in front of me; He was stretching…» | | | |
| «И.» → I. (с пробелом/знаком после) | 1125 (47.8) | 22 (1.0) | 1818 (45.0) | 1069 / 21 / 1827 |
|  | Vol1 с.1: «…dko”, “Jolanta”, “Werther”, etc. She knew F. I. Chaliapin, S. V. Rachmaninoff and other famo…»<br>Vol1 с.71: «…invitation they came to help Ali, and so did I. Try to look at their faces differently for t…»<br>Vol2 с.102: «…s absolutely free in the same way as you and I. were doing it, but such miracles don’t happe…» | | | |

## Кальки

| Закономерность | Vol1 (ч. I) | Vol2 (ч. II) | Vol3 (ч. III) | RU (ч. I / II / III) |
|---|---|---|---|---|
| everything what / all what | 65 (2.8) | 114 (4.9) | 163 (4.0) | — |
|  | Vol1 с.25: «…m my eyes. It seemed to me that I had buried everything what was the best in this world and, having come…»<br>Vol1 с.25: «…e left for hunting on occasion.” And I named everything what I had been entrusted to in detail – about th…»<br>Vol2 с.10: «…?” “It is very strange, my father. Actually, everything what I have had in my life up to now – everything…» | | | |
| According to me | 0 (0.0) | 1 (0.0) | 0 (0.0) | — |
|  | Vol2 с.24: «…of you is her father and who is her fiancé. According to me, both of you are grooms,” she uttered timidl…» | | | |
| глагол речи/действия + by -ing (деепричастие) | 64 (2.7) | 102 (4.4) | 140 (3.5) | — |
|  | Vol1 с.89: «…d forgotten in Ali’s house so carelessly,” I told Florentian by giving him the wonderful note-book of my brother wi…»<br>Vol1 с.91: «…drops out of it into the glass of water and told me by giving the glass to me. “When I was ill, Ananda alw…»<br>Vol2 с.4: «…he wouldn’t be able to sleep,” the secretary told him in a whisper by smiling mischievously, “and now look, both the unusu…» | | | |
| hair were (волосы — мн. ч.) | 0 (0.0) | 2 (0.1) | 0 (0.0) | — |
|  | Vol2 с.23: «…head. Her distinct, curly, copper and parted hair were unusually luxuriant, it was done up in two w…»<br>Vol2 с.36: «…yes – and everybody understood why such grey hair were covering such young face. All of a sudden, e…» | | | |
| begin and start (начать и кончить) | 0 (0.0) | 0 (0.0) | 2 (0.0) | — |
|  | Vol3 с.8: «…al engine of your life – you will be able to begin and to start your every meeting calmly and joyfully. Beli…»<br>Vol3 с.8: «…man must achieve in his meeting – that’s to begin and to start each of them calmly, with compassion and kin…» | | | |

## Регистр и лексика

| Закономерность | Vol1 (ч. I) | Vol2 (ч. II) | Vol3 (ч. III) | RU (ч. I / II / III) |
|---|---|---|---|---|
| глагол речи uttered | 66 (2.8) | 134 (5.8) | 247 (6.1) | — |
|  | Vol1 с.7: «…ear heard a horse come rumbling. “Wait,” he uttered “they are coming.” I didn’t hear anything. M…»<br>Vol1 с.8: «…now from the very bottom of my heart, and I uttered with my plaintive voice. “I want to sleep ve…»<br>Vol2 с.6: «…rd the steamer as soon as possible. She only uttered by being amazed at the grandeur of the city.…» | | | |
| be going to | 84 (3.6) | 87 (3.8) | 87 (2.2) | — |
|  | Vol1 с.25: «…shutters. It was quiet in the street. When I was going to the bathroom, I saw the messenger who was al…»<br>Vol1 с.25: «…for hunting late in the evening, and that I was going to report about that to colonel N. It seemed th…»<br>Vol2 с.5: «…epends on our self- control how perfectly we are going to play our roles and save our lives. We have t…» | | | |
| clumsy sailor (матрос-верзила) | 77 (3.3) | 0 (0.0) | 0 (0.0) | 47 / 0 / 0 |
|  | Vol1 с.122: «…nd of the hospital’s section I saw that tall clumsy sailor who was accompanying us with the stretcher a…»<br>Vol1 с.122: «…the fourth class quickly, because this tall clumsy sailor was running up and down the stairs not worse…» | | | |
| oriental robe (халат) | 63 (2.7) | 1 (0.0) | 0 (0.0) | 65 / 22 / 10 |
|  | Vol1 с.4: «…locals who used to wear their bright motley oriental robes, I would feel as being in Baghdad and I woul…»<br>Vol1 с.4: «…youth were wearing white turbans and motley oriental robes made of silk. Their carriage and manners wer…»<br>Vol2 с.2: «…he young Ali Mahmed into the reddish wedding oriental robe and the sumptuous hijab. She separated with…» | | | |
| calm (как передача «мир» — проверять по контексту) | 75 (3.2) | 134 (5.8) | 328 (8.1) | — |
|  | Vol1 с.4: «…all of these Eastern people with their grand calm, or on the contrary – with their too great e…»<br>Vol1 с.10: «…y oriental robes up himself. “Now, Lovushka, calm yourself and put this green oriental robe on…»<br>Vol2 с.4: «…’t any trace of excitement on his serene and calm face of an old philosopher; it seemed that n…» | | | |
| peace | 64 (2.7) | 71 (3.1) | 68 (1.7) | 93 / 151 / 541 |
|  | Vol1 с.15: «…ter word, to cause a pain. She could be only peace, comfort and joy for everybody who would be…»<br>Vol1 с.17: «…e your faithfulness to only law – the law of peace. Be strong and wait for me without any fear…»<br>Vol2 с.15: «…igure of Florentian, next to the undisturbed peace which was reflected on his face. “Take my ar…» | | | |

## Пунктуация

| Закономерность | Vol1 (ч. I) | Vol2 (ч. II) | Vol3 (ч. III) | RU (ч. I / II / III) |
|---|---|---|---|---|
| реплика продолжается без запятой: «uttered “they» | 68 (2.9) | 54 (2.3) | 294 (7.3) | — |
|  | Vol1 с.7: «…eard a horse come rumbling. “Wait,” he uttered “they are coming.” I didn’t hear anything. My b…»<br>Vol1 с.7: «…ing staggering,” my brother was speaking to me “only stand so as nobody could notice us behind…»<br>Vol2 с.2: «…ened, and it was unusual for her to answer him “yes”. Having seen the girl with the simple Eng…» | | | |
