"""
Есть список заказов:
- `status` - статус заказа
    - `delivered` доставлен покупателю
    - `returned` возврат
- `amount` — сумма заказа.

Нужно найти:
- на какую сумму оформили возвраты
- кто хотя бы раз вернул заказ
- сколько заказов доставлено покупателю
- средний чек доставленных заказов
"""


def main():
    orders = [
        {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
        {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
        {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
        {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
        {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
        {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100},
    ]

    print("Сумма возвратов:",
          sum([order["amount"] for order in orders if order["status"] == "returned"]))
    print("Хотя бы раз вернули заказ:",
          set([order["buyer"] for order in orders if order["status"] == "returned"]))
    delivered_orders_number = sum([1 for order in orders if order["status"] == "delivered"])
    print("Количество доставленных заказов:", delivered_orders_number)
    print("Средний чек доставленных заказов:",
          sum([order["amount"] for order in orders
               if order["status"] == "delivered"]) / delivered_orders_number)


if __name__ == '__main__':
    main()
