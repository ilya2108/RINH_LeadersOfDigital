#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests

test_num = input('Выберите тест от 1 до 5: ')

if test_num == '1':
    test = """
 Смитсоновский центр транскрипции привлекает общественность, чтобы сделать наши бесценные коллекции более доступными. Мы работаем рука об руку с сообществом цифровых добровольцев, называемых “добровольцами ", чтобы расшифровать исторические документы и коллекционные записи, чтобы облегчить исследования и поощрять обучение в классах повсюду. Участники имеют возможность переписать разнообразный массив коллекционных материалов, взятых из коллекций Смитсоновского института в области науки, истории, искусства и культуры. Даже расшифровка одной строки-это большая помощь!
Это подпроект под названием " Martin Moynihan-ATLAPETES (racemose finches) - Панама, Эквадор и Перу, 1958, 1960-1962 гг. понимание тенденций биоразнообразия и факторов, влияющих на них, требует от нас прежде всего глубокого знания самих видов . В этих полевых заметках д-р Мартин Мойнихан (1928-1996) документирует свою работу по кистевидным вьюркам (atlapetes) в Панаме, Эквадоре и Перу. Более полувека спустя орнитологи все еще делают открытия, такие как Антиокийский Зяблик, который был идентифицирован по музейным образцам, собранным в 1971 году. Его не видели живым в течение следующих 47 лет, пока он не был вновь открыт в Колумбии в 2018 году. Присоединяйтесь к другим цифровым добровольцам, чтобы записать наблюдения доктора Мойнихана и сделать их более доступными для современных исследователей. """

    tags = ['история','анализ']

if test_num == '2':
    test = "Наш клиент из Вирджинии ищет высококвалифицированного врача по сердечной недостаточности, который может обеспечить страховое покрытие заменяющего врача в течение примерно 6 месяцев, начиная с января. Провайдер будет работать с 8:00 до 17:00 плюс звонок по графику 1: 4. Провайдеру потребуются навыки ведения LVAd, трансплантации сердца и краткосрочных стратегий механической поддержки. Это средство использует Epic EMR"
    tags = ['кардиология', 'физиология']

if test_num == '3':
    test = "Цель этого проекта - измерить извилистость спиральных рукавов в галактиках. Этот параметр обмотки был связан с другими параметрами, которые являются более трудоемкими и трудными для измерения, такими как масса черной дыры в ядре галактики. С вашей помощью мы можем измерить, насколько плотно обернуты спиральные рукава в галактиках, и определить интересных кандидатов для будущих детальных наблюдений телескопа. В среднем люди находят задачи, которые должны быть достаточно простыми. "
    tags = ['физика', 'астрономия']

if test_num == '4':
    test = """
    Мы все живем ниже по течению! Чистая вода важна для здорового образа жизни. Помогите охране дикой природы защитить здоровье ручья в пределах водораздела долины Лихай, проведя простые тесты в вашем местном ручье или на участках, где охрана дикой природы создала проекты восстановления.
    """
    tags = ['здоровый образ жизни', 'физиология']

if test_num == '5':
    test = """
    Мы ищем целеустремленного человека со страстью к индустрии здравоохранения. Один из наших клиентов хочет добавить в свою команду сильного ученого-исследователя. Обязанности включают в себя:
    1) уведомить научных основателей и координатора программы об исследовании наиболее перспективных объектов
    2) Разработка молекулярных и клеточных анализов для тестирования инструментов редактирования генов и сгрнк
    3) планировать, проектировать и проводить исследования опухолей in vivo для глубокой характеристики целевых кандидатов компании
    4) установить новые механистические идеи, касающиеся влияния новых мишеней на противоопухолевый иммунный ответ и рост опухолевых клеток
    5) поддерживать безопасную и здоровую окружающую среду
    6) разработка и проведение комплексных клеточных функционал"""

    tags = ['биология','онкология','опухоли','лучевая терапия']





