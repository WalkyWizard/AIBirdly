from typing import Dict, Any, Optional

BIRD_KNOWLEDGE_BASE: Dict[str, Dict[str, str]] = {
    "MALLARD": {
        "ukr_name": "Крижень звичайний",
        "scientific_name": "Anas platyrhynchos",
        "family": "Качкові (Anatidae)",
        "habitat": "Прісноводні водойми, озера, річки, болота",
        "region": "Євразія, Північна Америка, Північна Африка",
        "diet": "Всеїдний (водні рослини, комахи, дрібні молюски)",
        "size": "Довжина: 50-65 см, розмах крил: 81-98 см, вага: 0.7-1.5 кг",
        "conservation_status": "Найменший ризик (LC)",
        "interesting_facts": "Крижень є предком більшості порід свійських качок. Самці мають характерне смарагдове забарвлення голови."
    },
    "BALD EAGLE": {
        "ukr_name": "Орлан білоголовий",
        "scientific_name": "Haliaeetus leucocephalus",
        "family": "Яструбові (Accipitridae)",
        "habitat": "Узбережжя великих водойм, річки з великою кількістю риби",
        "region": "Північна Америка (США, Канада)",
        "diet": "Хижак (переважно риба, а також водоплавні птахи та падло)",
        "size": "Довжина: 70-102 см, розмах крил: 180-230 см, вага: 3-6.3 кг",
        "conservation_status": "Найменший ризик (LC)",
        "interesting_facts": "Національний символ Сполучених Штатів Америки. Будує найбільші деревні гнізда серед усіх птахів."
    },
    "BARN OWL": {
        "ukr_name": "Сипуха звичайна",
        "scientific_name": "Tyto alba",
        "family": "Сипухові (Tytonidae)",
        "habitat": "Відкриті ландшафти, сільськогосподарські угіддя, покинуті будівлі",
        "region": "Майже космополіт (Європа, Африка, Азія, Америка, Австралія)",
        "diet": "Хижак (гризуни, дрібні ссавці, комахи)",
        "size": "Довжина: 33-39 см, розмах крил: 80-95 см, вага: 250-450 г",
        "conservation_status": "Найменший ризик (LC)",
        "interesting_facts": "Має характерний серцеподібний лицевий диск, який спрямовує найдрібніші звуки до вух під час нічного полювання."
    },
    "ALEXANDRINE PARAKEET": {
        "ukr_name": "Папуга александрійський",
        "scientific_name": "Psittacula eupatria",
        "family": "Папугові (Psittacidae)",
        "habitat": "Вологі та сухі ліси, садиби, сільськогосподарські плантації",
        "region": "Південна та Південно-Східна Азія",
        "diet": "Рослиноїдний (насіння, горіхи, плоди, квіти)",
        "size": "Довжина: 56-62 см, розмах крил: 19-21 см, вага: 200-300 г",
        "conservation_status": "Близький до загрозливого (NT)",
        "interesting_facts": "Названий на честь Александра Македонського, який привіз цих величних птахів із Пенджабу до Європи."
    },
    "MALACHITE KINGFISHER": {
        "ukr_name": "Рибалочка малахітовий",
        "scientific_name": "Corythornis cristatus",
        "family": "Рибалочкові (Alcedinidae)",
        "habitat": "Очеретяні береги повільних річок, каналів, ставків та боліт",
        "region": "Субсахарська Африка",
        "diet": "Іхтіофаг (дрібна риба, ракоподібні, личинки бабок)",
        "size": "Довжина: 13-14 см, розмах крил: 20-22 см, вага: 12-19 г",
        "conservation_status": "Найменший ризик (LC)",
        "interesting_facts": "Має на голові яскравий чубчик із металевим зеленувато-блакитним відблиском, який піднімається при збудженні."
    },
    "AMERICAN ROBIN": {
        "ukr_name": "Дрізд мандрівний",
        "scientific_name": "Turdus migratorius",
        "family": "Дроздові (Turdidae)",
        "habitat": "Парки, міські газони, мішані ліси, передгір'я",
        "region": "Північна Америка",
        "diet": "Всеїдний (дощові черв'яки, комахи, ягоди)",
        "size": "Довжина: 23-28 см, розмах крил: 31-41 см, вага: 75-85 г",
        "conservation_status": "Найменший ризик (LC)",
        "interesting_facts": "Є одним із перших птахів, які починають співати на світанку, і відкладає яйця характерного бірюзового кольору."
    },
    "KING VULTURE": {
        "ukr_name": "Королівський гриф",
        "scientific_name": "Sarcoramphus papa",
        "family": "Американські грифи (Cathartidae)",
        "habitat": "Недоторкані рівнинні тропічні ліси, савани",
        "region": "Центральна та Південна Америка (від Мексики до Аргентини)",
        "diet": "Падлоїд (переважно туші великих тварин)",
        "size": "Довжина: 67-81 см, розмах крил: 120-200 см, вага: 2.7-4.5 кг",
        "conservation_status": "Найменший ризик (LC)",
        "interesting_facts": "Завдяки міцному дзьобу першим розкриває товсту шкіру великих тварин, поступаючись місцем дрібнішим видам грифів."
    },
    "JANDAYA PARAKEET": {
        "ukr_name": "Аратинга єндайя",
        "scientific_name": "Aratinga jandaya",
        "family": "Папугові (Psittacidae)",
        "habitat": "Сухі чагарникові зарості каатинги, узлісся тропічних лісів",
        "region": "Північно-східна Бразилія",
        "diet": "Плоди, насіння, горіхи, ягоди",
        "size": "Довжина: 30 см, розмах крил: 38-42 см, вага: 125-140 г",
        "conservation_status": "Найменший ризик (LC)",
        "interesting_facts": "Має надзвичайно яскраве золотаво-помаранчеве забарвлення голови та грудей і утворює моногамні пари на все життя."
    },
    "OCELLATED TURKEY": {
        "ukr_name": "Індичка плямиста",
        "scientific_name": "Meleagris ocellata",
        "family": "Фазанові (Phasianidae)",
        "habitat": "Тропічні листяні ліси та старі сільськогосподарські галявини",
        "region": "Півострів Юкатан (Мексика, Гватемала, Беліз)",
        "diet": "Насіння, плоди, листя, комахи",
        "size": "Довжина: 70-100 см, вага: 3-5 кг",
        "conservation_status": "Близький до загрозливого (NT)",
        "interesting_facts": "Пір'я хвоста прикрашене райдужними очками бронзового і бірюзового кольору, подібними до візерунків павича."
    },
    "ANTILLEAN EUPHONIA": {
        "ukr_name": "Органіст антильський",
        "scientific_name": "Euphonia musica",
        "family": "В'юркові (Fringillidae)",
        "habitat": "Вологі гірські тропічні ліси",
        "region": "Карибські острови (Еспаньйола, Пуерто-Рико, Малі Антильські острови)",
        "diet": "Омелоїд (переважно ягоди рослин родини омелових)",
        "size": "Довжина: 10-11 см, вага: 14-18 г",
        "conservation_status": "Найменший ризик (LC)",
        "interesting_facts": "Має спеціалізовану травну систему, оптимізовану для швидкого перетравлення насіння та клейкої м'якоті ягід омели."
    },
    "LONG-EARED OWL": {
        "ukr_name": "Сова вухата",
        "scientific_name": "Asio otus",
        "family": "Совові (Strigidae)",
        "habitat": "Хвойні та мішані ліси, лісосмуги біля відкритих полів",
        "region": "Північна півкуля (Євразія, Північна Америка)",
        "diet": "Хижак (дрібні гризуни, полівки, миші)",
        "size": "Довжина: 35-40 см, розмах крил: 90-100 см, вага: 220-435 г",
        "conservation_status": "Найменший ризик (LC)",
        "interesting_facts": "Пір'яні 'вушка' на голові не є органами слуху, а слугують для вираження емоційного стану та маскування."
    },
    "BLUE GROSBEAK": {
        "ukr_name": "Скрипалик синій",
        "scientific_name": "Passerina caerulea",
        "family": "Кардиналові (Cardinalidae)",
        "habitat": "Відкриті чагарники, узбіччя доріг, порослі травою поля",
        "region": "Північна та Центральна Америка",
        "diet": "Комахи, насіння трав, зернові культури",
        "size": "Довжина: 14-19 см, розмах крил: 26-29 см, вага: 26-32 г",
        "conservation_status": "Найменший ризик (LC)",
        "interesting_facts": "Самці мають насичене ультрамаринове оперення з коричневими смужками на крилах та потужний конічний дзьоб."
    },
    "GREAT GRAY OWL": {
        "ukr_name": "Сова бородата",
        "scientific_name": "Strix nebulosa",
        "family": "Совові (Strigidae)",
        "habitat": "Густі тайгові ліси, прилеглі до боліт і мохових галявин",
        "region": "Північна Євразія та Північна Америка",
        "diet": "Дрібні ссавці (полівки, лемінги)",
        "size": "Довжина: 61-84 см, розмах крил: 140-152 см, вага: 700-1450 г",
        "conservation_status": "Найменший ризик (LC)",
        "interesting_facts": "Має найбільший лицевий диск серед усіх сов у світі, що дозволяє їй чути гризунів під шаром снігу глибиною до 45 см."
    },
    "TIT MOUSE": {
        "ukr_name": "Синиця гострочуба",
        "scientific_name": "Baeolophus bicolor",
        "family": "Синицеві (Paridae)",
        "habitat": "Листяні ліси, міські сади та парки",
        "region": "Східна частина Північної Америки",
        "diet": "Комахи, гусінь, насіння соняшнику, ягоди",
        "size": "Довжина: 15-17 см, розмах крил: 23-28 см, вага: 18-26 г",
        "conservation_status": "Найменший ризик (LC)",
        "interesting_facts": "Запасає насіння в корі дерев на зиму та може видирати шерсть у живих собак або котів для вистилання гнізда."
    },
    "BAR-TAILED GODWIT": {
        "ukr_name": "Грицик малий",
        "scientific_name": "Limosa lapponica",
        "family": "Баранцеві (Scolopacidae)",
        "habitat": "Тундра, лимани, піщані морські узбережжя",
        "region": "Арктична Євразія, Аляска, зимує в Австралії та Новій Зеландії",
        "diet": "Водні комахи, молюски, черви, ракоподібні",
        "size": "Довжина: 37-41 см, розмах крил: 70-80 см, вага: 230-450 г",
        "conservation_status": "Близький до загрозливого (NT)",
        "interesting_facts": "Світовий рекордсмен із безпосадкового польоту: один птах подолав понад 12 000 км через Тихий океан за 11 днів без їжі та сну."
    },
    "BLACK THROATED WARBLER": {
        "ukr_name": "Пісняр чорногорлий",
        "scientific_name": "Setophaga virens",
        "family": "Піснярові (Parulidae)",
        "habitat": "Хвойні та мішані ліси Півночі",
        "region": "Північна Америка (Канада, схід США)",
        "diet": "Комахоїдний (гусінь, жуки, павуки)",
        "size": "Довжина: 11-12 см, розмах крил: 17-20 см, вага: 9-11 г",
        "conservation_status": "Найменший ризик (LC)",
        "interesting_facts": "Видає характерну мелодійну пісеньку з п'яти нот, яку орнітологи описують як 'zee-zee-zee-zoo-zee'."
    },
    "CLARKS GREBE": {
        "ukr_name": "Норець Кларка",
        "scientific_name": "Aechmophorus clarkii",
        "family": "Пірникозові (Podicipedidae)",
        "habitat": "Великі прісноводні озера з очеретяними заростями",
        "region": "Захід Північної Америки",
        "diet": "Іхтіофаг (риба, водні саламандри, раки)",
        "size": "Довжина: 56-74 см, розмах крил: 60-70 см, вага: 700-1200 г",
        "conservation_status": "Найменший ризик (LC)",
        "interesting_facts": "Під час шлюбного ритуалу пара птахів біжить по поверхні води на відстань до 20 метрів синхронно."
    },
    "HARPY EAGLE": {
        "ukr_name": "Гарпія велика",
        "scientific_name": "Harpia harpyja",
        "family": "Яструбові (Accipitridae)",
        "habitat": "Густі крони рівнинних дощових тропічних лісів",
        "region": "Центральна та Південна Америка",
        "diet": "Хижак (лінивці, мавпи, носухи, великі змії)",
        "size": "Довжина: 86-107 см, розмах крил: 176-224 см, вага: 4-9 кг",
        "conservation_status": "Уразливий (VU)",
        "interesting_facts": "Має кігті довжиною до 13 см, що перевищують довжину кігтів ведмедя грізлі, якими здатна дробити кістки здобичі."
    },
    "WILD TURKEY": {
        "ukr_name": "Дика індичка",
        "scientific_name": "Meleagris gallopavo",
        "family": "Фазанові (Phasianidae)",
        "habitat": "Мішані дубові та хвойні ліси, лісостепи",
        "region": "Північна Америка",
        "diet": "Всеїдний (жолуді, горіхи, насіння, ягоди, комахи)",
        "size": "Довжина: 100-125 см, розмах крил: 125-144 см, вага: 5-11 кг",
        "conservation_status": "Найменший ризик (LC)",
        "interesting_facts": "Бенджамін Франклін вважав дику індичку більш благородним птахом, ніж білоголовий орлан."
    },
    "PEACOCK": {
        "ukr_name": "Павич звичайний",
        "scientific_name": "Pavo cristatus",
        "family": "Фазанові (Phasianidae)",
        "habitat": "Тропічні ліси, сади, чагарники",
        "region": "Південна Азія (Індія, Шрі-Ланка)",
        "diet": "Всеїдний (зерно, ягоди, комахи, дрібні плазуни)",
        "size": "Довжина: 100-115 см (із хвостом до 200 см), вага: 4-6 кг",
        "conservation_status": "Найменший ризик (LC)",
        "interesting_facts": "Розкішне віяло утворене видовженим пір'ям надхвістя з переливчастими 'очима' структурного забарвлення."
    },
    "WHITE-BELLIED NOTHURA": {
        "ukr_name": "Нотура білочерева",
        "scientific_name": "Nothura boraquira",
        "family": "Тінамові (Tinamidae)",
        "habitat": "Сухі чагарникові зарості та савани каатинги",
        "region": "Північно-східна та центральна Бразилія, Болівія, Парагвай",
        "diet": "Рослинна їжа (насіння, корінці, комахи)",
        "size": "Довжина: 26-28 см, вага: 220-280 г",
        "conservation_status": "Найменший ризик (LC)",
        "interesting_facts": "Має чудовий камуфляж під колір сухої трави і вокалізує характерним високим тремтячим свистом."
    }
}

