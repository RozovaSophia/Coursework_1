import csv
import datetime
import os

import pandas as pd


def decorator_for_writing_to_file(filename=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if filename:
                file_name = filename
            else:
                func_name = func.__name__
                file_name = os.path.join("..", "data", f"{func_name}.txt")

            with open(file_name, "w", encoding="utf-8") as f:
                f.write(str(result))

            return result

        return wrapper

    return decorator


def returns_dataframe_format(file_path="../data/operations.csv"):
    with open(file_path, "r", newline="", encoding="UTF-8") as f:
        reader = csv.DictReader(f, delimiter=",")
        data = list(reader)
        transactions = pd.DataFrame(data)
        return transactions


@decorator_for_writing_to_file()
def spending_by_category(transactions: pd.DataFrame, category: str, date: str = None) -> pd.DataFrame:
    if date is None:
        date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    transactions["Сумма операции"] = transactions["Сумма операции"].str.replace(",", ".").str.strip().astype(float)

    date_obj = datetime.datetime.strptime(date, "%d.%m.%Y %H:%M:%S")
    three_months_ago = date_obj - datetime.timedelta(days=90)
    filtered_transactions = []
    for transaction in transactions.to_dict("records"):
        date_obj_csv = datetime.datetime.strptime(transaction["Дата операции"], "%d.%m.%Y %H:%M:%S")
        if three_months_ago <= date_obj_csv <= date_obj:
            if category == "Все категории" or transaction["Категория"] == category:
                filtered_transactions.append(transaction)
    filtered_transactions = pd.DataFrame(filtered_transactions)
    result = filtered_transactions.groupby("Категория")["Сумма операции"].sum()

    return result


if __name__ == "__main__":
    transactions = returns_dataframe_format()
    result = spending_by_category(transactions, "Супермаркеты", "31.12.2021 16:44:00")
    print(result)
