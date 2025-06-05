import random

# 商品リスト（20種類）
products = [
    "りんご", "バナナ", "牛乳", "パン", "卵", "チーズ", "トマト", "きゅうり", "にんじん", "玉ねぎ",
    "お米", "鶏肉", "豚肉", "牛肉", "魚", "ヨーグルト", "ジュース", "お菓子", "コーヒー", "紅茶"
]

# 商品ごとの価格（100円～1000円でランダムに設定）
product_prices = {name: random.randint(100, 1000) for name in products}

# かごの中身をカメラで認識したと仮定してランダムに商品を選ぶ（例：5～10個）
basket = random.choices(products, k=random.randint(5, 10))

# 合計金額計算
total = sum(product_prices[item] for item in basket)

# 結果表示
print("かごの中身：")
for item in basket:
    print(f"{item}：{product_prices[item]}円")
print("-" * 30)
print(f"合計金額：{total}円")