test_articles = """
Фон Было обнаружено, что возбудимость моторной коры изменяется после повторной транскраниальной магнитной стимуляции (Ртмс) височной коры, что подчеркивает возникновение кросс-модальной пластичности при неинвазивной стимуляции мозга. Здесь мы исследовали влияние временных низкочастотных ритмов на пластичность моторной коры головного мозга у большой выборки пациентов с шумом в ушах. У 116 пациентов с хроническим шумом в ушах оценивали различные параметры кортикальной возбудимости до и после десяти сеансов лечения Ртмс. Пациенты получали один из трех различных протоколов, каждый из которых включал 1 Гц Ртмс над левой височной корой. Ответ на лечение определялся как улучшение по крайней мере на пять баллов по опроснику тиннитуса (TQ). Переменные проценты покоились на моторном пороге (RMT) с короткими интервалами внутрикоркового торможения (ICF), внутрикоркового облегчения (ICF) и периода коркового молчания (UPC). Результаты
После лечения Ртмс РМТ была снижена примерно на 1% от выхода стимулятора почти достоверно во всей группе пациентов. SICI был связан со значительными изменениями в ответе на лечение. В группе людей, ответивших на лечение, наблюдалось снижение SICI в течение курса лечения, в группе людей, не ответивших на лечение, наблюдалась противоположная картина.\ Выводы
Незначительные изменения в РМТ во время лечения Ртмс не обязательно подразумевают систематический обзор РМТ на предмет безопасности и эффективности. Было показано, что ответ на лечение Ртмс связан с изменениями в SICI, которые могут отражать модуляцию ГАМКергических механизмов, прямо или косвенно связанных с эффектами лечения Ртмс.\ Фон
Шум в ушах связан с нервными изменениями как в слуховом тракте, так и в не слуховых областях мозга [1]. Например, связанные с тиннитусом изменения активности и связности в лобной, височной, теменной и лимбической областях [2, 3], по-видимому, отражают патологически измененные мозговые сети [4, 5].основываясь на этих данных, повторяющаяся транскраниальная магнитная стимуляция (Ртмс) была введена в качестве подхода к лечению тиннитуса [6]. Однако оказалось, что терапевтические эффекты являются умеренными и связаны с высокой межиндивидуальной вариабельностью, что повышает потребность в показателях для эффективной терапии. Клинические испытания Ртмс для тиннитуса обычно используют стимуляцию одного или обоих отделов височно-слуховой или височно-теменной коры. В последнее время эти протоколы были расширены за счет дополнительной стимуляции не слуховых областей, таких как лобная кора, чтобы более эффективно воздействовать на специфические для тиннитуса сети [7, 8].\
Повторная транскраниальная магнитная стимуляция (Ртмс) как терапевтическое вмешательство состоит из неинвазивной повторной стимуляции неокортикальных областей сотни раз в день с использованием принципов электромагнитной индукции. \
В заключение следует отметить, что эти исследования подчеркивают существование кросс-модальной пластичности в исследованиях Ртмс для тиннитуса или временной стимуляции. Доказательства функциональной связи между височной и моторной корой были получены в результате нейрофизиологических исследований и исследований метаболизма мозга [17, 18]. При шуме в ушах взаимодействие между сенсомоторной и слуховой системами хорошо установлено и клинически отражается соматосенсорной модуляцией восприятия шума в ушах [19]. Здесь мы стремились исследовать влияние временных ритмов на различные параметры возбудимости моторной коры головного мозга в самой большой на сегодняшний день изученной выборке тиннитуса, используя ретроспективный анализ данных, полученных в контексте различных клинических исследований. Поскольку до сих пор было проведено только одно исследование шума в ушах с небольшим размером выборки, мы особенно сосредоточились на ассоциации клинического ответа с изменениями возбудимости в поисках не слухового нейрофизиологического показателя для эффективной терапии.\ Методы
Предметы
Все участники дали письменное информированное согласие после тщательного разъяснения процедур. Все исследования, которые способствовали этому анализу, были одобрены комитетом по этике Регенсбургского университета. Все эксперименты проводились в соответствии с последней редакцией Хельсинкской декларации.\
Кортикальная возбудимость была измерена у 116 пациентов (84 (72,4%) мужчины; 49,2 ± 12,5 (21-83) года) с хроническим шумом в ушах (длительность 90 ± 94 (2-476) месяца). 28 (25,2%) из 111 пациентов (данные о 5 пациентах отсутствуют) сообщили о чисто левостороннем шуме в ушах, 21 (18,9%) сообщили о чисто правостороннем шуме в ушах, а 62 (55,9%) пациента описали свой шум в ушах как двусторонний или возникающий в голове. Дистресс тиннитуса оценивали с помощью немецкой версии [20] опросника тиннитуса (TQ) [21]; начальные баллы ТК варьировали от 3 до 79 (41 ± 18). Пациенты, страдающие болезнью Меньера, имеющие кондуктивную тугоухость или проявляющие признаки объективного шума в ушах, в исследование не включались. 62 пациента прошли полное отологическое и аудиологическое обследование, включая чистую тональную аудиометрию, тимпанометрию, стапедиус-рефлекторные тесты и отоскопию. Средний уровень слуха аудиограммы (двухсторонние пороги слуха при 0.125, 0.25, 0.5, 1, 2, 3, 4, 6, 8 кГц) составил 17 ± 13 (0-61 дБ ГЛ). В исследование были включены только те пациенты, которые имели право на лечение Ртмс. Таким образом, пациенты с кардиостимуляторами, судорогами в анамнезе, подозрением на органическое поражение головного мозга или любым другим тяжелым соматическим, неврологическим или психиатрическим диагнозом не были включены.\ Процедуры
Терапевтическое вмешательство состояло из 10 сеансов транскраниальной магнитной стимуляции в другие дни недели. Эффект лечения оценивали по изменению ТС между первым (1-й день) и последним днем лечения (12-й день). Возбудимость моторной коры изучали в первый день до лечения и в последний день после Ртмс. Мы проанализировали лонгитюдные данные 116 пациентов, участвовавших в трех различных исследованиях лечения [7, 22]. Пациенты получали один из трех различных протоколов активной стимуляции (2000 стимулов над слуховой корой с частотой 1 Гц: n = 68; 4000 стимулов над слуховой корой с частотой 1 Гц: n = 26; 2000 стимулов над левой лобной корой с частотой 20 Гц и затем 2000 стимулов над слуховой корой с частотой 1 Гц: n = 22). Стимуляция была установлена на уровне 110% от индивидуального порога покоя. Локализация стимулированных участков проводилась либо с помощью нейронавигационной системы, либо по стандартной методике, основанной на системе 10-20 [23]. Недавние исследования не выявили клинически значимых различий в эффективности лечения в зависимости от используемого метода позиционирования катушки [7]. В деталях каждый пациент лечился по одному протоколу продолжительностью десять дней и одним типом локализации, что означает, что были подгруппы с различными методами лечения. Данные были зафиксированы с 2004 по 2009 год. Все измерения проводились одним и тем же персоналом, который имел опыт работы с используемыми методами.\
Кортикальный период молчания измерялся в 10 испытаниях (интенсивность стимула: 150% порог моторного покоя; интервал сканирования: 5 С) в умеренно активной дигитальной отведительной мышце для непрямой записи каждого отдельного сканирования и затем усреднялся [26]. Участники были проинструктированы сжать эту мышцу на 30% максимальной силы. Начало периода молчания коры головного мозга определялось как окончание МЭП, когда активность последовательно опускалась ниже уровня ЭМГ перед стимулом. Окончание периода молчания коры головного мозга определялось как первое появление произвольной ЭМГ-активности. В заключение следует отметить, что переменные проценты ТМС покоились на моторном пороге (РМТ), соотношении сигнал/смерть от инфаркта 2 мс и 15 мс межстимульных интервалов (ICF и ICF соответственно) и периоде кортикального молчания (UPC).\ Статистика
Статистика основана на ретроспективном анализе. Нас интересовало, связаны ли изменения возбудимости моторной коры с лечением Ртмс как таковой и с вызванным Ртмс клиническим ответом. Таким образом, мы провели дисперсионный анализ с лечением как внутриобъектным фактором (первый и последний день лечения) и ответом на лечение как межобъектным фактором (ответчик и не ответчик). Ответ на лечение определялся как изменение ТК не менее чем на 5 баллов [27, 28]. Если ANOVA обнаруживала значимые результаты, мы проводили пост-hoc t-тесты для сравнения респондентов и не респондентов до и после Ртмс, а также для определения изменений в обеих группах с течением времени. Мы интересовались результатами протоколов ССО как потенциальным сопутствующим лицевым индикатором и повторили эти Ановы с протоколом РТМ в качестве ковариата (2000 стимулов и височных стимулов 4000 и 2000 стимулов лобных и височных 2000) - для значительного эффекта.\
Во-первых, Ртмс привела к почти значительному снижению РМТ (снижение выхода стимулятора на 1%) во всей исследуемой популяции (табл. 1). Остальные параметры возбудимости моторной коры остались неизменными. Мы не обнаружили существенных эффектов взаимодействия “протокола rTMS с изменениями в RMT, SICI, ICF и CSP.\ Оргвыводы
Контрапунктом к большому объему выборки является отсутствие контрольных групп и ретроспективного анализа. Поэтому необходимы дальнейшие проспективные исследования, включая контрольные группы, прежде чем можно будет сделать твердые выводы о специфике наблюдаемых эффектов Ртмс при лечении шума в ушах. Кроме того, последовательные ежедневные измерения лучше характеризуют временной ход изменений возбудимости.\"""
"""

