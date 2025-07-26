import os
import unittest
import pandas as pd
import csv

from src.reports import *

class TestReturnsDataFrameFormat(unittest.TestCase):

    def test_returns_dataframe(self):
        """проверяет, что функция возвращает DataFrame."""
        df = returns_dataframe_format()
        self.assertIsInstance(df, pd.DataFrame)


    def test_data_loaded(self):
        """Проверяет, что DataFrame не пустой."""
        df = returns_dataframe_format()
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

if __name__ == '__main__':
    unittest.main()