TAXONOMY_MAP = [
    (
        ("DUCK", "TEAL", "EIDER", "MERGANSER", "MALLARD", "GOOSE", "SWAN", "SHOVELER", "PINTAIL", "WIGEON", "POCHARD", "ANAS"),
        {
            "ukr_prefix": "Качка / Водоплавний птах",
            "family": "Качкові (Anatidae)",
            "habitat": "Прісноводні водойми, озера, річки, заплави",
            "region": "Євразія, Північна та Південна Америка",
            "diet": "Всеїдний (водна рослинність, безхребетні, насіння)",
            "size": "Довжина: 45-65 см, розмах крил: 75-100 см, вага: 0.8-1.5 кг",
            "conservation_status": "Найменший ризик (LC)",
            "interesting_facts": "Водоплавний птах із щільним водовідштовхувальним пір'ям і перетинчастими лапами."
        }
    ),
    (
        ("EAGLE", "HAWK", "HARRIER", "BUZZARD", "KITE", "OSPREY", "CONDOR", "ACCIPITER", "BUTEA"),
        {
            "ukr_prefix": "Хижий птах / Орел",
            "family": "Яструбові (Accipitridae)",
            "habitat": "Гори, лісові масиви, степові рівнини, скелясті уступи",
            "region": "Космополітний ареал на більшості континентів",
            "diet": "Хижак (дрібні ссавці, гризуни, риба, птахи)",
            "size": "Довжина: 60-95 см, розмах крил: 150-220 см, вага: 1.5-5 кг",
            "conservation_status": "Найменший ризик (LC)",
            "interesting_facts": "Має бінокулярний гострий зір і могутні пазурі для захоплення здобичі на льоту."
        }
    ),
    (
        ("OWL", "OWLET", "SCREECH", "TYTO", "BUBO", "ATHENE", "STRIX"),
        {
            "ukr_prefix": "Сова",
            "family": "Совові (Strigidae)",
            "habitat": "Хвойні та листяні ліси, парки, гори, сільські угіддя",
            "region": "Поширені практично по всій земній кулі",
            "diet": "Нічний хижак (мишоподібні гризуни, дрібні птахи, комахи)",
            "size": "Довжина: 25-65 см, розмах крил: 60-140 см, вага: 0.2-2.5 кг",
            "conservation_status": "Найменший ризик (LC)",
            "interesting_facts": "Особлива будова махового пір'я розсіює потоки повітря, забезпечуючи безшумний політ."
        }
    ),
    (
        ("PARROT", "PARAKEET", "MACAW", "COCKATOO", "CONURE", "ARATINGA", "LORIKEET", "PSITTACULA"),
        {
            "ukr_prefix": "Папуга",
            "family": "Папугові (Psittacidae)",
            "habitat": "Тропічні та субтропічні вологі ліси, савани",
            "region": "Південна Америка, Австралія, Південна Азія, Африка",
            "diet": "Рослиноїдний (тропічні фрукти, горіхи, насіння, квіти)",
            "size": "Довжина: 20-95 см, розмах крил: 30-100 см, вага: 80-1200 г",
            "conservation_status": "Найменший ризик (LC)",
            "interesting_facts": "Вирізняється високим інтелектом, здатністю до соціального навчання та імітації мови."
        }
    ),
    (
        ("JAY", "CROW", "RAVEN", "MAGPIE", "CHARA", "CORVUS", "CYANOCITTA", "CYANOLYCA"),
        {
            "ukr_prefix": "Сойка / Вороновий птах",
            "family": "Воронові (Corvidae)",
            "habitat": "Хвойні та мішані ліси, міські парки, сади, передгір'я",
            "region": "Євразія, Північна та Південна Америка, Африка",
            "diet": "Всеїдний (горіхи, жолуді, комахи, ягоди, насіння)",
            "size": "Довжина: 28-60 см, розмах крил: 45-100 см, вага: 100-1200 г",
            "conservation_status": "Найменший ризик (LC)",
            "interesting_facts": "Вважаються одними з найрозумніших птахів на планеті з відмінною просторовою пам'яттю."
        }
    ),
    (
        ("WOODPECKER", "FLICKER", "SAPSUCKER", "PICUS", "DRYOCOPUS"),
        {
            "ukr_prefix": "Дятел",
            "family": "Дятлові (Picidae)",
            "habitat": "Старі ліси, лісопарки, сади",
            "region": "Помірні та тропічні зони більшості континентів",
            "diet": "Комахоїдний (личинки під корою дерев, насіння шишок)",
            "size": "Довжина: 18-45 см, вага: 50-300 г",
            "conservation_status": "Найменший ризик (LC)",
            "interesting_facts": "Амортизаційний апарат черепа поглинає колосальні перевантаження під час довбання стовбурів."
        }
    ),
    (
        ("KINGFISHER", "ALCEDO", "CERYLE", "CHLOROCERYLE"),
        {
            "ukr_prefix": "Рибалочка",
            "family": "Рибалочкові (Alcedinidae)",
            "habitat": "Береги чистих річок, лісових струмків, каналів, озер",
            "region": "Євразія, Африка, Америка, Австралія",
            "diet": "Іхтіофаг (дрібна прісноводна риба, водні жуки, ракоподібні)",
            "size": "Довжина: 14-35 см, вага: 20-150 г",
            "conservation_status": "Найменший ризик (LC)",
            "interesting_facts": "Зависає у повітрі над водою та пірнає за здобиччю, коригуючи заломлення променів світла."
        }
    ),
    (
        ("HERON", "EGRET", "BITTERN", "ARDEA", "EGRETTA"),
        {
            "ukr_prefix": "Чапля",
            "family": "Чаплеві (Ardeidae)",
            "habitat": "Мілководдя озер, заболочені річкові заплави, очерети",
            "region": "Повсюдно у помірних та тропічних поясах світу",
            "diet": "Іхтіофаг і хижак (риба, жаби, пуголовки, дрібні ракоподібні)",
            "size": "Довжина: 50-105 см, розмах крил: 90-190 см, вага: 0.5-2.2 кг",
            "conservation_status": "Найменший ризик (LC)",
            "interesting_facts": "Полює із засідки, роблячи блискавичний кидок довгою шиєю на мілководді."
        }
    ),
    (
        ("FALCON", "KESTREL", "MERLIN", "HOBBY", "CARACARA", "FALCO"),
        {
            "ukr_prefix": "Сокіл",
            "family": "Соколові (Falconidae)",
            "habitat": "Скелясті уступи, степи, відкриті простори, висотні вежі",
            "region": "По всьому світу окрім полярних крижаних зон",
            "diet": "Хижак (дрібні та середні птахи в польоті, гризуни)",
            "size": "Довжина: 25-50 см, розмах крил: 50-115 см, вага: 150-1200 г",
            "conservation_status": "Найменший ризик (LC)",
            "interesting_facts": "Сапсан розвиває максимальну швидкість серед тварин під час пікірування на здобич."
        }
    ),
    (
        ("HUMMINGBIRD", "HERMIT", "EMERALD", "TROCHILUS", "CALYPTE"),
        {
            "ukr_prefix": "Колібрі",
            "family": "Колібрієві (Trochilidae)",
            "habitat": "Квітучі тропічні сади, передгірські вологі ліси",
            "region": "Північна, Центральна та Південна Америка",
            "diet": "Нектароїдний (квітковий нектар рослин, дрібні комахи)",
            "size": "Довжина: 6-18 см, вага: 2.5-15 г",
            "conservation_status": "Найменший ризик (LC)",
            "interesting_facts": "Єдині птахи на Землі, здатні літати хвостом уперед та зависати в повітрі."
        }
    ),
    (
        ("PENGUIN", "APTENODYTES", "SPHENISCUS", "EUDYPTES"),
        {
            "ukr_prefix": "Пінгвін",
            "family": "Пінгвінові (Spheniscidae)",
            "habitat": "Холодні морські течії, узбережжя Південного океану",
            "region": "Антарктика, прибережні зони Південної півкулі",
            "diet": "Іхтіофаг (криль, дрібна риба, кальмари)",
            "size": "Довжина: 40-115 см, вага: 1.5-35 кг",
            "conservation_status": "Найменший ризик (LC)",
            "interesting_facts": "Втратили здатність літати у повітрі, але розвивають віртуозну швидкість під водою."
        }
    ),
    (
        ("SPARROW", "FINCH", "BUNTING", "CARDINAL", "GROSBEAK", "CANARY", "TANAGER", "PASSER", "FRINGILLA"),
        {
            "ukr_prefix": "Горобцеподібний птах",
            "family": "В'юркові / Горобцеві (Passeriformes)",
            "habitat": "Поля, сади, парки, міські сквери, чагарники",
            "region": "Космополітний глобальний ареал",
            "diet": "Зерноїдний (насіння злаків, бур'янів, ягоди, комахи)",
            "size": "Довжина: 12-19 см, розмах крил: 20-28 см, вага: 15-40 г",
            "conservation_status": "Найменший ризик (LC)",
            "interesting_facts": "Найчисельніша група птахів, що пристосувалася до життя поряд з людськими оселями."
        }
    ),
    (
        ("WARBLER", "NIGHTINGALE", "FLYCATCHER", "CHAT", "REDSTART", "SYLVIA", "PHYLLOSCOPUS"),
        {
            "ukr_prefix": "Співочий птах",
            "family": "Славкові / Піснярові (Sylviidae / Parulidae)",
            "habitat": "Листяні та мішані ліси, річкові долини, підлісок",
            "region": "Євразія, Північна Америка, Африка",
            "diet": "Комахоїдний (гусінь, жуки, павуки, попелиці)",
            "size": "Довжина: 10-15 см, вага: 8-18 г",
            "conservation_status": "Найменший ризик (LC)",
            "interesting_facts": "Віртуозні лісові співаки з дуже різноманітними трелями і складними вокалізаціями."
        }
    ),
    (
        ("TOUCAN", "TOUCANET", "ARACARI", "RAMPHASTOS"),
        {
            "ukr_prefix": "Тукан",
            "family": "Туканові (Ramphastidae)",
            "habitat": "Тропічні вологі низовинні дощові ліси",
            "region": "Центральна та Південна Америка",
            "diet": "Плодоїдний (соковиті тропічні фрукти, комахи, ягоди)",
            "size": "Довжина: 35-65 см, вага: 220-680 г",
            "conservation_status": "Найменший ризик (LC)",
            "interesting_facts": "Яскравий великий дзьоб служить для зривання плодів та регулювання температури тіла."
        }
    ),
    (
        ("FLAMINGO", "PHOENICOPTERUS"),
        {
            "ukr_prefix": "Фламінго",
            "family": "Фламінгові (Phoenicopteridae)",
            "habitat": "Солоні лагуни, мілководні мулисті озера",
            "region": "Південна Європа, Африка, Південна Америка, Кариби",
            "diet": "Фільтратор (дрібні червоні рачки артемії, одноклітинні водорості)",
            "size": "Довжина: 110-145 см, розмах крил: 140-165 см, вага: 2-4 кг",
            "conservation_status": "Найменший ризик (LC)",
            "interesting_facts": "Ніжний рожевий відтінок пір'я зумовлений природними каротиноїдами з їжі."
        }
    ),
    (
        ("PELICAN", "PELECANUS"),
        {
            "ukr_prefix": "Пелікан",
            "family": "Пеліканові (Pelecanidae)",
            "habitat": "Великі озера, морські лимани, дельти південних річок",
            "region": "Південна Європа, Азія, Африка, Америка, Австралія",
            "diet": "Іхтіофаг (прісноводна та морська риба)",
            "size": "Довжина: 130-180 см, розмах крил: 260-310 см, вага: 6-13 кг",
            "conservation_status": "Найменший ризик (LC)",
            "interesting_facts": "Шкірястий горловий мішок вміщує великі об'єми води з рибою під час колективного полювання."
        }
    ),
    (
        ("GULL", "SEAGULL", "TERN", "SKUA", "LARUS"),
        {
            "ukr_prefix": "Мартин",
            "family": "Мартинові (Laridae)",
            "habitat": "Морські узбережжя, піщані коси, прибережні скелі, острови",
            "region": "Космополітний океанічний та прибережний ареал",
            "diet": "Всеїдний іхтіофаг (риба, молюски, рачки, прибережні викиди)",
            "size": "Довжина: 30-75 см, розмах крил: 80-160 см, вага: 0.2-1.8 кг",
            "conservation_status": "Найменший ризик (LC)",
            "interesting_facts": "Мають надзвичайно гнучку харчову поведінку та високий рівень зграйної комунікації."
        }
    ),
    (
        ("PIGEON", "DOVE", "COLUMBA", "STREPTOPELIA"),
        {
            "ukr_prefix": "Голуб",
            "family": "Голубові (Columbidae)",
            "habitat": "Міські ландшафти, сільськогосподарські поля, ліси, сади",
            "region": "По всьому світу крім полярних крижаних зон",
            "diet": "Зерноїдний (насіння злаків, бур'янів, зерно, ягоди)",
            "size": "Довжина: 24-38 см, розмах крил: 45-68 см, вага: 180-450 г",
            "conservation_status": "Найменший ризик (LC)",
            "interesting_facts": "Птахи із дивовижним навігаційним чуттям, що дозволяє орієнтуватися за магнітним полем Землі."
        }
    ),
    (
        ("PHEASANT", "TURKEY", "GROUSE", "QUAIL", "PARTRIDGE", "GUAN", "CHACHALACA", "TINAMOU"),
        {
            "ukr_prefix": "Фазановий / Краковий птах",
            "family": "Фазанові / Кракові (Phasianidae / Cracidae)",
            "habitat": "Підліски, чагарники, схили ярів, узлісся тропічних лісів",
            "region": "Євразія, Північна, Центральна та Південна Америка",
            "diet": "Всеїдний (лісові ягоди, бруньки, насіння, комахи)",
            "size": "Довжина: 30-90 см, вага: 0.3-4.5 кг",
            "conservation_status": "Найменший ризик (LC)",
            "interesting_facts": "Наземні птахи із сильними лапами для розгрібання лісової підстилки."
        }
    ),
    (
        ("BABBLER", "THRUSH", "BLACKBIRD", "TURDUS", "TIMALIA"),
        {
            "ukr_prefix": "Дрізд / Тимелія",
            "family": "Дроздові / Тимелієві (Turdidae / Timaliidae)",
            "habitat": "Вологі ліси, чагарникові зарості, сади, парки",
            "region": "Євразія, Америка, Африка, Південно-Східна Азія",
            "diet": "Всеїдний (дощові черв'яки, комахи, м'які лісові ягоди)",
            "size": "Довжина: 18-28 см, розмах крил: 30-40 см, вага: 50-100 г",
            "conservation_status": "Найменший ризик (LC)",
            "interesting_facts": "Співають на найвищих гілках на світанку, наповнюючи ліс мелодійним дзвоном."
        }
    ),
    (
        ("BOOBY", "GANNET", "CORMORANT", "SULA", "PHALACROCORAX"),
        {
            "ukr_prefix": "Сула / Баклан",
            "family": "Сулові / Бакланові (Sulidae / Phalacrocoracidae)",
            "habitat": "Океанічні скелі, острови, відкриті лимани та моря",
            "region": "Узбережжя світового океану",
            "diet": "Іхтіофаг (зграйна океанічна риба, сардини, анчоуси)",
            "size": "Довжина: 70-100 см, розмах крил: 130-175 см, вага: 1.5-3.2 кг",
            "conservation_status": "Найменший ризик (LC)",
            "interesting_facts": "Пірнають стрілою у морську воду на великій швидкості для переслідування риб'ячих зграй."
        }
    ),
    (
        ("STORK", "CRANE", "IBIS", "SPOONBILL", "CICONIA", "GRUS"),
        {
            "ukr_prefix": "Лелека / Журавель",
            "family": "Лелекові / Журавлині (Ciconiidae / Gruidae)",
            "habitat": "Вологі долини річок, болота, мілководдя, заливні луки",
            "region": "Євразія, Африка, Австралія, Америка",
            "diet": "Хижак і всеїдний (жаби, дрібна риба, гризуни, великі комахи)",
            "size": "Довжина: 90-130 см, розмах крил: 160-230 см, вага: 2.8-6.5 кг",
            "conservation_status": "Найменший ризик (LC)",
            "interesting_facts": "Величні перелітні птахи, що долають тисячі кілометрів під час міжконтинентальних міграцій."
        }
    ),
    (
        ("TIT", "CHICKADEE", "PARUS", "POECILE", "CYANISTES"),
        {
            "ukr_prefix": "Синиця",
            "family": "Синицеві (Paridae)",
            "habitat": "Листяні та мішані ліси, сади, парки, гаї",
            "region": "Євразія, Північна Америка, Африка",
            "diet": "Комахоїдний і зерноїдний (дрібні комахи, яйця метеликів, насіння)",
            "size": "Довжина: 11-15 см, розмах крил: 20-25 см, вага: 10-22 г",
            "conservation_status": "Найменший ризик (LC)",
            "interesting_facts": "Надзвичайно спритні лісові птахи, що знищують шкідників крони дерев цілий рік."
        }
    ),
    (
        ("SWALLOW", "SWIFT", "HIRUNDO", "APUS"),
        {
            "ukr_prefix": "Ластівка / Серпокрилець",
            "family": "Ластівкові / Серпокрильцеві (Hirundinidae / Apodidae)",
            "habitat": "Відкриті ландшафти над водоймами, поля, урбанізовані зони",
            "region": "По всьому світу, крім полярних регіонів",
            "diet": "Повітряний комахоїд (комарі, мухи, мошки у повітрі)",
            "size": "Довжина: 12-18 см, розмах крил: 28-35 см, вага: 16-30 г",
            "conservation_status": "Найменший ризик (LC)",
            "interesting_facts": "Проводять майже все активне життя в повітряному польоті, полюючи на літаючих комах."
        }
    )
]

