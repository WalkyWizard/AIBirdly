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
