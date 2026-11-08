from collections import defaultdict
from typing import Any, Callable
from frozendict import frozendict
from functools import cmp_to_key


def group_by(data: list[dict], columns: list[str]) -> dict[frozendict[str, Any], list[dict]]:
    """
    Группирует данные по указанным атрибутам.
    :param data: данные
    :param columns: атрибуты
    :return: словарь {группа: список строк}
    """
    result = defaultdict(list)
    for row in data:
        result[frozendict({column: row[column] for column in columns})].append(row)
    return dict(result)


def where(data: list[dict], predicate: Callable[[Any], bool]) -> list[dict]:
    """
    Фильтрует данные по указанному предикату.
    :param data: данные
    :param predicate: предикат
    :return: набор строк, для которых предикат верен
    """
    result = []
    for row in data:
        if predicate(row):
            result.append(row)
    return result


def sort_values(data: list[dict], columns: list[str],
                ascending: list[bool] | None = None) -> list[dict]:
    """
    Сортирует данные по указанным атрибутам в указанном порядке.
    :param data: данные
    :param columns: атрибуты
    :param ascending: порядок сортировки (True - сортировка по соот. атрибуту идет по возрастанию,
    False - в обратном порядке)
    :return: отсортированный набор данных
    """
    if ascending is None:
        ascending = [True] * len(columns)
    if len(ascending) != len(columns):
        raise ValueError(
            'Длина ascending должна совпадать с числом атрибутов, по которым проводится сортировка.')

    def compare(a, b):
        for i in range(len(columns)):
            if ascending[i]:
                if a[columns[i]] > b[columns[i]]:
                    return 1
                if a[columns[i]] < b[columns[i]]:
                    return -1
            else:
                if a[columns[i]] > b[columns[i]]:
                    return -1
                if a[columns[i]] < b[columns[i]]:
                    return 1
        return 0

    return list(sorted(
        data,
        key=cmp_to_key(compare)
    ))


def apply(data: list[dict], func: Callable) -> list:
    """
    Применяет функцию к каждой строчке датасета
    :param data: данные
    :param func: функция
    :return: список результатов
    """
    return list(map(func, data))