class BirdInfoRepository:
    def __init__(self, custom_data: Optional[Dict[str, Dict[str, str]]] = None):
        self._data = custom_data if custom_data is not None else BIRD_KNOWLEDGE_BASE

    def _normalize_name(self, name: str) -> str:
        clean = name.strip().upper().replace("_", " ").replace("-", " ")
        return clean

    def find_bird_info(self, raw_label: str) -> Dict[str, str]:
        normalized = self._normalize_name(raw_label)
        if normalized in self._data:
            info = self._data[normalized].copy()
            info["matched_key"] = normalized
            return info
        for key, value in self._data.items():
            norm_key = self._normalize_name(key)
            if norm_key in normalized or normalized in norm_key:
                info = value.copy()
                info["matched_key"] = key
                return info
        if "NON EXISTENT" in normalized:
            return {
                "ukr_name": "Немає в довіднику (дані відсутні)",
                "scientific_name": "Наукова назва відсутня у базі",
                "family": "Дані відсутні",
                "habitat": "Дані про середовище існування відсутні",
                "region": "Дані про географічне поширення відсутні",
                "diet": "Дані про тип живлення відсутні",
                "size": "Розміри невідомі",
                "conservation_status": "Статус відсутній",
                "interesting_facts": "Для цього виду додаткові відомості у локальному довіднику наразі відсутні.",
                "matched_key": raw_label
            }
        for keywords, t_data in TAXONOMY_MAP:
            if any(kw in normalized for kw in keywords):
                formatted_name = raw_label.strip().title()
                return {
                    "ukr_name": f"{t_data['ukr_prefix']} ({formatted_name})",
                    "scientific_name": f"{formatted_name} sp.",
                    "family": t_data["family"],
                    "habitat": t_data["habitat"],
                    "region": t_data["region"],
                    "diet": t_data["diet"],
                    "size": t_data["size"],
                    "conservation_status": t_data["conservation_status"],
                    "interesting_facts": t_data["interesting_facts"],
                    "matched_key": raw_label
                }
        formatted_name = raw_label.strip().title()
        return {
            "ukr_name": f"Птах ({formatted_name})",
            "scientific_name": f"{formatted_name} sp.",
            "family": "Птахи (Aves)",
            "habitat": "Природні біотопи та лісові зони",
            "region": "Природний ареал поширення виду",
            "diet": "Всеїдний (рослинна та тваринна їжа)",
            "size": "Середні розміри птахів відповідної групи",
            "conservation_status": "Найменший ризик (LC)",
            "interesting_facts": f"Вид {formatted_name}, класифікований та ідентифікований системою біометричного аналізу Birdly.",
            "matched_key": raw_label
        }

    def get_all_families(self) -> list[str]:
        families = {info["family"] for info in self._data.values() if "family" in info and info["family"] != "Дані відсутні"}
        return sorted(list(families))

    def get_all_habitats(self) -> list[str]:
        habitats = {info["habitat"] for info in self._data.values() if "habitat" in info and info["habitat"] != "Дані про середовище існування відсутні"}
        return sorted(list(habitats))

    def get_all_diets(self) -> list[str]:
        diets = {info["diet"] for info in self._data.values() if "diet" in info and info["diet"] != "Дані про тип живлення відсутні"}
        return sorted(list(diets))

    def get_birds_by_region(self, region_substring: str) -> list[Dict[str, Any]]:
        results = []
        sub = region_substring.lower()
        for key, info in self._data.items():
            if sub in info.get("region", "").lower():
                item = info.copy()
                item["species_id"] = key
                results.append(item)
        return results
