import json
import logging
import os
import re

from src.utils import read_csv_file

PATH = os.path.dirname(os.path.abspath(__file__))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="logging.log",
    filemode="w",
    encoding="utf-8",
)

services_logger = logging.getLogger("services")


def search_for_transactions_by_individ():
    """возвращает только транзакции перевода физ.лицам"""
    data = read_csv_file(os.path.join(PATH, "..", "data", "operations.csv"))
    pattern = re.compile(r"^[А-Я][а-я]+ [А-Я]\.$")
    transactions_for_individ = [
        row for row in data if row["Категория"] == "Переводы" and re.match(pattern, row["Описание"]) is not None
    ]
    services_logger.info("Данные успешно созданы")
    result = json.dumps(transactions_for_individ, indent=4, ensure_ascii=False)
    return result


if __name__ == "__main__":
    result = search_for_transactions_by_individ()
    print(result)