test_articles_2 = """
Краткое описание Существует представление о том, что влияние западных традиций на Россию началось при царе-реформаторе, Петре Ι Великом. Возможно миф был во многом создан романом А.К. Толстого «Петр I» и его экранизацией в двух фильмах: «Юность Петра» и «В начале славных дел». 
Действительность Однако если присмотреться к этому сюжету детальнее, то получается, что еще при его предшественниках некоторые традиции западноевропейских стран усваивались при дворе. Это прослеживалось на протяжении ΧVII века. На самом деле определенная линия сближения с западом прослеживается еще в правление Бориса Годунова. Как отмечает Р.Г. Скрынников в своей монографии «Борис Годунов царь» признавал, что отношения с западом важны для Российского государства. Борис первым из русских правителей отправил молодых дворян для обучения наукам за границу. Он вынашивал планы учреждения в России школ и даже университета по европейскому образцу. Он проявлял живой интерес к просвещению и культуре, к успехам западной цивилизации. Более того, именно Борисом был сформирован из наемников-немцев собственный отряд телохранителей. Предвосхищая начинания Петра, Борис Годунов поощрял торговлю с западными странами. Немецкие купцы, переселенные в Россию из завоеванных Ливонских городов, получили от казны ссуды и право свободно перемещаться как внутри страны, так и за ее пределами. Однако сначала голод, а затем и Смутное время помешали осуществить все идеи. Короткое и трагическое царствование Лжедмитрия еще больше пестрило иностранным влиянием. Это был первый царь, который не привык спать после обеда, согласно традиции. Именно Лжедмитрий отменил для дворян запрет на выезд за рубеж, именно он заявил о своем намерении открыть в России первый университет и отправить русских дворян на обучение за границу. Это был первый из царей, который одевался на западный манер. Однако эти идеи авантюриста не нашли поддержки ни у знатной верхушки, ни у московского люда. Московское восстание и дальнейший ход Смуты, разумеется, отложил реализацию многих этих планов почти на сто лет. Страна была настолько разорена. На какое-то время иностранное не проявлялось в придворном этикете. Продолжая разговор о Петре, считается, что именно при нем возникла регулярная армия, организованная на европейский манер. Однако следует учесть, что для этого действа уже была подготовлена хорошая почва. Уже в ΧVII веке формируются полки «нового строя», они вооружались по образцу западноевропейских армий. Эти полки были солдатские, рейтарские и драгунские. В 1631 году было сформировано 2 солдатских полка, а во время русско-польской войны 1632-1634 гг. — еще 6 солдатских, один рейтарский и один драгунский полк. Эти полки стали постепенно вытеснять собой стрелецкое войско. Участие в войнах стрелецкого контингента, составлявшего постоянный контингент вооруженных сил, значительно сокращается. Стрельцы выполняли теперь преимущественно полицейские функции. А вместо стрелецкого войска в вооруженных силах все большее значение приобретали именно полки нового строя. Безусловно необходимо приписать в заслугу Петра Великого создание флота России по европейскому образцу. Петр Ι считал, что «Всякой потентатъ, который едино войско сухопутное имѣетъ, одну руку имѣетъ; а который и флотъ имѣетъ, обѣ руки имѣетъ». Однако и у этого мероприятия были свои предпослылки. Даже Н.И. Павленков, один из современных исследователей Петра I отмечает, что на верфи в подмосковном селе Дединове по царскому указу 1667 года было намечено построить несколько морских судов для защиты торговых интересов русских купцов у Астрахани.  Так был создан корабль «Орел». Его вооружение составляли 22 пищали. Это был первый парусный корабль, заложенный на территории России. Однако его постигла незавидная судьба: корабль «Орел» с незаконченной оснасткой находился у Астрахани и был захвачен и сожжен Степаном Разиным в 1670 году. XVII век по сути своей оказался столетием обмирщения русской культуры, проникновения в нее светских начал. Образованные слои горожан уже не довольствовались усвоением богословских истин и проявляли интерес к научным знаниям, к литературе, рассказывающей не о подвигах библейских героев, а о жизни обыкновенных людей. В живописи наметилась тенденция к реализму, в архитектуре пробивали путь светские элементы. Таким образом, стоит признать, что иностранное влияние при дворе прослеживалось и раньше правления Петра Ι. Конечно, оно оставляло свое отражение в культуре Российского государства. Однако это нисколько не умаляет заслуг реформ Петра. Ведь стоит признать, что именно его преобразования прочно засели в российскую политическую идеологию и культуру. И конечно, именно его преобразования затронули почти всю элитарную среду, что не проявлялось среди его предшественников. Возможно, именно благодаря этому в массовом сознании он и воспринимается как первый правитель, в эпоху которого Россия оказалась в зоне европейского влияния. 
"""

