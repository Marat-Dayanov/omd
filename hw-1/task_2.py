"""
Дана история поисковых запросов: каждая строка — один введённый запрос.
Повтор в списке значит, что этот запрос ввели ещё раз.

Нужно найти:
- сколько всего поисковых запросов в ленте
- сколько раз ввели каждый запрос
- какой запрос вводили чаще всего
- какую долю всех поисков он занимает
- какие запросы встретились один раз
"""
from collections import Counter


def main():
    queries = [
        "чехол",
        "iphone",
        "чехол",
        "наушники",
        "iphone",
        "iphone",
        "кабель",
        "чехол",
        "iphone",
    ]

    print("Всего поисковых запросов в ленте:", len(queries))
    counter = Counter(queries)
    print("Cколько раз ввели каждый запрос:")
    for k, v in counter.items():
        print(k, "-", v)
    print("Чаще всего вводили запрос:", counter.most_common(1)[0][0])
    print("Его доля среди всех поисков:", max(counter.values()) / len(queries))
    print("Встретились один раз:",
          [query for query, amount in counter.items() if amount == 1])


if __name__ == '__main__':
    main()
