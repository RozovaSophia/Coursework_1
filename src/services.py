import json
import re

from src.utils import read_csv_file


def search_for_transactions_by_individ():
    """возвращает только транзакции перевода физ.лицам"""
    data = read_csv_file("../data/operations.csv")
    pattern = re.compile(r"^[А-Я][а-я]+ [А-Я]\.$")
    transactions_for_individ = [
        row for row in data if row["Категория"] == "Переводы" and re.match(pattern, row["Описание"]) is not None
    ]
    result = json.dumps(transactions_for_individ, indent=4, ensure_ascii=False)
    return result


if __name__ == "__main__":
    result = search_for_transactions_by_individ()
    print(result)
