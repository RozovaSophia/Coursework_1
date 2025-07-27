import os
import pytest
import tempfile
import pandas as pd

from src.reports import returns_dataframe_format

print(f"__file__ is: {__file__}")  # Добавьте эту строку!

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/operations.csv'))
print(f"file_path is: {file_path}")
class TestReturnsDataframeFormat():

    def test_exception_handling(self):
        result = returns_dataframe_format(file_path="non_exist.csv")
        assert result == "Ошибка: [Errno 2] No such file or directory: 'non_exist.csv'"

    def test_to_check_processing_of_empty_file(self, tmp_path):
        temp_file_path = tmp_path / "test_file.csv"  # Используем csv для совместимости
        temp_file_path.touch()
        result = returns_dataframe_format(file_path=str(temp_file_path))
        assert isinstance(result, pd.DataFrame)
        assert result.empty

    def test_format_verification(self):
        result = returns_dataframe_format(file_path)
        assert isinstance(result, pd.DataFrame)


class TestSpendingByCategory():

    def test_exception_handling_transactions(self, category, date_string):
        from src.reports import spending_by_category
        result = spending_by_category('transactions', category, date_string)
        assert result == "Oшибка: string indices must be integers, not 'str'"

    def test_exception_hangling_category(self, date_string):
        from src.reports import spending_by_category
        transactions = returns_dataframe_format()
        result = spending_by_category(transactions, 'hanging_category', date_string)
        assert result == "Oшибка: string indices must be integers, not 'str'"

    def test_exception_hangling_date(self, category):
        from src.reports import spending_by_category
        transactions = returns_dataframe_format()
        result = spending_by_category(transactions, category, 'hanging_date')
        assert result == "Ошибка: time data 'hanging_date' does not match format '%d.%m.%Y %H:%M:%S'"


class TestDecorator():
    pass



