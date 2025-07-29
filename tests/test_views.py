from src.views import *

file_path = os.path.dirname(__file__), "../data/operations.csv"


def test_exception_handling_date():
    result = transaction_analysis(date="30-12-2021 19:04:44")
    assert result == "Ошибка: DataFrame constructor not properly called!"


def test_for_returned_data_format():
    result = transaction_analysis(date="30.12.2021 19:04:44")
    assert isinstance(result, str)


def test_input_data_format():
    result = transaction_analysis(date=1)
    assert result == "Ошибка: DataFrame constructor not properly called!"


def test_services():
    data = search_for_transactions_by_individ()
    assert isinstance(data, str)


def test_reports(category, date_string):
    transactions = returns_dataframe_format()
    data = spending_by_category(transactions, category, date_string)
    assert isinstance(data, str)
