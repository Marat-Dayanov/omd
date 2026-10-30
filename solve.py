import csv
from typing import Any
from collections import defaultdict

FILE = 'Corp_Summary.csv'
FIELDS_NAME = ('name', 'department', 'team', 'job_title', 'rating', 'salary')
OUTPUT_FILE = 'report.csv'


def avg(numbers: list[int | float]) -> float:
    """
    Считает среднее арифметическое значение списка чисел
    :param numbers: список чисел
    :return: среднее значение
    """
    return sum(numbers) / len(numbers)


def read() -> list[dict[str, Any]]:
    """
    Считывает информацию о сотрудниках из файла. Записывает информацию о каждом
    сотруднике в словарь и возвращает список этих словарей.
    :return: Список с информацией о сотрудниках
    """
    data = []
    with open(FILE, encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)
        for row in reader:
            record = dict(zip(
                FIELDS_NAME,
                (row[0], row[1], row[2], row[3], float(row[4]), int(row[5]))
            ))
            data.append(record)
    return data


def report_1(data: list[dict[str, Any]]) -> None:
    """
    Для каждого департамента показывает, какие команды в него входят.
    Выводит эту информацию на экран.
    :param data: Данные о сотрудниках
    :return:
    """
    result = defaultdict(set)
    for employee in data:
        result[employee['department']].add(employee['team'])

    for department in result:
        print(department)
        for team in result[department]:
            print('-', team)
        print()


def get_departments_info(data: list[dict[str, Any]]) -> dict[str, tuple]:
    """
    Формирует сводку по департаментам: название, сколько человек, минимальная и
    максимальная зарплата, средняя по каждому департаменту.
    :param data: Данные о сотрудниках
    :return: Сводка по департаментам
    """
    department_salaries = defaultdict(list)
    for employee in data:
        department_salaries[employee['department']].append(employee['salary'])

    result = {}
    for department in department_salaries:
        salaries = department_salaries[department]
        result[department] = (
            len(salaries),
            min(salaries),
            max(salaries),
            round(avg(salaries), 2)
        )
    return result


def report_2(data: list[dict[str, Any]]) -> None:
    """
    Получает сводку по департаментам и выводит ее на экран.
    :param data: Данные о сотрудниках
    :return:
    """
    departments_info = get_departments_info(data)
    for department in departments_info:
        info = departments_info[department]
        print(department)
        print(f'Количество сотрудников = {info[0]}')
        print(f'Минимальная зарплата = {info[1]}')
        print(f'Максимальная зарплата = {info[2]}')
        print(f'Средняя зарплата = {info[3]}')
        print()


def report_3(data: list[dict[str, Any]]) -> None:
    """
    Получает сводку по департаментам и записывает ее в файл.
    :param data: Данные о сотрудниках
    :return:
    """
    output = [['Департамент', 'Количество сотрудников', 'Минимальная зарплата',
               'Максимальная зарплата', 'Средняя зарплата']]
    departments_info = get_departments_info(data)
    for department in departments_info:
        output.append([department, *departments_info[department]])

    with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(output)


def report(report_number: int) -> None:
    """
    Формирует отчет по заданному номеру.
    :param report_number: Номер отчета
    :return:
    """
    if report_number not in (1, 2, 3):
        raise ValueError('Invalid report number')

    reports = [None, report_1, report_2, report_3]
    reports[report_number](read())


def main():
    report_number = int(input('Введите номер отчета: '))
    report(report_number)


if __name__ == '__main__':
    main()
