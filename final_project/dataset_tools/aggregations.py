from statistics import fmean, median, mode, variance, stdev
from typing import Any

from dataset_tools.attribute_manager import get_column


def _drop_nones(values: list) -> list:
    """
    Убирает из списка None и возвращает полученный список.
    :param values: исходный список
    :return: список без None
    """
    return [value for value in values if value is not None]


AGGREGATIONS = {
    'sum': lambda values: sum(_drop_nones(values)),
    'min': lambda values: min(_drop_nones(values)),
    'max': lambda values: max(_drop_nones(values)),
    'median': lambda values: median(_drop_nones(values)),
    'mode': lambda values: mode(_drop_nones(values)),
    'var': lambda values: variance(_drop_nones(values)),
    'std': lambda values: stdev(_drop_nones(values)),
    'mean': lambda values: fmean(_drop_nones(values)),
    'count': lambda values: len(_drop_nones(values)),
    'nunique': lambda values: len(set(values)),
    'none_count': lambda values: len(values) - len(_drop_nones(values)),
    'argmax': lambda values: [i for i in range(len(values)) if values[i] == max(values)],
    'argmin': lambda values: [i for i in range(len(values)) if values[i] == min(values)],
}


def agg(data: list | dict, func: str | dict[str, str | list[str]]) -> dict[str, Any] | list[dict[str, Any]]:
    """
    Агрегирует данные при помощи заданных агрегатных функций.

    Функция может быть задана одной строкой (в этом случае эта функция применяется ко всем атрибутам)
    или словарем {атрибут: функция / набор функций} (агрегируются только указанные атрибуты при помощи
    указанных функций).

    Если передан не группированный датасет, то возращается словарь с результатами агрегации.
    Если датасет группирован, то для каждой группы применяется агрегирование и возвращается список словарей
    с результатами агрегации и атрибутами группировки
    :param data: датасет
    :param func: агрегационная функция
    :return: новый датасет с результатами агрегации
    """
    if isinstance(data, list):
        if len(data) == 0:
            return {}

        result = {}
        columns = data[0].keys()
        if isinstance(func, str):
            func = {column: func for column in columns}
        for column in func:
            if isinstance(func[column], list):
                for f in func[column]:
                    result[f'{column}_{f}'] = AGGREGATIONS[f](get_column(data, column))
            else:
                result[f"{column}_{func[column]}"] = AGGREGATIONS[func[column]](get_column(data, column))
        return result
    elif isinstance(data, dict):
        result = []
        for group, rows in data.items():
            agg_result = agg(rows, func)
            for column in group:
                agg_result[column] = group[column]
            result.append(agg_result)
        return result
    raise TypeError('Данные должны представлять из себя список или словарь')
