import json
import sqlite3

def get_list(sqlite_query):
    """
    функция подключается к бд и выводит запрос в виде списка кортежей только с использованием sqlite3.Row row_factory
    :param sqlite_query: str sql запрос
    :return: list
    """
    with sqlite3.connect("animal.db") as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(sqlite_query)
        list_db = cursor.fetchall()

    return list_db


def get_json_item(num_item):
    """
    функция, принимает число и выводит транзакцию в бд с данным числом
    :param num_item:
    :return:
    """

    query = f"""
        SELECT *
        FROM fin_ledger
        WHERE id = {num_item}
        """

    return [dict(result) for result in get_list(query)]





