from src.services import search_for_transactions_by_individ
from src.utils import *


def transaction_analysis(date: str):
    """принимает на вход строку с датой и временем в формате YYYY-MM-DD HH:MM:SS
    и возвращает JSON-ответ"""
    transactions = return_abbreviated_list_of_dict("30.12.2021 19:04:44")
    card_num_df, top_transactions = sorts_transactions(transactions)
    greeting = define_time()
    currency_rates = converted_currency()
    stock_prices = request_stock_prices()
    result = format_dataframe_to_json(card_num_df, top_transactions, currency_rates, stock_prices, greeting)
    return result


def services():
    while True:
        print("Желаете посмотреть информацию о переводах физическим лицам? Да/Нет")
        user_input = input().lower()
        if user_input == "да":
            data = search_for_transactions_by_individ()
            print(data)
            break
        elif user_input == "нет":
            break
        else:
            print("Повторите попытку.")


if __name__ == "__main__":
    result_1 = transaction_analysis("30.12.2021 19:04:44")
    result_2 = services()
    print(result_1, result_2)
