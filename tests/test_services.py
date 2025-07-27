from src.services import search_for_transactions_by_individ

class TestServices():

    def test_for_returned_data_format(self):
        result = search_for_transactions_by_individ()
        assert isinstance(result, str)