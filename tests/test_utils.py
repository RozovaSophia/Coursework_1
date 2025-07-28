import datetime
import pytest
from unittest.mock import patch
from src.utils import *

class TestReadCsvFile:

    def test_read_csv_file(self):
        read_csv_file(file_path = r"C:\Users\Thunderobot\Downloads\operations.xlsx - Отчет по операциям.csv",
        output_file_path = "../data/test_operations.csv")
        assert os.path.exists("../data/test_operations.csv")
        os.remove("../data/test_operations.csv")

    def test_for_returned_data_format(self):
        result = read_csv_file(file_path = r"C:\Users\Thunderobot\Downloads\operations.xlsx - Отчет по операциям.csv",
        output_file_path = "../data/operations.csv")
        assert isinstance(result, list)

    def test_input_data_format(self):
        result = read_csv_file(file_path = r"fake_file", output_file_path = "../data/operations.csv")
        assert result == "Ошибка: [Errno 2] No such file or directory: 'fake_file'"

    def test_for_returned_data_invalid_format(self):
        result = read_csv_file(file_path = (), output_file_path = "../data/operations.csv")
        assert result == "Ошибка: expected str, bytes or os.PathLike object, not tuple"

class TestDefineTime:

    @patch('src.utils.datetime.datetime')
    def test_define_time_morning(self, mock_datetime):
        mock_datetime.now.return_value.hour = 8
        assert define_time() == "Доброе утро!"

    @patch('src.utils.datetime.datetime')
    def test_define_time_afternoon(self, mock_datetime):
        mock_datetime.now.return_value.hour = 14
        assert define_time() == "Добрый день!"

    @patch('src.utils.datetime.datetime')
    def test_define_time_evening(self, mock_datetime):
        mock_datetime.now.return_value.hour = 20
        assert define_time() == "Добрый вечер!"

class TestReturnAbbreviatedListOfDict():

    def test_input_data_format(self):
        result = return_abbreviated_list_of_dict(date = "31-12-2021")
        assert result == "Ошибка: time data '31-12-2021' does not match format '%d.%m.%Y %H:%M:%S'"

    def test_input_data_type(self):
        result = return_abbreviated_list_of_dict(date = ())
        assert result == "Ошибка: strptime() argument 1 must be str, not tuple"

    def test_for_returned_data_format(self, date_string):
        result = return_abbreviated_list_of_dict(date_string)
        assert isinstance(result, list)

class TestSortTransactions():

    def test_sort_transactions(self, data_list):
        result = sorts_transactions(data_list)
        assert isinstance(result, tuple)