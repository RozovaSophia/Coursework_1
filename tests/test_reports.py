import os
import unittest
import tempfile
import pytest
import pandas as pd
import csv

from src.reports import *

class TestReturnsDataFrameFormat(unittest.TestCase):

    def test_returns_dataframe(self):
        """проверяет, что функция возвращает DataFrame."""
        df = returns_dataframe_format(file_path="../data/operations.csv")
        self.assertIsInstance(df, pd.DataFrame)


    def test_data_loaded(self):
        """Проверяет, что DataFrame не пустой."""
        df = returns_dataframe_format(file_path="../data/operations.csv")
        self.assertFalse(df.empty)


    def test_file_not_found(self):
        """Проверяет, что функция корректно обрабатывает отсутствие файла."""
        with self.assertRaises(FileNotFoundError):
            returns_dataframe_format(file_path="nonexistent_file.csv")

    def test_empty_file(self):
        """Проверяет, что функция возвращает пустой DataFrame при пустом файле."""
        with open("empty_file.csv", "w", newline="") as f:
            pass
        df = returns_dataframe_format(file_path="empty_file.csv")
        self.assertTrue(df.empty)
        os.remove("empty_file.csv")


class TestSpendingByCategory(unittest.TestCase):

    def test_spending_by_category(self):
        """проверяет, что функция возвращает json (строку)"""
        transactions = returns_dataframe_format()
        category = "Супермаркеты"
        date = "31.12.2021 16:44:00"
        json_f = spending_by_category(transactions, category, date)
        self.assertIsInstance(json_f, str)

    def test_invalid_date_format(self):
        transactions = returns_dataframe_format()
        category = 'Еда'
        date = '26-10-2021 16:00:00'

        with self.assertRaises(ValueError):
            spending_by_category(transactions, category, date)

    def test_invalid_amount_format_in_dataframe(self):
        data = {'Дата операции': ['20.10.2024 10:00:00'],
                'Категория': ['Еда'],
                'Сумма операции': ['abc']}
        transactions = pd.DataFrame(data)
        category = 'Еда'
        date = '26.10.2021 16:00:00'

        with self.assertRaises(ValueError):
            spending_by_category(transactions, category, date)

class TestDecoratorForWritingToFile(unittest.TestCase):

    def setUp(self):
        """настройка перед тестом"""
        self.temp_dir = tempfile.TemporaryDirectory()
        self.data_dir = os.path.join(self.temp_dir.name, "data")
        os.makedirs(self.data_dir, exist_ok=True)

    def tearDown(self):
        """удаление после каждого теста"""
        self.temp_dir.cleanup()


    def test_decorator_with_filename(self):
        """тестирование с указанным именем файла"""
        test_filename = os.path.join(self.temp_dir.name, "test_file.json")

        @decorator_for_writing_to_file(filename=test_filename)
        def test_function():
            return '{"key": "value"}'

        result = test_function()

        self.assertEqual(result, '{"key": "value"}') # Проверяем что функция возвращает правильный результат

        with open(test_filename, "r", encoding="utf-8") as f:
            file_content = json.load(f)

        self.assertEqual(file_content, {"key": "value"}) # Проверяем что в файл записан правильный json


if __name__ == '__main__':
    unittest.main()