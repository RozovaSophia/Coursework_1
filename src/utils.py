import csv
import json
import datetime
from collections import Counter
import pandas as pd

pd.set_option('display.max_columns', None)


def read_csv_file(file_path=r"C:\Users\Thunderobot\Downloads\operations.xlsx - Отчет по операциям.csv", output_file_path="../data/operations.csv"):
    """считывает файл csv, выводит в виде списка словарей, записывает в новый файл"""
    with open(file_path, "r", encoding="UTF-8") as infile:  # Открываем для чтения
        reader = csv.DictReader(infile, delimiter=",")
        data = list(reader)
        with open(output_file_path, "w", encoding="UTF-8", newline="") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=data[0].keys(), delimiter=",")
            writer.writeheader()
            writer.writerows(data)
        return data


def define_time():
    """определяет настоящее время и возвращает приветствие, которое ему соответствует"""
    current_date_time = datetime.datetime.now()
    if current_date_time.hour >= 12:
        return "Добрый день!"
    elif current_date_time.hour >= 18:
        return "Добрый вечер!"
    else:
        return "Доброе утро!"


def return_abbreviated_list_of_dict(date):
    """пользователь вводит дату и функция возвращает данные до этой даты, отсчитывая от начала указанного месяца"""
    data = read_csv_file()
    date_obj = datetime.datetime.strptime(date, "%d.%m.%Y %H:%M:%S")
    filtered_transactions = []
    for transaction in data:
        date_obj_csv = datetime.datetime.strptime(transaction['Дата операции'], "%d.%m.%Y %H:%M:%S")
        if date_obj_csv < date_obj and date_obj_csv.month == date_obj.month:
            filtered_transactions.append(transaction)
    return filtered_transactions


def get_card_number(transactions):
    """группирует данные по номеру карты, высчитывает сумму всех операций и кэшбэка за указанный период.
    Сортирует транзакции по категориям"""

    df = pd.DataFrame(transactions)
    df["Сумма операции"] = df["Сумма операции"].str.replace(",", ".").str.strip().astype(float)

    df["Кэшбэк"] = pd.to_numeric(df["Кэшбэк"], errors='coerce')
    df["Кэшбэк"] = df["Кэшбэк"].fillna(0)
    df = df[df["Номер карты"] != '']
    card_num_df = df.groupby("Номер карты")[["Сумма операции", "Кэшбэк"]].sum()

    df = df[df['Категория'] != '']
    category_counts = df['Категория'].value_counts()
    top_5_categories = category_counts.head(5)
    top_transactions = []
    for category, count in top_5_categories.items():
        example_transaction = df[df['Категория'] == category].iloc[0]

        top_transactions.append({
            "date": example_transaction['Дата операции'],  # или другой столбец с датой
            "amount": example_transaction['Сумма операции'],
            "category": category,
            "description": example_transaction['Описание']  # или другой столбец с описанием
        })

    return card_num_df, top_transactions


def format_dataframe_to_json(card_num_df, top_transactions, greeting):
    cards_data = []
    for card_number, row in card_num_df.iterrows():
        last_digits = str(card_number)[-4:] if len(str(card_number)) >= 4 else str(card_number)
        card_info = {
            "last_digits": last_digits,
            "total_spent": round(row["Сумма операции"], 2),
            "cashback": round(row["Кэшбэк"], 2)
        }
        cards_data.append(card_info)
    json_data = {
        "greeting": greeting,
        "cards": cards_data,
        "top_transactions": top_transactions
    }

    json_string = json.dumps(json_data, ensure_ascii=False, indent=2)
    return json_string


if __name__ == '__main__':
    transactions = return_abbreviated_list_of_dict('30.12.2021 19:04:44')
    card_num_df, top_transactions = get_card_number(transactions)
    greeting = define_time()
    result = format_dataframe_to_json(card_num_df, top_transactions, greeting)
    print(result)
