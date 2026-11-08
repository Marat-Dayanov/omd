def extract_nested_value(obj, keys):
    """
    Достает значение из словаря по указанному пути.
    :param obj: словарь
    :param keys: путь
    :return: значение
    """
    result = obj
    for key in keys:
        if key not in result:
            return None
        result = result[key]
    return result


def process_dictionary_with_config(dictionary, config):
    """
    Преобразует данные в указанную конфигурацией структуру.
    :param dictionary: данные
    :param config: конфигурация
    :return: структурированные данные
    """
    result = {}
    for attribute in config:
        if isinstance(config[attribute], tuple):
            path, func = config[attribute]
            result[attribute] = func(extract_nested_value(dictionary, path))
        else:
            result[attribute] = extract_nested_value(dictionary, config[attribute])
    return result


def process_list_of_dicts_with_config(list_of_dicts, config):
    """
    Преобразует данные в указанную конфигурацией структуру для каждого элемента списка.
    :param list_of_dicts: список с данными
    :param config: конфигурация
    :return: список структурированных данных
    """
    result = []
    for dictionary in list_of_dicts:
        result.append(process_dictionary_with_config(dictionary, config))
    return result


def create_processor(config, list_processor=False):
    """
    Создает сконфигурированную функцию для обработки данных
    :param config: конфигурация
    :param list_processor: обрабатывает ли функция списки данных
    :return: функция для обработки данных
    """
    if list_processor:
        return lambda list_of_dicts: process_list_of_dicts_with_config(list_of_dicts, config)
    return lambda dictionary: process_dictionary_with_config(dictionary, config)