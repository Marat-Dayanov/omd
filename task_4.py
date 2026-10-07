"""
Есть статистика за пять дней работы магазина. У каждого дня число заказов, выручка и число возвратов.

Нужно найти:
- выручку за всю неделю
- день с самой большой выручкой
- среднюю выручку на один заказ в каждый день
- дни, где возвратов больше 20% заказов
"""

days = [
    {"day": "пн", "orders": 20, "revenue": 40_000, "returns": 2},
    {"day": "вт", "orders": 16, "revenue": 19_200, "returns": 4},
    {"day": "ср", "orders": 25, "revenue": 55_000, "returns": 1},
    {"day": "чт", "orders": 10, "revenue": 12_000, "returns": 3},
    {"day": "пт", "orders": 30, "revenue": 48_000, "returns": 3},
]

print("Выручка за всю неделю:", sum([day["revenue"] for day in days]))
max_revenue = max([day["revenue"] for day in days])
print("День с самой большой выручкой:", [day["day"] for day in days if day["revenue"] == max_revenue])
print("Средняя выручка на один заказ в каждый день:")
for day in days:
    print(f'{day["day"]} - {day["revenue"] / day["orders"]}')
print("Дни, где возвратов больше 20% заказов:",
      [day["day"] for day in days if day["returns"] / day["orders"] > 0.2])