candidates = \
  [
  {'ID':1, 'articles': [], 'rating': 4, 'projects': [1], 'tags': [{'name': 'физиология', 'stage': 3}, {'name': 'кардиология', 'stage': 1}, {'name': 'онкология', 'stage': 2}]},
  {'ID':2,'articles':['Исследование раковых опухолей'],'rating':5,'projects':[],'tags':[{'name':'биология','stage':1},{'name':'онкология','stage':2}],},
  {'ID':3, 'articles': [], 'rating': 3, 'projects': [1], 'tags': [{'name': 'история', 'stage': 3}, {'name': 'россия', 'stage': 1}, {'name': 'обществознание', 'stage': 2}]},
  {'ID':4,'articles':['Авиастроение в современности'],'rating':3,'projects':[],'tags':[{'name':'программирование','stage':3},{'name':'спорт','stage':3}]},
  {'ID':5,'articles':[test_articles_2],'rating':0,'projects':[1],'tags':[{'name':'ядерная физика','stage':3},{'name':'физическая культура','stage':1},{'name':'история','stage':2}]},
  {'ID':6,'articles':[test_articles],'rating':0,'projects':[1,1,1],'tags':[{'name':'биология','stage':3},{'name':'нейрофизиология','stage':2},{'name':'машинное обучение','stage':1}]},
  {'ID':7,'articles':[],'rating':3,'projects':[1],'tags':[{'name':'обществознание','stage':3},{'name':'история','stage':2}]},
  {'ID':8,'articles':[],'rating':5,'projects':[1],'tags':[{'name':'физика','stage':3},{'name':'биология','stage':1},{'name':'авиастроение','stage':2}]},
  {'ID':9, 'articles': ['Исследование раковых опухолей', 'Разбор карбюратора'], 'rating': 3, 'projects': [], 'tags': [{'name': 'биология', 'stage': 1}, {'name': 'онкология', 'stage': 2}], },
  {'ID': 10, 'articles': ['Теория струн'], 'rating': 3, 'projects': [], 'tags': [{'name': 'биология', 'stage': 1}, {'name': 'онкология', 'stage': 2}], },
  ]

print(test)
print('--------------')
print(candidates)
# Результаты зависят от весов в test
print(requests.post('http://localhost:883/get_candidates',headers={'Content-Type':'application/json'},json={'project_tags':tags,'candidates':candidates,'annotation':test}).json())
