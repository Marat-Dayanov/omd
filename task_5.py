"""
Есть список отзывов на товары. На каждой строке — по одному.
Данные слегка битые, и названия товара записаны в разном регистре.
`id` при этом один и тот же для одного и того же товара.
Перед подсчётом приведите названия к одному формату, иначе они будут считаться как разные.

Нужно найти:

- среднюю оценку каждого товара
- худший товар по средней оценке среди тех, у кого хотя бы два отзыва
- сколько отзывов на 1 или 2 звезды
- какую долю всех отзывов они составляют
"""
from collections import defaultdict, Counter

reviews = [
    {"id": 1, "product": "Чехол", "stars": 5},
    {"id": 1, "product": "Чехол", "stars": 3},
    {"id": 1, "product": "Чехол", "stars": 4},
    {"id": 2, "product": "Наушники", "stars": 2},
    {"id": 2, "product": "наушники", "stars": 2},
    {"id": 2, "product": "НАУШНИКИ", "stars": 5},
    {"id": 3, "product": "Планшет", "stars": 5},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 5, "product": "Кабель", "stars": 1},
]

for review in reviews:
    review["product"] = review["product"].lower()

product_sum_stars = defaultdict(int)
for review in reviews:
    product_sum_stars[review["product"]] += review["stars"]

product_review_number = Counter([review["product"] for review in reviews])
products = set([review["product"] for review in reviews])
product_average_rating = {product: product_sum_stars[product] / product_review_number[product]
                          for product in products}
print(product_average_rating)

products_with_two_or_more_reviews = [product for product in products
                                     if product_review_number[product] >= 2]
min_average_rating = min(product_average_rating[product] for product in products_with_two_or_more_reviews)
print([product for product in products_with_two_or_more_reviews
       if product_average_rating[product] == min_average_rating])

bad_reviews_amount = sum([1 for review in reviews if review["stars"] in (1, 2)])
print(bad_reviews_amount)

print(bad_reviews_amount / len(reviews))
