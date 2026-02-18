from src.reports import *
from src.services import search_for_transactions_by_individ
from src.utils import *


def transaction_analysis(date: str):
    """принимает на вход строку с датой и временем в формате YYYY-MM-DD HH:MM:SS
    и возвращает JSON-ответ"""
    try:
        transactions = return_abbreviated_list_of_dict(date)
        card_num_df, top_transactions = sorts_transactions(transactions)
        greeting = define_time()
        currency_rates = converted_currency()
        stock_prices = request_stock_prices()
        result = format_dataframe_to_json(card_num_df, top_transactions, currency_rates, stock_prices, greeting)
        return result
    except ValueError as e:
        return f"Ошибка: {e}"
    except TypeError as e:
        return f"Ошибка: {e}"


if __name__ == "__main__":
    result_1 = transaction_analysis("31.12.2021 16:44:00")
    print(result_1)


def services():
    """реализует функционал, который выводит информацию переводов физ.лицам"""
    while True:
        print("Желаете посмотреть информацию о переводах физическим лицам? Да/Нет")
        user_input = input().lower()
        if user_input == "да":
            data = search_for_transactions_by_individ()
            return data
        elif user_input == "нет":
            break
        else:
            print("Повторите попытку.")


def reports():
    """реализует функционал, который выводит информацию трат по определенной категории за определенное время"""

    transactions = returns_dataframe_format()

    while True:
        print("Желаете посмотреть информацию о тратах по категориям? Да/Нет")
        user_input = input().lower()
        if user_input == "да":
            print("Введите категорию: ")
            user_input_category = input().capitalize()
            print("Чтобы получить данные за последние три месяца, введите дату: ")
            user_input_date = input().lower()
            data = spending_by_category_decorated(transactions, user_input_category, user_input_date)
            return data
        elif user_input == "нет":
            break
        else:
            print("Повторите попытку.")


if __name__ == "__main__":
    result_2 = services()
    result_3 = reports()
    print(result_2, result_3)
