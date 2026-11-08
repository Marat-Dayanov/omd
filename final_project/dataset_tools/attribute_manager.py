from copy import deepcopy


def delete_columns(data, columns: list[str]):
    """
    Удаляет из датасета перечисленные атрибуты и возращает полученный датасет.
    :param data: исходные данные
    :param columns: удаляемые атрибуты
    :return: данные без перечисленных атрибутов
    """
    result = []
    for row in data:
        new_row = {k: v for k, v in row.items() if k not in columns}
        result.append(new_row)
    return result


def add_column(data: list, column: str, values: list | None = None) -> list:
    """
    Добавляет в датасет новый атрибут.
    :param data: исходные данные
    :param column: название нового атрибута
    :param values: значения нового атрибута
    :return: данные с добавленным атрибутом
    """
    result = []
    if values is None:
        for row in data:
            new_row = row.copy()
            new_row[column] = None
            result.append(new_row)
        return result

    if len(data) != len(values):
        raise ValueError('Количество новых значений должно совпадать с количеством записей')

    for i in range(len(data)):
        new_row = data[i].copy()
        new_row[column] = values[i]
        result.append(new_row)
    return result


def get_column(data: list[dict], column: str) -> list:
    """
    Возращает значения атрибута в виде списка.
    :param data: данные
    :param column: атрибут
    :return: список значений атрибута
    """
    result = []
    for row in data:
        result.append(row[column])
    return result


def get_column_names(data: list[dict]) -> tuple[str]:
    """
    Возращает названия атрибутов датасета.
    :param data: датасет
    :return: названия атрибутов
    """
    if len(data) == 0:
        return tuple()
    return tuple(sorted(data[0].keys()))


def concat(data1: list[dict], data2: list[dict], axis: int = 0) -> list[dict]:
    """
    Склеивает 2 набора данных.
    При axis=0 получается новый набор, состоящий из строк 1 и 2 набора.
    При axis=1 получается новый набор с атрибутами 1 и 2 набора.
    :param data1: первый набор данных
    :param data2: второй набор данных
    :param axis: ось (0 или 1)
    :return: объединенный набор данных
    """
    if axis == 0:
        result = deepcopy(data1)
        columns1 = get_column_names(data1)
        columns2 = get_column_names(data2)
        if columns1 != columns2:
            raise ValueError('У наборов данных должны совпадать названия атрибутов')
        for row in data2:
            result.append(row)
        return result
    if axis == 1:
        if len(data1) != len(data2):
            raise ValueError('Наборы данных должны иметь одинаковый размер')
        result = deepcopy(data1)
        if len(data2) == 0:
            return result
        columns1 = get_column_names(data1)
        columns2 = get_column_names(data2)
        for column in columns2:
            if column in columns1:
                result = add_column(result, column + '_2', get_column(data2, column))
            else:
                result = add_column(result, column, get_column(data2, column))
        return result
    raise ValueError('Параметр axis должен равняться 0 или 1')


def flat(data: list) -> list:
    """
    Преобразовывает вложенную структуру списков в одномерный список.
    Пример: [[1, 2, 3], [], [[4]], [[[5, 6], 7]]] -> [1, 2, 3, 4, 5, 6, 7]
    :param data: данные в виде вложенных списков
    :return: одномерный список
    """
    result = []
    for item in data:
        if not isinstance(item, list):
            result.append(item)
            continue
        if len(item) == 0:
            continue
        flat_item = flat(item)
        for value in flat_item:
            result.append(value)
    return result


def get_columns(data: list[dict], columns: list[str] | None = None) -> dict[str, list]:
    """
    Преобразует данные вида [{атрибут1: значение, атрибут2: значение, ...}, ...] в вид
    {'атрибут1': [список значений], 'атрибут2': [список значений], ...}
    :param data: исходные данные
    :param columns: необходимые атрибуты
    :return: словарь с названием атрибутов и списком их значений
    """
    if len(data) == 0:
        return {}
    if columns is None:
        columns = get_column_names(data)
    return {
        column: get_column(data, column)
        for column in columns
    }
