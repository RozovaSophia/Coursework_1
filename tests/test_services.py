from src.services import search_for_transactions_by_individ


def test_for_returned_data_format():
    result = search_for_transactions_by_individ()
    assert isinstance(result, str)
