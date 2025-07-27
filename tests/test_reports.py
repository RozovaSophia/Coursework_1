import pytest
import tempfile
import pandas as pd

from src.reports import returns_dataframe_format


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
        result = returns_dataframe_format(file_path="../data/operations.csv")
        assert isinstance(result, pd.DataFrame)


class TestSpendingByCategory():

    def test_exception_handling_transactions(self, category, date_string):
        from src.reports import spending_by_category
        result = spending_by_category('transactions', category, date_string)
        assert result == "Oшибка: string indices must be integers, not 'str'"


