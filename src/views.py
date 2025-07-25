from src.utils import *


def transaction_analysis(date: str):
    """принимает на вход строку с датой и временем в формате YYYY-MM-DD HH:MM:SS
    и возвращает JSON-ответ"""
    transactions = return_abbreviated_list_of_dict("30.12.2021 19:04:44")
    df = get_card_number(transactions)
    greeting = define_time()
    result = format_dataframe_to_json(df, greeting)
    return result


if __name__ == "__main__":
    result = transaction_analysis("30.12.2021 19:04:44")
    print(result)
