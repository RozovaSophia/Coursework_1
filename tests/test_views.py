import pytest

from src.views import transaction_analysis

class TestTransactionsAnalysis():

    def test_transaction_analysis(date_string):
        """проверяет, что функция возвращает json (строку)"""
        json_f = transaction_analysis(date_string)
        assert isinstance(json_f, str)