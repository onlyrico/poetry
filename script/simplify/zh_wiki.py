# -*- coding: utf-8 -*-
# copy fom wikipedia

zhu = ['土著', '著作', '著名', '名著', '专著', '著称', '著有', '原著', '显著', '臭名昭著']

not_translated = ['乾坤', '乾隆', '康乾', '乾陵', '幺公']

for z in zhu:
    not_translated.append(z)

translated = {
    "菸": "烟",
    "勳": "勋",
    "㖭": "舔",
    "薑": "姜",
    "牠": "它",
    "溼": "湿",
    "瀋": "沈",
    "畫": "划",
    "鍾": "钟",
    "靦": "腼",
    "餘": "余",
    "鹼": "碱",
    "㠏": "㟆",
    "𡞵": "㛟",
    "万": "万",
    "与": "与",
    "丑": "丑",
    "丟": "丢",
    "並": "并",
    "丰": "丰",
    "么": "么",
    "乾": "干",
    "亂": "乱",
    "云": "云",
    "亙": "亘",
    "亞": "亚",
    "仆": "仆",
    "价": "价",
    "伙": "伙",
    "佇": "伫",
    "佈": "布",
    "体": "体",
    "余": "余",
    "佣": "佣",
    "併": "并",
    "來": "来",
    "侖": "仑",
    "侶": "侣",
    "俁": "俣",
    "係": "系",
    "俔": "伣",
    "俠": "侠",
    "倀": "伥",
    "倆": "俩",
    "倈": "俫",
    "倉": "仓",
    "個": "个",
    "們": "们",
    "倫": "伦",
    "偉": "伟",
    "側": "侧",
    "偵": "侦",
    "偽": "伪",
    "傑": "杰",
    "傖": "伧",
    "傘": "伞",
    "備": "备",
    "傢": "家",
    "傭": "佣",
    "傯": "偬",
    "傳": "传",
    "傴": "伛",
    "債": "债",
    "傷": "伤",
    "傾": "倾",
    "僂": "偻",
    "僅": "仅",
    "僉": "佥",
    "僑": "侨",
    "僕": "仆",
    "僞": "伪",
    "僥": "侥",
    "僨": "偾",
    "價": "价",
    "儀": "仪",
    "儂": "侬",
    "億": "亿",
    "儈": "侩",
    "儉": "俭",
    "儐": "傧",
    "儔": "俦",
    "儕": "侪",
    "儘": "尽",
    "償": "偿",
    "優": "优",
    "儲": "储",
    "儷": "俪",
    "儸": "㑩",
    "儺": "傩",
    "儻": "傥",
    "儼": "俨",
    "儿": "儿",
    "兇": "凶",
    "兌": "兑",
    "兒": "儿",
    "兗": "兖",
    "党": "党",
    "內": "内",
    "兩": "两",
    "冊": "册",
    "冪": "幂",
    "准": "准",
    "凈": "净",
    "凍": "冻",
    "凜": "凛",
    "几": "几",
    "凱": "凯",
    "划": "划",
    "別": "别",
    "刪": "删",
    "剄": "刭",
    "則": "则",
    "剎": "刹",
    "剗": "刬",
    "剛": "刚",
    "剝": "剥",
    "剮": "剐",
    "剴": "剀",
    "創": "创",
    "劃": "划",
    "劇": "剧",
    "劉": "刘",
    "劊": "刽",
    "劌": "刿",
    "劍": "剑",
    "劏": "㓥",
    "劑": "剂",
    "劚": "㔉",
    "勁": "劲",
    "動": "动",
    "務": "务",
    "勛": "勋",
    "勝": "胜",
    "勞": "劳",
    "勢": "势",
    "勩": "勚",
    "勱": "劢",
    "勵": "励",
    "勸": "劝",
    "勻": "匀",
    "匭": "匦",
    "匯": "汇",
    "匱": "匮",
    "區": "区",
    "協": "协",
    "卷": "卷",
    "卻": "却",
    "厂": "厂",
    "厙": "厍",
    "厠": "厕",
    "厭": "厌",
    "厲": "厉",
    "厴": "厣",
    "參": "参",
    "叄": "叁",
    "叢": "丛",
    "台": "台",
    "叶": "叶",
    "吊": "吊",
    "后": "后",
    "吳": "吴",
    "吶": "呐",
    "呂": "吕",
    "獃": "呆",
    "咼": "呙",
    "員": "员",
    "唄": "呗",
    "唚": "吣",
    "問": "问",
    "啓": "启",
    "啞": "哑",
    "啟": "启",
    "啢": "唡",
    "喎": "㖞",
    "喚": "唤",
    "喪": "丧",
    "喬": "乔",
    "單": "单",
    "喲": "哟",
    "嗆": "呛",
    "嗇": "啬",
    "嗊": "唝",
    "嗎": "吗",
    "嗚": "呜",
    "嗩": "唢",
    "嗶": "哔",
    "嘆": "叹",
    "嘍": "喽",
    "嘔": "呕",
    "嘖": "啧",
    "嘗": "尝",
    "嘜": "唛",
    "嘩": "哗",
    "嘮": "唠",
    "嘯": "啸",
    "嘰": "叽",
    "嘵": "哓",
    "嘸": "呒",
    "嘽": "啴",
    "噁": "恶",
    "噓": "嘘",
    "噚": "㖊",
    "噝": "咝",
    "噠": "哒",
    "噥": "哝",
    "噦": "哕",
    "噯": "嗳",
    "噲": "哙",
    "噴": "喷",
    "噸": "吨",
    "噹": "当",
    "嚀": "咛",
    "嚇": "吓",
    "嚌": "哜",
    "嚕": "噜",
    "嚙": "啮",
    "嚥": "咽",
    "嚦": "呖",
    "嚨": "咙",
    "嚮": "向",
    "嚲": "亸",
    "嚳": "喾",
    "嚴": "严",
    "嚶": "嘤",
    "囀": "啭",
    "囁": "嗫",
    "囂": "嚣",
    "囅": "冁",
    "囈": "呓",
    "囌": "苏",
    "囑": "嘱",
    "囪": "囱",
    "圇": "囵",
    "國": "国",
    "圍": "围",
    "園": "园",
    "圓": "圆",
    "圖": "图",
    "團": "团",
    "坏": "坏",
    "垵": "埯",
    "埡": "垭",
    "埰": "采",
    "執": "执",
    "堅": "坚",
    "堊": "垩",
    "堖": "垴",
    "堝": "埚",
    "堯": "尧",
    "報": "报",
    "場": "场",
    "塊": "块",
    "塋": "茔",
    "塏": "垲",
    "塒": "埘",
    "塗": "涂",
    "塚": "冢",
    "塢": "坞",
    "塤": "埙",
    "塵": "尘",
    "塹": "堑",
    "墊": "垫",
    "墜": "坠",
    "墮": "堕",
    "墳": "坟",
    "墻": "墙",
    "墾": "垦",
    "壇": "坛",
    "壈": "𡒄",
    "壋": "垱",
    "壓": "压",
    "壘": "垒",
    "壙": "圹",
    "壚": "垆",
    "壞": "坏",
    "壟": "垄",
    "壠": "垅",
    "壢": "坜",
    "壩": "坝",
    "壯": "壮",
    "壺": "壶",
    "壼": "壸",
    "壽": "寿",
    "夠": "够",
    "夢": "梦",
    "夾": "夹",
    "奐": "奂",
    "奧": "奥",
    "奩": "奁",
    "奪": "夺",
    "奬": "奖",
    "奮": "奋",
    "奼": "姹",
    "妝": "妆",
    "姍": "姗",
    "姜": "姜",
    "姦": "奸",
    "娛": "娱",
    "婁": "娄",
    "婦": "妇",
    "婭": "娅",
    "媧": "娲",
    "媯": "妫",
    "媼": "媪",
    "媽": "妈",
    "嫗": "妪",
    "嫵": "妩",
    "嫻": "娴",
    "嫿": "婳",
    "嬀": "妫",
    "嬈": "娆",
    "嬋": "婵",
    "嬌": "娇",
    "嬙": "嫱",
    "嬡": "嫒",
    "嬤": "嬷",
    "嬪": "嫔",
    "嬰": "婴",
    "嬸": "婶",
    "孌": "娈",
    "孫": "孙",
    "學": "学",
    "孿": "孪",
    "宁": "宁",
    "宮": "宫",
    "寢": "寝",
    "實": "实",
    "寧": "宁",
    "審": "审",
    "寫": "写",
    "寬": "宽",
    "寵": "宠",
    "寶": "宝",
    "將": "将",
    "專": "专",
    "尋": "寻",
    "對": "对",
    "導": "导",
    "尷": "尴",
    "屆": "届",
    "屍": "尸",
    "屓": "屃",
    "屜": "屉",
    "屢": "屡",
    "層": "层",
    "屨": "屦",
    "屬": "属",
    "岡": "冈",
    "峴": "岘",
    "島": "岛",
    "峽": "峡",
    "崍": "崃",
    "崗": "岗",
    "崢": "峥",
    "崬": "岽",
    "嵐": "岚",
    "嶁": "嵝",
    "嶄": "崭",
    "嶇": "岖",
    "嶔": "嵚",
    "嶗": "崂",
    "嶠": "峤",
    "嶢": "峣",
    "嶧": "峄",
    "嶮": "崄",
    "嶴": "岙",
    "嶸": "嵘",
    "嶺": "岭",
    "嶼": "屿",
    "嶽": "岳",
    "巋": "岿",
    "巒": "峦",
    "巔": "巅",
    "巰": "巯",
    "帘": "帘",
    "帥": "帅",
    "師": "师",
    "帳": "帐",
    "帶": "带",
    "幀": "帧",
    "幃": "帏",
    "幗": "帼",
    "幘": "帻",
    "幟": "帜",
    "幣": "币",
    "幫": "帮",
    "幬": "帱",
    "幹": "干",
    "幺": "么",
    "幾": "几",
    "广": "广",
    "庫": "库",
    "廁": "厕",
    "廂": "厢",
    "廄": "厩",
    "廈": "厦",
    "廚": "厨",
    "廝": "厮",
    "廟": "庙",
    "廠": "厂",
    "廡": "庑",
    "廢": "废",
    "廣": "广",
    "廩": "廪",
    "廬": "庐",
    "廳": "厅",
    "弒": "弑",
    "弳": "弪",
    "張": "张",
    "強": "强",
    "彆": "别",
    "彈": "弹",
    "彌": "弥",
    "彎": "弯",
    "彙": "汇",
    "彞": "彝",
    "彥": "彦",
    "征": "征",
    "後": "后",
    "徑": "径",
    "從": "从",
    "徠": "徕",
    "復": "复",
    "徵": "征",
    "徹": "彻",
    "志": "志",
    "恆": "恒",
    "恥": "耻",
    "悅": "悦",
    "悞": "悮",
    "悵": "怅",
    "悶": "闷",
    "惡": "恶",
    "惱": "恼",
    "惲": "恽",
    "惻": "恻",
    "愛": "爱",
    "愜": "惬",
    "愨": "悫",
    "愴": "怆",
    "愷": "恺",
    "愾": "忾",
    "愿": "愿",
    "慄": "栗",
    "態": "态",
    "慍": "愠",
    "慘": "惨",
    "慚": "惭",
    "慟": "恸",
    "慣": "惯",
    "慤": "悫",
    "慪": "怄",
    "慫": "怂",
    "慮": "虑",
    "慳": "悭",
    "慶": "庆",
    "憂": "忧",
    "憊": "惫",
    "憐": "怜",
    "憑": "凭",
    "憒": "愦",
    "憚": "惮",
    "憤": "愤",
    "憫": "悯",
    "憮": "怃",
    "憲": "宪",
    "憶": "忆",
    "懇": "恳",
    "應": "应",
    "懌": "怿",
    "懍": "懔",
    "懞": "蒙",
    "懟": "怼",
    "懣": "懑",
    "懨": "恹",
    "懲": "惩",
    "懶": "懒",
    "懷": "怀",
    "懸": "悬",
    "懺": "忏",
    "懼": "惧",
    "懾": "慑",
    "戀": "恋",
    "戇": "戆",
    "戔": "戋",
    "戧": "戗",
    "戩": "戬",
    "戰": "战",
    "戱": "戯",
    "戲": "戏",
    "戶": "户",
    "担": "担",
    "拋": "抛",
    "挩": "捝",
    "挾": "挟",
    "捨": "舍",
    "捫": "扪",
    "据": "据",
    "掃": "扫",
    "掄": "抡",
    "掗": "挜",
    "掙": "挣",
    "掛": "挂",
    "採": "采",
    "揀": "拣",
    "揚": "扬",
    "換": "换",
    "揮": "挥",
    "損": "损",
    "搖": "摇",
    "搗": "捣",
    "搵": "揾",
    "搶": "抢",
    "摑": "掴",
    "摜": "掼",
    "摟": "搂",
    "摯": "挚",
    "摳": "抠",
    "摶": "抟",
    "摺": "折",
    "摻": "掺",
    "撈": "捞",
    "撏": "挦",
    "撐": "撑",
    "撓": "挠",
    "撝": "㧑",
    "撟": "挢",
    "撣": "掸",
    "撥": "拨",
    "撫": "抚",
    "撲": "扑",
    "撳": "揿",
    "撻": "挞",
    "撾": "挝",
    "撿": "捡",
    "擁": "拥",
    "擄": "掳",
    "擇": "择",
    "擊": "击",
    "擋": "挡",
    "擓": "㧟",
    "擔": "担",
    "據": "据",
    "擠": "挤",
    "擬": "拟",
    "擯": "摈",
    "擰": "拧",
    "擱": "搁",
    "擲": "掷",
    "擴": "扩",
    "擷": "撷",
    "擺": "摆",
    "擻": "擞",
    "擼": "撸",
    "擾": "扰",
    "攄": "摅",
    "攆": "撵",
    "攏": "拢",
    "攔": "拦",
    "攖": "撄",
    "攙": "搀",
    "攛": "撺",
    "攜": "携",
    "攝": "摄",
    "攢": "攒",
    "攣": "挛",
    "攤": "摊",
    "攪": "搅",
    "攬": "揽",
    "敗": "败",
    "敘": "叙",
    "敵": "敌",
    "數": "数",
    "斂": "敛",
    "斃": "毙",
    "斕": "斓",
    "斗": "斗",
    "斬": "斩",
    "斷": "断",
    "於": "于",
    "時": "时",
    "晉": "晋",
    "晝": "昼",
    "暈": "晕",
    "暉": "晖",
    "暘": "旸",
    "暢": "畅",
    "暫": "暂",
    "曄": "晔",
    "曆": "历",
    "曇": "昙",
    "曉": "晓",
    "曏": "向",
    "曖": "暧",
    "曠": "旷",
    "曨": "昽",
    "曬": "晒",
    "書": "书",
    "會": "会",
    "朧": "胧",
    "朮": "术",
    "术": "术",
    "朴": "朴",
    "東": "东",
    "杴": "锨",
    "极": "极",
    "柜": "柜",
    "柵": "栅",
    "桿": "杆",
    "梔": "栀",
    "梘": "枧",
    "條": "条",
    "梟": "枭",
    "梲": "棁",
    "棄": "弃",
    "棖": "枨",
    "棗": "枣",
    "棟": "栋",
    "棧": "栈",
    "棲": "栖",
    "棶": "梾",
    "椏": "桠",
    "楊": "杨",
    "楓": "枫",
    "楨": "桢",
    "業": "业",
    "極": "极",
    "榪": "杩",
    "榮": "荣",
    "榲": "榅",
    "榿": "桤",
    "構": "构",
    "槍": "枪",
    "槤": "梿",
    "槧": "椠",
    "槨": "椁",
    "槳": "桨",
    "樁": "桩",
    "樂": "乐",
    "樅": "枞",
    "樓": "楼",
    "標": "标",
    "樞": "枢",
    "樣": "样",
    "樸": "朴",
    "樹": "树",
    "樺": "桦",
    "橈": "桡",
    "橋": "桥",
    "機": "机",
    "橢": "椭",
    "橫": "横",
    "檁": "檩",
    "檉": "柽",
    "檔": "档",
    "檜": "桧",
    "檟": "槚",
    "檢": "检",
    "檣": "樯",
    "檮": "梼",
    "檯": "台",
    "檳": "槟",
    "檸": "柠",
    "檻": "槛",
    "櫃": "柜",
    "櫓": "橹",
    "櫚": "榈",
    "櫛": "栉",
    "櫝": "椟",
    "櫞": "橼",
    "櫟": "栎",
    "櫥": "橱",
    "櫧": "槠",
    "櫨": "栌",
    "櫪": "枥",
    "櫫": "橥",
    "櫬": "榇",
    "櫱": "蘖",
    "櫳": "栊",
    "櫸": "榉",
    "櫻": "樱",
    "欄": "栏",
    "權": "权",
    "欏": "椤",
    "欒": "栾",
    "欖": "榄",
    "欞": "棂",
    "欽": "钦",
    "歐": "欧",
    "歟": "欤",
    "歡": "欢",
    "歲": "岁",
    "歷": "历",
    "歸": "归",
    "歿": "殁",
    "殘": "残",
    "殞": "殒",
    "殤": "殇",
    "殨": "㱮",
    "殫": "殚",
    "殮": "殓",
    "殯": "殡",
    "殰": "㱩",
    "殲": "歼",
    "殺": "杀",
    "殻": "壳",
    "殼": "壳",
    "毀": "毁",
    "毆": "殴",
    "毿": "毵",
    "氂": "牦",
    "氈": "毡",
    "氌": "氇",
    "氣": "气",
    "氫": "氢",
    "氬": "氩",
    "氳": "氲",
    "汙": "污",
    "決": "决",
    "沒": "没",
    "沖": "冲",
    "況": "况",
    "洶": "汹",
    "浹": "浃",
    "涂": "涂",
    "涇": "泾",
    "涼": "凉",
    "淀": "淀",
    "淒": "凄",
    "淚": "泪",
    "淥": "渌",
    "淨": "净",
    "淩": "凌",
    "淪": "沦",
    "淵": "渊",
    "淶": "涞",
    "淺": "浅",
    "渙": "涣",
    "減": "减",
    "渦": "涡",
    "測": "测",
    "渾": "浑",
    "湊": "凑",
    "湞": "浈",
    "湯": "汤",
    "溈": "沩",
    "準": "准",
    "溝": "沟",
    "溫": "温",
    "滄": "沧",
    "滅": "灭",
    "滌": "涤",
    "滎": "荥",
    "滬": "沪",
    "滯": "滞",
    "滲": "渗",
    "滷": "卤",
    "滸": "浒",
    "滻": "浐",
    "滾": "滚",
    "滿": "满",
    "漁": "渔",
    "漚": "沤",
    "漢": "汉",
    "漣": "涟",
    "漬": "渍",
    "漲": "涨",
    "漵": "溆",
    "漸": "渐",
    "漿": "浆",
    "潁": "颍",
    "潑": "泼",
    "潔": "洁",
    "潙": "沩",
    "潛": "潜",
    "潤": "润",
    "潯": "浔",
    "潰": "溃",
    "潷": "滗",
    "潿": "涠",
    "澀": "涩",
    "澆": "浇",
    "澇": "涝",
    "澐": "沄",
    "澗": "涧",
    "澠": "渑",
    "澤": "泽",
    "澦": "滪",
    "澩": "泶",
    "澮": "浍",
    "澱": "淀",
    "濁": "浊",
    "濃": "浓",
    "濕": "湿",
    "濘": "泞",
    "濛": "蒙",
    "濟": "济",
    "濤": "涛",
    "濫": "滥",
    "濰": "潍",
    "濱": "滨",
    "濺": "溅",
    "濼": "泺",
    "濾": "滤",
    "瀅": "滢",
    "瀆": "渎",
    "瀇": "㲿",
    "瀉": "泻",
    "瀋": "沈",
    "瀏": "浏",
    "瀕": "濒",
    "瀘": "泸",
    "瀝": "沥",
    "瀟": "潇",
    "瀠": "潆",
    "瀦": "潴",
    "瀧": "泷",
    "瀨": "濑",
    "瀰": "弥",
    "瀲": "潋",
    "瀾": "澜",
    "灃": "沣",
    "灄": "滠",
    "灑": "洒",
    "灕": "漓",
    "灘": "滩",
    "灝": "灏",
    "灠": "漤",
    "灣": "湾",
    "灤": "滦",
    "灧": "滟",
    "災": "灾",
    "為": "为",
    "烏": "乌",
    "烴": "烃",
    "無": "无",
    "煉": "炼",
    "煒": "炜",
    "煙": "烟",
    "煢": "茕",
    "煥": "焕",
    "煩": "烦",
    "煬": "炀",
    "煱": "㶽",
    "熅": "煴",
    "熒": "荧",
    "熗": "炝",
    "熱": "热",
    "熲": "颎",
    "熾": "炽",
    "燁": "烨",
    "燈": "灯",
    "燉": "炖",
    "燒": "烧",
    "燙": "烫",
    "燜": "焖",
    "營": "营",
    "燦": "灿",
    "燭": "烛",
    "燴": "烩",
    "燶": "㶶",
    "燼": "烬",
    "燾": "焘",
    "爍": "烁",
    "爐": "炉",
    "爛": "烂",
    "爭": "争",
    "爲": "为",
    "爺": "爷",
    "爾": "尔",
    "牆": "墙",
    "牘": "牍",
    "牽": "牵",
    "犖": "荦",
    "犢": "犊",
    "犧": "牺",
    "狀": "状",
    "狹": "狭",
    "狽": "狈",
    "猙": "狰",
    "猶": "犹",
    "猻": "狲",
    "獁": "犸",
    "獄": "狱",
    "獅": "狮",
    "獎": "奖",
    "獨": "独",
    "獪": "狯",
    "獫": "猃",
    "獮": "狝",
    "獰": "狞",
    "獱": "㺍",
    "獲": "获",
    "獵": "猎",
    "獷": "犷",
    "獸": "兽",
    "獺": "獭",
    "獻": "献",
    "獼": "猕",
    "玀": "猡",
    "現": "现",
    "琺": "珐",
    "琿": "珲",
    "瑋": "玮",
    "瑒": "玚",
    "瑣": "琐",
    "瑤": "瑶",
    "瑩": "莹",
    "瑪": "玛",
    "瑲": "玱",
    "璉": "琏",
    "璣": "玑",
    "璦": "瑷",
    "璫": "珰",
    "環": "环",
    "璽": "玺",
    "瓊": "琼",
    "瓏": "珑",
    "瓔": "璎",
    "瓚": "瓒",
    "甌": "瓯",
    "產": "产",
    "産": "产",
    "畝": "亩",
    "畢": "毕",
    "異": "异",
    "畵": "画",
    "當": "当",
    "疇": "畴",
    "疊": "叠",
    "痙": "痉",
    "痾": "疴",
    "瘂": "痖",
    "瘋": "疯",
    "瘍": "疡",
    "瘓": "痪",
    "瘞": "瘗",
    "瘡": "疮",
    "瘧": "疟",
    "瘮": "瘆",
    "瘲": "疭",
    "瘺": "瘘",
    "瘻": "瘘",
    "療": "疗",
    "癆": "痨",
    "癇": "痫",
    "癉": "瘅",
    "癘": "疠",
    "癟": "瘪",
    "癢": "痒",
    "癤": "疖",
    "癥": "症",
    "癧": "疬",
    "癩": "癞",
    "癬": "癣",
    "癭": "瘿",
    "癮": "瘾",
    "癰": "痈",
    "癱": "瘫",
    "癲": "癫",
    "發": "发",
    "皚": "皑",
    "皰": "疱",
    "皸": "皲",
    "皺": "皱",
    "盃": "杯",
    "盜": "盗",
    "盞": "盏",
    "盡": "尽",
    "監": "监",
    "盤": "盘",
    "盧": "卢",
    "盪": "荡",
    "眥": "眦",
    "眾": "众",
    "睏": "困",
    "睜": "睁",
    "睞": "睐",
    "瞘": "眍",
    "瞜": "䁖",
    "瞞": "瞒",
    "瞭": "了",
    "瞶": "瞆",
    "瞼": "睑",
    "矇": "蒙",
    "矓": "眬",
    "矚": "瞩",
    "矯": "矫",
    "硃": "朱",
    "硜": "硁",
    "硤": "硖",
    "硨": "砗",
    "确": "确",
    "硯": "砚",
    "碩": "硕",
    "碭": "砀",
    "碸": "砜",
    "確": "确",
    "碼": "码",
    "磑": "硙",
    "磚": "砖",
    "磣": "碜",
    "磧": "碛",
    "磯": "矶",
    "磽": "硗",
    "礆": "硷",
    "礎": "础",
    "礙": "碍",
    "礦": "矿",
    "礪": "砺",
    "礫": "砾",
    "礬": "矾",
    "礱": "砻",
    "祿": "禄",
    "禍": "祸",
    "禎": "祯",
    "禕": "祎",
    "禡": "祃",
    "禦": "御",
    "禪": "禅",
    "禮": "礼",
    "禰": "祢",
    "禱": "祷",
    "禿": "秃",
    "秈": "籼",
    "种": "种",
    "稅": "税",
    "稈": "秆",
    "稏": "䅉",
    "稟": "禀",
    "種": "种",
    "稱": "称",
    "穀": "谷",
    "穌": "稣",
    "積": "积",
    "穎": "颖",
    "穠": "秾",
    "穡": "穑",
    "穢": "秽",
    "穩": "稳",
    "穫": "获",
    "穭": "稆",
    "窩": "窝",
    "窪": "洼",
    "窮": "穷",
    "窯": "窑",
    "窵": "窎",
    "窶": "窭",
    "窺": "窥",
    "竄": "窜",
    "竅": "窍",
    "竇": "窦",
    "竈": "灶",
    "竊": "窃",
    "竪": "竖",
    "競": "竞",
    "筆": "笔",
    "筍": "笋",
    "筑": "筑",
    "筧": "笕",
    "筴": "䇲",
    "箋": "笺",
    "箏": "筝",
    "節": "节",
    "範": "范",
    "築": "筑",
    "篋": "箧",
    "篔": "筼",
    "篤": "笃",
    "篩": "筛",
    "篳": "筚",
    "簀": "箦",
    "簍": "篓",
    "簞": "箪",
    "簡": "简",
    "簣": "篑",
    "簫": "箫",
    "簹": "筜",
    "簽": "签",
    "簾": "帘",
    "籃": "篮",
    "籌": "筹",
    "籖": "签",
    "籙": "箓",
    "籜": "箨",
    "籟": "籁",
    "籠": "笼",
    "籩": "笾",
    "籪": "簖",
    "籬": "篱",
    "籮": "箩",
    "籲": "吁",
    "粵": "粤",
    "糝": "糁",
    "糞": "粪",
    "糧": "粮",
    "糰": "团",
    "糲": "粝",
    "糴": "籴",
    "糶": "粜",
    "糹": "纟",
    "糾": "纠",
    "紀": "纪",
    "紂": "纣",
    "約": "约",
    "紅": "红",
    "紆": "纡",
    "紇": "纥",
    "紈": "纨",
    "紉": "纫",
    "紋": "纹",
    "納": "纳",
    "紐": "纽",
    "紓": "纾",
    "純": "纯",
    "紕": "纰",
    "紖": "纼",
    "紗": "纱",
    "紘": "纮",
    "紙": "纸",
    "級": "级",
    "紛": "纷",
    "紜": "纭",
    "紝": "纴",
    "紡": "纺",
    "紬": "䌷",
    "細": "细",
    "紱": "绂",
    "紲": "绁",
    "紳": "绅",
    "紵": "纻",
    "紹": "绍",
    "紺": "绀",
    "紼": "绋",
    "紿": "绐",
    "絀": "绌",
    "終": "终",
    "組": "组",
    "絅": "䌹",
    "絆": "绊",
    "絎": "绗",
    "結": "结",
    "絕": "绝",
    "絛": "绦",
    "絝": "绔",
    "絞": "绞",
    "絡": "络",
    "絢": "绚",
    "給": "给",
    "絨": "绒",
    "絰": "绖",
    "統": "统",
    "絲": "丝",
    "絳": "绛",
    "絶": "绝",
    "絹": "绢",
    "綁": "绑",
    "綃": "绡",
    "綆": "绠",
    "綈": "绨",
    "綉": "绣",
    "綌": "绤",
    "綏": "绥",
    "綐": "䌼",
    "經": "经",
    "綜": "综",
    "綞": "缍",
    "綠": "绿",
    "綢": "绸",
    "綣": "绻",
    "綫": "线",
    "綬": "绶",
    "維": "维",
    "綯": "绹",
    "綰": "绾",
    "綱": "纲",
    "網": "网",
    "綳": "绷",
    "綴": "缀",
    "綵": "䌽",
    "綸": "纶",
    "綹": "绺",
    "綺": "绮",
    "綻": "绽",
    "綽": "绰",
    "綾": "绫",
    "綿": "绵",
    "緄": "绲",
    "緇": "缁",
    "緊": "紧",
    "緋": "绯",
    "緑": "绿",
    "緒": "绪",
    "緓": "绬",
    "緔": "绱",
    "緗": "缃",
    "緘": "缄",
    "緙": "缂",
    "線": "线",
    "緝": "缉",
    "緞": "缎",
    "締": "缔",
    "緡": "缗",
    "緣": "缘",
    "緦": "缌",
    "編": "编",
    "緩": "缓",
    "緬": "缅",
    "緯": "纬",
    "緱": "缑",
    "緲": "缈",
    "練": "练",
    "緶": "缏",
    "緹": "缇",
    "緻": "致",
    "縈": "萦",
    "縉": "缙",
    "縊": "缢",
    "縋": "缒",
    "縐": "绉",
    "縑": "缣",
    "縕": "缊",
    "縗": "缞",
    "縛": "缚",
    "縝": "缜",
    "縞": "缟",
    "縟": "缛",
    "縣": "县",
    "縧": "绦",
    "縫": "缝",
    "縭": "缡",
    "縮": "缩",
    "縱": "纵",
    "縲": "缧",
    "縳": "䌸",
    "縴": "纤",
    "縵": "缦",
    "縶": "絷",
    "縷": "缕",
    "縹": "缥",
    "總": "总",
    "績": "绩",
    "繃": "绷",
    "繅": "缫",
    "繆": "缪",
    "繒": "缯",
    "織": "织",
    "繕": "缮",
    "繚": "缭",
    "繞": "绕",
    "繡": "绣",
    "繢": "缋",
    "繩": "绳",
    "繪": "绘",
    "繫": "系",
    "繭": "茧",
    "繮": "缰",
    "繯": "缳",
    "繰": "缲",
    "繳": "缴",
    "繸": "䍁",
    "繹": "绎",
    "繼": "继",
    "繽": "缤",
    "繾": "缱",
    "繿": "䍀",
    "纈": "缬",
    "纊": "纩",
    "續": "续",
    "纍": "累",
    "纏": "缠",
    "纓": "缨",
    "纔": "才",
    "纖": "纤",
    "纘": "缵",
    "纜": "缆",
    "缽": "钵",
    "罈": "坛",
    "罌": "罂",
    "罰": "罚",
    "罵": "骂",
    "罷": "罢",
    "羅": "罗",
    "羆": "罴",
    "羈": "羁",
    "羋": "芈",
    "羥": "羟",
    "義": "义",
    "習": "习",
    "翹": "翘",
    "耬": "耧",
    "耮": "耢",
    "聖": "圣",
    "聞": "闻",
    "聯": "联",
    "聰": "聪",
    "聲": "声",
    "聳": "耸",
    "聵": "聩",
    "聶": "聂",
    "職": "职",
    "聹": "聍",
    "聽": "听",
    "聾": "聋",
    "肅": "肃",
    "胜": "胜",
    "脅": "胁",
    "脈": "脉",
    "脛": "胫",
    "脫": "脱",
    "脹": "胀",
    "腊": "腊",
    "腎": "肾",
    "腖": "胨",
    "腡": "脶",
    "腦": "脑",
    "腫": "肿",
    "腳": "脚",
    "腸": "肠",
    "膃": "腽",
    "膚": "肤",
    "膠": "胶",
    "膩": "腻",
    "膽": "胆",
    "膾": "脍",
    "膿": "脓",
    "臉": "脸",
    "臍": "脐",
    "臏": "膑",
    "臘": "腊",
    "臚": "胪",
    "臟": "脏",
    "臠": "脔",
    "臢": "臜",
    "臥": "卧",
    "臨": "临",
    "臺": "台",
    "與": "与",
    "興": "兴",
    "舉": "举",
    "舊": "旧",
    "艙": "舱",
    "艤": "舣",
    "艦": "舰",
    "艫": "舻",
    "艱": "艰",
    "艷": "艳",
    "芻": "刍",
    "苧": "苎",
    "苹": "苹",
    "范": "范",
    "茲": "兹",
    "荊": "荆",
    "莊": "庄",
    "莖": "茎",
    "莢": "荚",
    "莧": "苋",
    "華": "华",
    "萇": "苌",
    "萊": "莱",
    "萬": "万",
    "萵": "莴",
    "葉": "叶",
    "葒": "荭",
    "著": "着",
    "葤": "荮",
    "葦": "苇",
    "葯": "药",
    "葷": "荤",
    "蒓": "莼",
    "蒔": "莳",
    "蒞": "莅",
    "蒼": "苍",
    "蓀": "荪",
    "蓋": "盖",
    "蓮": "莲",
    "蓯": "苁",
    "蓴": "莼",
    "蓽": "荜",
    "蔔": "卜",
    "蔞": "蒌",
    "蔣": "蒋",
    "蔥": "葱",
    "蔦": "茑",
    "蔭": "荫",
    "蕁": "荨",
    "蕆": "蒇",
    "蕎": "荞",
    "蕒": "荬",
    "蕓": "芸",
    "蕕": "莸",
    "蕘": "荛",
    "蕢": "蒉",
    "蕩": "荡",
    "蕪": "芜",
    "蕭": "萧",
    "蕷": "蓣",
    "薀": "蕰",
    "薈": "荟",
    "薊": "蓟",
    "薌": "芗",
    "薔": "蔷",
    "薘": "荙",
    "薟": "莶",
    "薦": "荐",
    "薩": "萨",
    "薳": "䓕",
    "薴": "苧",
    "薺": "荠",
    "藉": "借",
    "藍": "蓝",
    "藎": "荩",
    "藝": "艺",
    "藥": "药",
    "藪": "薮",
    "藴": "蕴",
    "藶": "苈",
    "藹": "蔼",
    "藺": "蔺",
    "蘄": "蕲",
    "蘆": "芦",
    "蘇": "苏",
    "蘊": "蕴",
    "蘋": "苹",
    "蘚": "藓",
    "蘞": "蔹",
    "蘢": "茏",
    "蘭": "兰",
    "蘺": "蓠",
    "蘿": "萝",
    "虆": "蔂",
    "處": "处",
    "虛": "虚",
    "虜": "虏",
    "號": "号",
    "虧": "亏",
    "虫": "虫",
    "虯": "虬",
    "蛺": "蛱",
    "蛻": "蜕",
    "蜆": "蚬",
    "蜡": "蜡",
    "蝕": "蚀",
    "蝟": "猬",
    "蝦": "虾",
    "蝸": "蜗",
    "螄": "蛳",
    "螞": "蚂",
    "螢": "萤",
    "螮": "䗖",
    "螻": "蝼",
    "螿": "螀",
    "蟄": "蛰",
    "蟈": "蝈",
    "蟎": "螨",
    "蟣": "虮",
    "蟬": "蝉",
    "蟯": "蛲",
    "蟲": "虫",
    "蟶": "蛏",
    "蟻": "蚁",
    "蠅": "蝇",
    "蠆": "虿",
    "蠐": "蛴",
    "蠑": "蝾",
    "蠟": "蜡",
    "蠣": "蛎",
    "蠨": "蟏",
    "蠱": "蛊",
    "蠶": "蚕",
    "蠻": "蛮",
    "衆": "众",
    "衊": "蔑",
    "術": "术",
    "衕": "同",
    "衚": "胡",
    "衛": "卫",
    "衝": "冲",
    "衹": "只",
    "袞": "衮",
    "裊": "袅",
    "裏": "里",
    "補": "补",
    "裝": "装",
    "裡": "里",
    "製": "制",
    "複": "复",
    "褌": "裈",
    "褘": "袆",
    "褲": "裤",
    "褳": "裢",
    "褸": "褛",
    "褻": "亵",
    "襇": "裥",
    "襏": "袯",
    "襖": "袄",
    "襝": "裣",
    "襠": "裆",
    "襤": "褴",
    "襪": "袜",
    "襬": "䙓",
    "襯": "衬",
    "襲": "袭",
    "覆蓋": "覆盖",
    "翻來覆去": "翻来覆去",
    "見": "见",
    "覎": "觃",
    "規": "规",
    "覓": "觅",
    "視": "视",
    "覘": "觇",
    "覡": "觋",
    "覥": "觍",
    "覦": "觎",
    "親": "亲",
    "覬": "觊",
    "覯": "觏",
    "覲": "觐",
    "覷": "觑",
    "覺": "觉",
    "覽": "览",
    "覿": "觌",
    "觀": "观",
    "觴": "觞",
    "觶": "觯",
    "觸": "触",
    "訁": "讠",
    "訂": "订",
    "訃": "讣",
    "計": "计",
    "訊": "讯",
    "訌": "讧",
    "討": "讨",
    "訐": "讦",
    "訒": "讱",
    "訓": "训",
    "訕": "讪",
    "訖": "讫",
    "託": "讬",
    "記": "记",
    "訛": "讹",
    "訝": "讶",
    "訟": "讼",
    "訢": "䜣",
    "訣": "诀",
    "訥": "讷",
    "訩": "讻",
    "訪": "访",
    "設": "设",
    "許": "许",
    "訴": "诉",
    "訶": "诃",
    "診": "诊",
    "註": "注",
    "詁": "诂",
    "詆": "诋",
    "詎": "讵",
    "詐": "诈",
    "詒": "诒",
    "詔": "诏",
    "評": "评",
    "詖": "诐",
    "詗": "诇",
    "詘": "诎",
    "詛": "诅",
    "詞": "词",
    "詠": "咏",
    "詡": "诩",
    "詢": "询",
    "詣": "诣",
    "試": "试",
    "詩": "诗",
    "詫": "诧",
    "詬": "诟",
    "詭": "诡",
    "詮": "诠",
    "詰": "诘",
    "話": "话",
    "該": "该",
    "詳": "详",
    "詵": "诜",
    "詼": "诙",
    "詿": "诖",
    "誄": "诔",
    "誅": "诛",
    "誆": "诓",
    "誇": "夸",
    "誌": "志",
    "認": "认",
    "誑": "诳",
    "誒": "诶",
    "誕": "诞",
    "誘": "诱",
    "誚": "诮",
    "語": "语",
    "誠": "诚",
    "誡": "诫",
    "誣": "诬",
    "誤": "误",
    "誥": "诰",
    "誦": "诵",
    "誨": "诲",
    "說": "说",
    "説": "说",
    "誰": "谁",
    "課": "课",
    "誶": "谇",
    "誹": "诽",
    "誼": "谊",
    "誾": "訚",
    "調": "调",
    "諂": "谄",
    "諄": "谆",
    "談": "谈",
    "諉": "诿",
    "請": "请",
    "諍": "诤",
    "諏": "诹",
    "諑": "诼",
    "諒": "谅",
    "論": "论",
    "諗": "谂",
    "諛": "谀",
    "諜": "谍",
    "諝": "谞",
    "諞": "谝",
    "諢": "诨",
    "諤": "谔",
    "諦": "谛",
    "諧": "谐",
    "諫": "谏",
    "諭": "谕",
    "諮": "谘",
    "諱": "讳",
    "諳": "谙",
    "諶": "谌",
    "諷": "讽",
    "諸": "诸",
    "諺": "谚",
    "諼": "谖",
    "諾": "诺",
    "謀": "谋",
    "謁": "谒",
    "謂": "谓",
    "謄": "誊",
    "謅": "诌",
    "謊": "谎",
    "謎": "谜",
    "謐": "谧",
    "謔": "谑",
    "謖": "谡",
    "謗": "谤",
    "謙": "谦",
    "謚": "谥",
    "講": "讲",
    "謝": "谢",
    "謠": "谣",
    "謡": "谣",
    "謨": "谟",
    "謫": "谪",
    "謬": "谬",
    "謭": "谫",
    "謳": "讴",
    "謹": "谨",
    "謾": "谩",
    "譅": "䜧",
    "證": "证",
    "譎": "谲",
    "譏": "讥",
    "譖": "谮",
    "識": "识",
    "譙": "谯",
    "譚": "谭",
    "譜": "谱",
    "譫": "谵",
    "譯": "译",
    "議": "议",
    "譴": "谴",
    "護": "护",
    "譸": "诪",
    "譽": "誉",
    "譾": "谫",
    "讀": "读",
    "變": "变",
    "讎": "仇",
    "讎": "雠",
    "讒": "谗",
    "讓": "让",
    "讕": "谰",
    "讖": "谶",
    "讜": "谠",
    "讞": "谳",
    "豈": "岂",
    "豎": "竖",
    "豐": "丰",
    "豬": "猪",
    "豶": "豮",
    "貓": "猫",
    "貙": "䝙",
    "貝": "贝",
    "貞": "贞",
    "貟": "贠",
    "負": "负",
    "財": "财",
    "貢": "贡",
    "貧": "贫",
    "貨": "货",
    "販": "贩",
    "貪": "贪",
    "貫": "贯",
    "責": "责",
    "貯": "贮",
    "貰": "贳",
    "貲": "赀",
    "貳": "贰",
    "貴": "贵",
    "貶": "贬",
    "買": "买",
    "貸": "贷",
    "貺": "贶",
    "費": "费",
    "貼": "贴",
    "貽": "贻",
    "貿": "贸",
    "賀": "贺",
    "賁": "贲",
    "賂": "赂",
    "賃": "赁",
    "賄": "贿",
    "賅": "赅",
    "資": "资",
    "賈": "贾",
    "賊": "贼",
    "賑": "赈",
    "賒": "赊",
    "賓": "宾",
    "賕": "赇",
    "賙": "赒",
    "賚": "赉",
    "賜": "赐",
    "賞": "赏",
    "賠": "赔",
    "賡": "赓",
    "賢": "贤",
    "賣": "卖",
    "賤": "贱",
    "賦": "赋",
    "賧": "赕",
    "質": "质",
    "賫": "赍",
    "賬": "账",
    "賭": "赌",
    "賰": "䞐",
    "賴": "赖",
    "賵": "赗",
    "賺": "赚",
    "賻": "赙",
    "購": "购",
    "賽": "赛",
    "賾": "赜",
    "贄": "贽",
    "贅": "赘",
    "贇": "赟",
    "贈": "赠",
    "贊": "赞",
    "贋": "赝",
    "贍": "赡",
    "贏": "赢",
    "贐": "赆",
    "贓": "赃",
    "贔": "赑",
    "贖": "赎",
    "贗": "赝",
    "贛": "赣",
    "贜": "赃",
    "赬": "赪",
    "趕": "赶",
    "趙": "赵",
    "趨": "趋",
    "趲": "趱",
    "跡": "迹",
    "踐": "践",
    "踴": "踊",
    "蹌": "跄",
    "蹕": "跸",
    "蹣": "蹒",
    "蹤": "踪",
    "蹺": "跷",
    "躂": "跶",
    "躉": "趸",
    "躊": "踌",
    "躋": "跻",
    "躍": "跃",
    "躑": "踯",
    "躒": "跞",
    "躓": "踬",
    "躕": "蹰",
    "躚": "跹",
    "躡": "蹑",
    "躥": "蹿",
    "躦": "躜",
    "躪": "躏",
    "軀": "躯",
    "車": "车",
    "軋": "轧",
    "軌": "轨",
    "軍": "军",
    "軑": "轪",
    "軒": "轩",
    "軔": "轫",
    "軛": "轭",
    "軟": "软",
    "軤": "轷",
    "軫": "轸",
    "軲": "轱",
    "軸": "轴",
    "軹": "轵",
    "軺": "轺",
    "軻": "轲",
    "軼": "轶",
    "軾": "轼",
    "較": "较",
    "輅": "辂",
    "輇": "辁",
    "輈": "辀",
    "載": "载",
    "輊": "轾",
    "輒": "辄",
    "輓": "挽",
    "輔": "辅",
    "輕": "轻",
    "輛": "辆",
    "輜": "辎",
    "輝": "辉",
    "輞": "辋",
    "輟": "辍",
    "輥": "辊",
    "輦": "辇",
    "輩": "辈",
    "輪": "轮",
    "輬": "辌",
    "輯": "辑",
    "輳": "辏",
    "輸": "输",
    "輻": "辐",
    "輾": "辗",
    "輿": "舆",
    "轀": "辒",
    "轂": "毂",
    "轄": "辖",
    "轅": "辕",
    "轆": "辘",
    "轉": "转",
    "轍": "辙",
    "轎": "轿",
    "轔": "辚",
    "轟": "轰",
    "轡": "辔",
    "轢": "轹",
    "轤": "轳",
    "辟": "辟",
    "辦": "办",
    "辭": "辞",
    "辮": "辫",
    "辯": "辩",
    "農": "农",
    "迴": "回",
    "适": "适",
    "逕": "迳",
    "這": "这",
    "連": "连",
    "週": "周",
    "進": "进",
    "遊": "游",
    "運": "运",
    "過": "过",
    "達": "达",
    "違": "违",
    "遙": "遥",
    "遜": "逊",
    "遞": "递",
    "遠": "远",
    "適": "适",
    "遲": "迟",
    "遷": "迁",
    "選": "选",
    "遺": "遗",
    "遼": "辽",
    "邁": "迈",
    "還": "还",
    "邇": "迩",
    "邊": "边",
    "邏": "逻",
    "邐": "逦",
    "郁": "郁",
    "郟": "郏",
    "郵": "邮",
    "鄆": "郓",
    "鄉": "乡",
    "鄒": "邹",
    "鄔": "邬",
    "鄖": "郧",
    "鄧": "邓",
    "鄭": "郑",
    "鄰": "邻",
    "鄲": "郸",
    "鄴": "邺",
    "鄶": "郐",
    "鄺": "邝",
    "酇": "酂",
    "酈": "郦",
    "醖": "酝",
    "醜": "丑",
    "醞": "酝",
    "醫": "医",
    "醬": "酱",
    "醱": "酦",
    "釀": "酿",
    "釁": "衅",
    "釃": "酾",
    "釅": "酽",
    "采": "采",
    "釋": "释",
    "釐": "厘",
    "釒": "钅",
    "釓": "钆",
    "釔": "钇",
    "釕": "钌",
    "釗": "钊",
    "釘": "钉",
    "釙": "钋",
    "針": "针",
    "釣": "钓",
    "釤": "钐",
    "釧": "钏",
    "釩": "钒",
    "釵": "钗",
    "釷": "钍",
    "釹": "钕",
    "釺": "钎",
    "鈀": "钯",
    "鈁": "钫",
    "鈃": "钘",
    "鈄": "钭",
    "鈈": "钚",
    "鈉": "钠",
    "鈍": "钝",
    "鈎": "钩",
    "鈐": "钤",
    "鈑": "钣",
    "鈒": "钑",
    "鈔": "钞",
    "鈕": "钮",
    "鈞": "钧",
    "鈣": "钙",
    "鈥": "钬",
    "鈦": "钛",
    "鈧": "钪",
    "鈮": "铌",
    "鈰": "铈",
    "鈳": "钶",
    "鈴": "铃",
    "鈷": "钴",
    "鈸": "钹",
    "鈹": "铍",
    "鈺": "钰",
    "鈽": "钸",
    "鈾": "铀",
    "鈿": "钿",
    "鉀": "钾",
    "鉅": "钜",
    "鉈": "铊",
    "鉉": "铉",
    "鉋": "铇",
    "鉍": "铋",
    "鉑": "铂",
    "鉕": "钷",
    "鉗": "钳",
    "鉚": "铆",
    "鉛": "铅",
    "鉞": "钺",
    "鉢": "钵",
    "鉤": "钩",
    "鉦": "钲",
    "鉬": "钼",
    "鉭": "钽",
    "鉶": "铏",
    "鉸": "铰",
    "鉺": "铒",
    "鉻": "铬",
    "鉿": "铪",
    "銀": "银",
    "銃": "铳",
    "銅": "铜",
    "銍": "铚",
    "銑": "铣",
    "銓": "铨",
    "銖": "铢",
    "銘": "铭",
    "銚": "铫",
    "銛": "铦",
    "銜": "衔",
    "銠": "铑",
    "銣": "铷",
    "銥": "铱",
    "銦": "铟",
    "銨": "铵",
    "銩": "铥",
    "銪": "铕",
    "銫": "铯",
    "銬": "铐",
    "銱": "铞",
    "銳": "锐",
    "銷": "销",
    "銹": "锈",
    "銻": "锑",
    "銼": "锉",
    "鋁": "铝",
    "鋃": "锒",
    "鋅": "锌",
    "鋇": "钡",
    "鋌": "铤",
    "鋏": "铗",
    "鋒": "锋",
    "鋙": "铻",
    "鋝": "锊",
    "鋟": "锓",
    "鋣": "铘",
    "鋤": "锄",
    "鋥": "锃",
    "鋦": "锔",
    "鋨": "锇",
    "鋩": "铓",
    "鋪": "铺",
    "鋭": "锐",
    "鋮": "铖",
    "鋯": "锆",
    "鋰": "锂",
    "鋱": "铽",
    "鋶": "锍",
    "鋸": "锯",
    "鋼": "钢",
    "錁": "锞",
    "錄": "录",
    "錆": "锖",
    "錇": "锫",
    "錈": "锩",
    "錏": "铔",
    "錐": "锥",
    "錒": "锕",
    "錕": "锟",
    "錘": "锤",
    "錙": "锱",
    "錚": "铮",
    "錛": "锛",
    "錟": "锬",
    "錠": "锭",
    "錡": "锜",
    "錢": "钱",
    "錦": "锦",
    "錨": "锚",
    "錩": "锠",
    "錫": "锡",
    "錮": "锢",
    "錯": "错",
    "録": "录",
    "錳": "锰",
    "錶": "表",
    "錸": "铼",
    "鍀": "锝",
    "鍁": "锨",
    "鍃": "锪",
    "鍆": "钔",
    "鍇": "锴",
    "鍈": "锳",
    "鍋": "锅",
    "鍍": "镀",
    "鍔": "锷",
    "鍘": "铡",
    "鍚": "钖",
    "鍛": "锻",
    "鍠": "锽",
    "鍤": "锸",
    "鍥": "锲",
    "鍩": "锘",
    "鍬": "锹",
    "鍰": "锾",
    "鍵": "键",
    "鍶": "锶",
    "鍺": "锗",
    "鍾": "钟",
    "鎂": "镁",
    "鎄": "锿",
    "鎇": "镅",
    "鎊": "镑",
    "鎔": "镕",
    "鎖": "锁",
    "鎘": "镉",
    "鎚": "锤",
    "鎛": "镈",
    "鎝": "𨱏",
    "鎡": "镃",
    "鎢": "钨",
    "鎣": "蓥",
    "鎦": "镏",
    "鎧": "铠",
    "鎩": "铩",
    "鎪": "锼",
    "鎬": "镐",
    "鎮": "镇",
    "鎰": "镒",
    "鎲": "镋",
    "鎳": "镍",
    "鎵": "镓",
    "鎸": "镌",
    "鎿": "镎",
    "鏃": "镞",
    "鏇": "镟",
    "鏈": "链",
    "鏌": "镆",
    "鏍": "镙",
    "鏐": "镠",
    "鏑": "镝",
    "鏗": "铿",
    "鏘": "锵",
    "鏜": "镗",
    "鏝": "镘",
    "鏞": "镛",
    "鏟": "铲",
    "鏡": "镜",
    "鏢": "镖",
    "鏤": "镂",
    "鏨": "錾",
    "鏰": "镚",
    "鏵": "铧",
    "鏷": "镤",
    "鏹": "镪",
    "鏽": "锈",
    "鐃": "铙",
    "鐋": "铴",
    "鐐": "镣",
    "鐒": "铹",
    "鐓": "镦",
    "鐔": "镡",
    "鐘": "钟",
    "鐙": "镫",
    "鐝": "镢",
    "鐠": "镨",
    "鐦": "锎",
    "鐧": "锏",
    "鐨": "镄",
    "鐫": "镌",
    "鐮": "镰",
    "鐲": "镯",
    "鐳": "镭",
    "鐵": "铁",
    "鐶": "镮",
    "鐸": "铎",
    "鐺": "铛",
    "鐿": "镱",
    "鑄": "铸",
    "鑊": "镬",
    "鑌": "镔",
    "鑒": "鉴",
    "鑔": "镲",
    "鑕": "锧",
    "鑞": "镴",
    "鑠": "铄",
    "鑣": "镳",
    "鑥": "镥",
    "鑭": "镧",
    "鑰": "钥",
    "鑱": "镵",
    "鑲": "镶",
    "鑷": "镊",
    "鑹": "镩",
    "鑼": "锣",
    "鑽": "钻",
    "鑾": "銮",
    "鑿": "凿",
    "钁": "镢",
    "镟": "旋",
    "長": "长",
    "門": "门",
    "閂": "闩",
    "閃": "闪",
    "閆": "闫",
    "閈": "闬",
    "閉": "闭",
    "開": "开",
    "閌": "闶",
    "閎": "闳",
    "閏": "闰",
    "閑": "闲",
    "間": "间",
    "閔": "闵",
    "閘": "闸",
    "閡": "阂",
    "閣": "阁",
    "閤": "合",
    "閥": "阀",
    "閨": "闺",
    "閩": "闽",
    "閫": "阃",
    "閬": "阆",
    "閭": "闾",
    "閱": "阅",
    "閲": "阅",
    "閶": "阊",
    "閹": "阉",
    "閻": "阎",
    "閼": "阏",
    "閽": "阍",
    "閾": "阈",
    "閿": "阌",
    "闃": "阒",
    "闆": "板",
    "闈": "闱",
    "闊": "阔",
    "闋": "阕",
    "闌": "阑",
    "闍": "阇",
    "闐": "阗",
    "闒": "阘",
    "闓": "闿",
    "闔": "阖",
    "闕": "阙",
    "闖": "闯",
    "關": "关",
    "闞": "阚",
    "闠": "阓",
    "闡": "阐",
    "闤": "阛",
    "闥": "闼",
    "阪": "坂",
    "陘": "陉",
    "陝": "陕",
    "陣": "阵",
    "陰": "阴",
    "陳": "陈",
    "陸": "陆",
    "陽": "阳",
    "隉": "陧",
    "隊": "队",
    "階": "阶",
    "隕": "陨",
    "際": "际",
    "隨": "随",
    "險": "险",
    "隱": "隐",
    "隴": "陇",
    "隸": "隶",
    "隻": "只",
    "雋": "隽",
    "雖": "虽",
    "雙": "双",
    "雛": "雏",
    "雜": "杂",
    "雞": "鸡",
    "離": "离",
    "難": "难",
    "雲": "云",
    "電": "电",
    "霢": "霡",
    "霧": "雾",
    "霽": "霁",
    "靂": "雳",
    "靄": "霭",
    "靈": "灵",
    "靚": "靓",
    "靜": "静",
    "靨": "靥",
    "鞀": "鼗",
    "鞏": "巩",
    "鞝": "绱",
    "鞦": "秋",
    "鞽": "鞒",
    "韁": "缰",
    "韃": "鞑",
    "韆": "千",
    "韉": "鞯",
    "韋": "韦",
    "韌": "韧",
    "韍": "韨",
    "韓": "韩",
    "韙": "韪",
    "韜": "韬",
    "韞": "韫",
    "韻": "韵",
    "響": "响",
    "頁": "页",
    "頂": "顶",
    "頃": "顷",
    "項": "项",
    "順": "顺",
    "頇": "顸",
    "須": "须",
    "頊": "顼",
    "頌": "颂",
    "頎": "颀",
    "頏": "颃",
    "預": "预",
    "頑": "顽",
    "頒": "颁",
    "頓": "顿",
    "頗": "颇",
    "領": "领",
    "頜": "颌",
    "頡": "颉",
    "頤": "颐",
    "頦": "颏",
    "頭": "头",
    "頮": "颒",
    "頰": "颊",
    "頲": "颋",
    "頴": "颕",
    "頷": "颔",
    "頸": "颈",
    "頹": "颓",
    "頻": "频",
    "頽": "颓",
    "顆": "颗",
    "題": "题",
    "額": "额",
    "顎": "颚",
    "顏": "颜",
    "顒": "颙",
    "顓": "颛",
    "顔": "颜",
    "願": "愿",
    "顙": "颡",
    "顛": "颠",
    "類": "类",
    "顢": "颟",
    "顥": "颢",
    "顧": "顾",
    "顫": "颤",
    "顬": "颥",
    "顯": "显",
    "顰": "颦",
    "顱": "颅",
    "顳": "颞",
    "顴": "颧",
    "風": "风",
    "颭": "飐",
    "颮": "飑",
    "颯": "飒",
    "颱": "台",
    "颳": "刮",
    "颶": "飓",
    "颸": "飔",
    "颺": "飏",
    "颻": "飖",
    "颼": "飕",
    "飀": "飗",
    "飄": "飘",
    "飆": "飙",
    "飈": "飚",
    "飛": "飞",
    "飠": "饣",
    "飢": "饥",
    "飣": "饤",
    "飥": "饦",
    "飩": "饨",
    "飪": "饪",
    "飫": "饫",
    "飭": "饬",
    "飯": "饭",
    "飲": "饮",
    "飴": "饴",
    "飼": "饲",
    "飽": "饱",
    "飾": "饰",
    "飿": "饳",
    "餃": "饺",
    "餄": "饸",
    "餅": "饼",
    "餉": "饷",
    "養": "养",
    "餌": "饵",
    "餎": "饹",
    "餏": "饻",
    "餑": "饽",
    "餒": "馁",
    "餓": "饿",
    "餕": "馂",
    "餖": "饾",
    "餚": "肴",
    "餛": "馄",
    "餜": "馃",
    "餞": "饯",
    "餡": "馅",
    "館": "馆",
    "餱": "糇",
    "餳": "饧",
    "餶": "馉",
    "餷": "馇",
    "餺": "馎",
    "餼": "饩",
    "餾": "馏",
    "餿": "馊",
    "饁": "馌",
    "饃": "馍",
    "饅": "馒",
    "饈": "馐",
    "饉": "馑",
    "饊": "馓",
    "饋": "馈",
    "饌": "馔",
    "饑": "饥",
    "饒": "饶",
    "饗": "飨",
    "饜": "餍",
    "饞": "馋",
    "饢": "馕",
    "馬": "马",
    "馭": "驭",
    "馮": "冯",
    "馱": "驮",
    "馳": "驰",
    "馴": "驯",
    "馹": "驲",
    "駁": "驳",
    "駐": "驻",
    "駑": "驽",
    "駒": "驹",
    "駔": "驵",
    "駕": "驾",
    "駘": "骀",
    "駙": "驸",
    "駛": "驶",
    "駝": "驼",
    "駟": "驷",
    "駡": "骂",
    "駢": "骈",
    "駭": "骇",
    "駰": "骃",
    "駱": "骆",
    "駸": "骎",
    "駿": "骏",
    "騁": "骋",
    "騂": "骍",
    "騅": "骓",
    "騌": "骔",
    "騍": "骒",
    "騎": "骑",
    "騏": "骐",
    "騖": "骛",
    "騙": "骗",
    "騤": "骙",
    "騧": "䯄",
    "騫": "骞",
    "騭": "骘",
    "騮": "骝",
    "騰": "腾",
    "騶": "驺",
    "騷": "骚",
    "騸": "骟",
    "騾": "骡",
    "驀": "蓦",
    "驁": "骜",
    "驂": "骖",
    "驃": "骠",
    "驄": "骢",
    "驅": "驱",
    "驊": "骅",
    "驌": "骕",
    "驍": "骁",
    "驏": "骣",
    "驕": "骄",
    "驗": "验",
    "驚": "惊",
    "驛": "驿",
    "驟": "骤",
    "驢": "驴",
    "驤": "骧",
    "驥": "骥",
    "驦": "骦",
    "驪": "骊",
    "驫": "骉",
    "骯": "肮",
    "髏": "髅",
    "髒": "脏",
    "體": "体",
    "髕": "髌",
    "髖": "髋",
    "髮": "发",
    "鬆": "松",
    "鬍": "胡",
    "鬚": "须",
    "鬢": "鬓",
    "鬥": "斗",
    "鬧": "闹",
    "鬩": "阋",
    "鬮": "阄",
    "鬱": "郁",
    "魎": "魉",
    "魘": "魇",
    "魚": "鱼",
    "魛": "鱽",
    "魢": "鱾",
    "魨": "鲀",
    "魯": "鲁",
    "魴": "鲂",
    "魷": "鱿",
    "魺": "鲄",
    "鮁": "鲅",
    "鮃": "鲆",
    "鮊": "鲌",
    "鮋": "鲉",
    "鮍": "鲏",
    "鮎": "鲇",
    "鮐": "鲐",
    "鮑": "鲍",
    "鮒": "鲋",
    "鮓": "鲊",
    "鮚": "鲒",
    "鮜": "鲘",
    "鮝": "鲞",
    "鮞": "鲕",
    "鮦": "鲖",
    "鮪": "鲔",
    "鮫": "鲛",
    "鮭": "鲑",
    "鮮": "鲜",
    "鮳": "鲓",
    "鮶": "鲪",
    "鮺": "鲝",
    "鯀": "鲧",
    "鯁": "鲠",
    "鯇": "鲩",
    "鯉": "鲤",
    "鯊": "鲨",
    "鯒": "鲬",
    "鯔": "鲻",
    "鯕": "鲯",
    "鯖": "鲭",
    "鯗": "鲞",
    "鯛": "鲷",
    "鯝": "鲴",
    "鯡": "鲱",
    "鯢": "鲵",
    "鯤": "鲲",
    "鯧": "鲳",
    "鯨": "鲸",
    "鯪": "鲮",
    "鯫": "鲰",
    "鯴": "鲺",
    "鯷": "鳀",
    "鯽": "鲫",
    "鯿": "鳊",
    "鰁": "鳈",
    "鰂": "鲗",
    "鰃": "鳂",
    "鰈": "鲽",
    "鰉": "鳇",
    "鰍": "鳅",
    "鰏": "鲾",
    "鰐": "鳄",
    "鰒": "鳆",
    "鰓": "鳃",
    "鰜": "鳒",
    "鰟": "鳑",
    "鰠": "鳋",
    "鰣": "鲥",
    "鰥": "鳏",
    "鰨": "鳎",
    "鰩": "鳐",
    "鰭": "鳍",
    "鰮": "鳁",
    "鰱": "鲢",
    "鰲": "鳌",
    "鰳": "鳓",
    "鰵": "鳘",
    "鰷": "鲦",
    "鰹": "鲣",
    "鰺": "鲹",
    "鰻": "鳗",
    "鰼": "鳛",
    "鰾": "鳔",
    "鱂": "鳉",
    "鱅": "鳙",
    "鱈": "鳕",
    "鱉": "鳖",
    "鱒": "鳟",
    "鱔": "鳝",
    "鱖": "鳜",
    "鱗": "鳞",
    "鱘": "鲟",
    "鱝": "鲼",
    "鱟": "鲎",
    "鱠": "鲙",
    "鱣": "鳣",
    "鱤": "鳡",
    "鱧": "鳢",
    "鱨": "鲿",
    "鱭": "鲚",
    "鱯": "鳠",
    "鱷": "鳄",
    "鱸": "鲈",
    "鱺": "鲡",
    "䰾": "鲃",
    "䲁": "鳚",
    "鳥": "鸟",
    "鳧": "凫",
    "鳩": "鸠",
    "鳬": "凫",
    "鳲": "鸤",
    "鳳": "凤",
    "鳴": "鸣",
    "鳶": "鸢",
    "鳾": "䴓",
    "鴆": "鸩",
    "鴇": "鸨",
    "鴉": "鸦",
    "鴒": "鸰",
    "鴕": "鸵",
    "鴛": "鸳",
    "鴝": "鸲",
    "鴞": "鸮",
    "鴟": "鸱",
    "鴣": "鸪",
    "鴦": "鸯",
    "鴨": "鸭",
    "鴯": "鸸",
    "鴰": "鸹",
    "鴴": "鸻",
    "鴷": "䴕",
    "鴻": "鸿",
    "鴿": "鸽",
    "鵁": "䴔",
    "鵂": "鸺",
    "鵃": "鸼",
    "鵐": "鹀",
    "鵑": "鹃",
    "鵒": "鹆",
    "鵓": "鹁",
    "鵜": "鹈",
    "鵝": "鹅",
    "鵠": "鹄",
    "鵡": "鹉",
    "鵪": "鹌",
    "鵬": "鹏",
    "鵮": "鹐",
    "鵯": "鹎",
    "鵲": "鹊",
    "鵷": "鹓",
    "鵾": "鹍",
    "鶄": "䴖",
    "鶇": "鸫",
    "鶉": "鹑",
    "鶊": "鹒",
    "鶓": "鹋",
    "鶖": "鹙",
    "鶘": "鹕",
    "鶚": "鹗",
    "鶡": "鹖",
    "鶥": "鹛",
    "鶩": "鹜",
    "鶪": "䴗",
    "鶬": "鸧",
    "鶯": "莺",
    "鶲": "鹟",
    "鶴": "鹤",
    "鶹": "鹠",
    "鶺": "鹡",
    "鶻": "鹘",
    "鶼": "鹣",
    "鶿": "鹚",
    "鷀": "鹚",
    "鷁": "鹢",
    "鷂": "鹞",
    "鷄": "鸡",
    "鷈": "䴘",
    "鷊": "鹝",
    "鷓": "鹧",
    "鷖": "鹥",
    "鷗": "鸥",
    "鷙": "鸷",
    "鷚": "鹨",
    "鷥": "鸶",
    "鷦": "鹪",
    "鷫": "鹔",
    "鷯": "鹩",
    "鷲": "鹫",
    "鷳": "鹇",
    "鷸": "鹬",
    "鷹": "鹰",
    "鷺": "鹭",
    "鷽": "鸴",
    "鷿": "䴙",
    "鸂": "㶉",
    "鸇": "鹯",
    "鸌": "鹱",
    "鸏": "鹲",
    "鸕": "鸬",
    "鸘": "鹴",
    "鸚": "鹦",
    "鸛": "鹳",
    "鸝": "鹂",
    "鸞": "鸾",
    "鹵": "卤",
    "鹹": "咸",
    "鹺": "鹾",
    "鹽": "盐",
    "麗": "丽",
    "麥": "麦",
    "麩": "麸",
    "麯": "曲",
    "麵": "面",
    "麼": "么",
    "麽": "么",
    "黃": "黄",
    "黌": "黉",
    "點": "点",
    "黨": "党",
    "黲": "黪",
    "黴": "霉",
    "黶": "黡",
    "黷": "黩",
    "黽": "黾",
    "黿": "鼋",
    "鼉": "鼍",
    "鼕": "冬",
    "鼴": "鼹",
    "齊": "齐",
    "齋": "斋",
    "齎": "赍",
    "齏": "齑",
    "齒": "齿",
    "齔": "龀",
    "齕": "龁",
    "齗": "龂",
    "齙": "龅",
    "齜": "龇",
    "齟": "龃",
    "齠": "龆",
    "齡": "龄",
    "齣": "出",
    "齦": "龈",
    "齪": "龊",
    "齬": "龉",
    "齲": "龋",
    "齶": "腭",
    "齷": "龌",
    "龍": "龙",
    "龎": "厐",
    "龐": "庞",
    "龔": "龚",
    "龕": "龛",
    "龜": "龟",
    "鯰": "鲶",
    "舖": "铺",
    "慾": "欲",
    "佔": "占",
    "湧": "涌",
    "妳": "你",
    "祂": "他",

    '顯著': '显著',
    "或著": "或者",

    "了嚒": "了么",
    "甦醒": "苏醒",
    "幽茫": "幽芒",
    "麻痺": "麻痺",

    "捲心菜": "卷心菜",
    "捲成": "卷成"
}

zh2Hans = {}

for n in not_translated:
    zh2Hans[n] = n

for k in translated:
    zh2Hans[k] = translated[k]
