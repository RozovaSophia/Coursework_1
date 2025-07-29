import os

import pandas as pd

from src.reports import returns_dataframe_format

PATH = os.path.dirname(os.path.abspath(__file__))


def test_format_verification():
    result = returns_dataframe_format()
    assert isinstance(result, pd.DataFrame)


def test_exception_handling_transactions(category, date_string):
    from src.reports import spending_by_category

    result = spending_by_category("transactions", category, date_string)
    assert result == "Oшибка: string indices must be integers, not 'str'"


def test_exception_hangling_category(date_string):
    from src.reports import spending_by_category

    transactions = returns_dataframe_format()
    result = spending_by_category(transactions, "hanging_category", date_string)
    assert result == "Ошибка: 'Категория'"


def test_exception_hangling_date(category):
    from src.reports import spending_by_category

    transactions = returns_dataframe_format()
    result = spending_by_category(transactions, category, "hanging_date")
    assert result == "Ошибка: time data 'hanging_date' does not match format '%d.%m.%Y %H:%M:%S'"
