import csv
import datetime
import json
import os
from typing import Any

import pandas as pd

PATH = os.path.dirname(os.path.abspath(__file__))


def decorator_for_writing_to_file(filename=None):
    """декоратор принимает параметры"""

    def decorator(func):
        """декоратор записывает результат в отдельный файл в папке /data"""
        try:

            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)

                if filename:
                    file_name = filename
                else:
                    func_name = func.__name__
                    file_name = os.path.join("..", "data", f"{func_name}.json")

                with open(file_name, "w", encoding="utf-8") as f:
                    json.dump(json.loads(result), f, indent=4, ensure_ascii=False)
                return result

        except FileNotFoundError as e:
            print(f"Ошибка:{e}")

        return wrapper

    return decorator


def returns_dataframe_format():
    """считывает файл operations.csv и возвращает его как DataFrame"""
    try:
        with open(os.path.join(PATH, "..", "data", "operations.csv"), "r", newline="", encoding="UTF-8") as f:
            reader = csv.DictReader(f, delimiter=",")
            data = list(reader)
            transactions = pd.DataFrame(data)
            return transactions
    except FileNotFoundError as e:
        return f"Ошибка: {e}"


def spending_by_category(transactions: pd.DataFrame, category: str, date: str = None) -> str | Any:
    """принимает транзакции в виде DataFrame, возвращает сумму операций по определенной категории
    за определенное время"""
    try:
        if date is None:
            date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

        transactions["Сумма операции"] = transactions["Сумма операции"].str.replace(",", ".").str.strip().astype(float)

        date_obj = datetime.datetime.strptime(date, "%d.%m.%Y %H:%M:%S")
        three_months_ago = date_obj - datetime.timedelta(days=90)
        filtered_transactions = []
        for transaction in transactions.to_dict("records"):
            date_obj_csv = datetime.datetime.strptime(transaction["Дата операции"], "%d.%m.%Y %H:%M:%S")
            if three_months_ago <= date_obj_csv <= date_obj:
                try:
                    if category == "Все категории" or transaction["Категория"] == category:
                        filtered_transactions.append(transaction)
                except KeyError as e:
                    return f"Ошибка: {e}"
        filtered_transactions = pd.DataFrame(filtered_transactions)
        result = (
            filtered_transactions.groupby("Категория")["Сумма операции"].sum().to_json(indent=4, force_ascii=False)
        )

        return result

    except TypeError as e:
        return f"Oшибка: {e}"
    except ValueError as e:
        return f"Ошибка: {e}"
    except KeyError as e:
        return f"Ошибка: {e}"


spending_by_category_decorated = decorator_for_writing_to_file()(spending_by_category)

if __name__ == "__main__":
    transactions = returns_dataframe_format()
    spending_by_category = decorator_for_writing_to_file()(spending_by_category)
    result = spending_by_category(transactions, "Перевод", "31.12.2021 16:44:00")
    print(result)
