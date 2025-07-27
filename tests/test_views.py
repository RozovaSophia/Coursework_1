from src.reports import *
from src.services import search_for_transactions_by_individ
from src.utils import *
from src.views import *
import pytest

file_path = os.path.dirname(__file__), '../data/operations.csv'

class TestTransactionAnalysis():

    def test_exception_handling_date(self):
        result = transaction_analysis(date='30-12-2021 19:04:44')
        assert result == "Ошибка: time data '30-12-2021 19:04:44' does not match format '%d.%m.%Y %H:%M:%S'"

    def test_for_returned_data_format(self):
        result = transaction_analysis(date='30.12.2021 19:04:44')
        assert isinstance(result, str)

    def test_input_data_format(self):
        result = transaction_analysis(date=1)
        assert result == "Ошибка: strptime() argument 1 must be str, not int"

class TestServices():

    def test_services(self):
        data = search_for_transactions_by_individ()
        assert isinstance(data, str)

class TestReports():

    def test_reports(self, category, date_string):
        transactions = returns_dataframe_format()
        data = spending_by_category(transactions, category, date_string)
        assert isinstance(data, str)
