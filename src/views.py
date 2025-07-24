from src.utils import *


def transaction_analysis(date: str):
    """принимает на вход строку с датой и временем в формате YYYY-MM-DD HH:MM:SS
    и возвращает JSON-ответ """
    greeting = define_time()
    data = return_abbreviated_list_of_dict(date)


if __name__ == '__main__':
    result = transaction_analysis(date='19.11.2018 18:01:42')
    print(result)