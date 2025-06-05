import random

# 日本人の名前リスト（姓＋名）
japanese_names = [
    "佐藤 大輔", "鈴木 健太", "高橋 翔太", "田中 直樹", "伊藤 拓海",
    "渡辺 悠斗", "山本 亮", "中村 優", "小林 海斗", "加藤 陸",
    "吉田 颯太", "山田 智也", "佐々木 大地", "山口 直人", "松本 悠真",
    "井上 大和", "木村 智樹", "林 颯", "斎藤 陽斗", "清水 悠人",
    "山崎 陸斗", "森 拓真", "池田 颯太", "橋本 大輝", "阿部 直樹",
    "石川 悠斗", "山下 智也", "中島 大地", "小川 陽斗", "前田 颯"
]

# 外国人の名前リスト
foreign_names = [
    "Michael Johnson", "Usain Bolt", "Justin Gatlin", "Yohan Blake", "Asafa Powell",
    "Andre De Grasse", "Trayvon Bromell", "Akani Simbine", "Jimmy Vicaut", "Su Bingtian"
]

# 年齢リスト（20～27歳）
ages = list(range(20, 28))

# 選手リスト作成
athletes = []

# 日本人40人
for name in random.sample(japanese_names, 40):
    athlete = {
        "name": name,
        "age": random.choice(ages),
        "nationality": "日本",
        "time": round(random.uniform(9.56, 12.99), 2)
    }
    athletes.append(athlete)

# 外国人10人
for name in foreign_names:
    athlete = {
        "name": name,
        "age": random.choice(ages),
        "nationality": "外国",
        "time": round(random.uniform(9.56, 12.99), 2)
    }
    athletes.append(athlete)

# タイムが良い順に並び替え
athletes_sorted = sorted(athletes, key=lambda x: x["time"])

# 結果表示
print("100m走 選手リスト（タイムが良い順）")
print("順位 | 名前                | 年齢 | 国籍 | タイム(秒)")
print("-" * 50)
for i, athlete in enumerate(athletes_sorted, 1):
    print(f"{i:2d}位 | {athlete['name']:<18} | {athlete['age']}歳 | {athlete['nationality']} | {athlete['time']:.2f}")