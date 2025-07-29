from unittest.mock import patch

from src.utils import *

PATH = os.path.dirname(os.path.abspath(__file__))


def test_read_csv_file():
    read_csv_file(output_file_path=os.path.join(PATH, "..", "data", "test_operations.csv"))
    assert os.path.exists(r"C:\Users\Thunderobot\PycharmProjects\Coursework_1\data\test_operations.csv")
    os.remove(r"C:\Users\Thunderobot\PycharmProjects\Coursework_1\data\test_operations.csv")


def test_for_returned_data_format():
    result = read_csv_file(output_file_path=os.path.join(PATH, "..", "data", "operations.csv"))
    assert isinstance(result, list)


@patch("src.utils.datetime.datetime")
def test_define_time_morning(mock_datetime):
    mock_datetime.now.return_value.hour = 8
    assert define_time() == "Доброе утро!"


@patch("src.utils.datetime.datetime")
def test_define_time_afternoon(mock_datetime):
    mock_datetime.now.return_value.hour = 14
    assert define_time() == "Добрый день!"


@patch("src.utils.datetime.datetime")
def test_define_time_evening(mock_datetime):
    mock_datetime.now.return_value.hour = 20
    assert define_time() == "Добрый вечер!"


def test_input_data_format():
    result = return_abbreviated_list_of_dict(date="31-12-2021")
    assert result == "Ошибка: time data '31-12-2021' does not match format '%d.%m.%Y %H:%M:%S'"


def test_input_data_type():
    result = return_abbreviated_list_of_dict(date=())
    assert result == "Ошибка: strptime() argument 1 must be str, not tuple"


def test_for_returned_data_format_(date_string):
    result = return_abbreviated_list_of_dict(date_string)
    assert isinstance(result, list)


def test_sort_transactions(data_list):
    result = sorts_transactions(data_list)
    assert isinstance(result, tuple)
