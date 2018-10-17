"""
dfm_to_records()関数をテスト
"""

import sys
import os
from nose.tools import eq_
import pandas as pd

# functiosディレクトリのpyファイルをインポートするためにパスを追加
PATH = os.path.dirname(os.path.abspath(__file__)).split("\\")
PATH = "\\".join(PATH[:-1])
sys.path.append(PATH)

from functios import dfm_to_records_040


class TestDfmToRecords:
    """
    040のdfm_to_records()関数をテストするために共通に必要な値や
    dfmを設定しておく
    """
    def test_dfm_to_records(self):
        """
        dfm_to_recordsをテスト
        """
        # 入力用dfm
        dfm = pd.DataFrame(
            [
                {"lcd": "E001", "product": "abc", "price": 100},
                {"lcd": "E001", "product": "abc", "price": ''},
                {"lcd": "E001", "product": "abc", "price": None},
                {"lcd": "E002", "product": "abc", "price": ''},
                {"lcd": "E002", "product": "abc", "price": None},
                {"lcd": "E003", "product": "abc", "price": ''},
                {"lcd": "E003", "product": "abc", "price": None},
                {"lcd": "F001", "product": "abc", "price": 100},
                {"lcd": "F001", "product": "abc", "price": ''},
                {"lcd": "F001", "product": "abc", "price": None},
                {"lcd": "F002", "product": "abc", "price": ''},
                {"lcd": "F002", "product": "abc", "price": None},
                {"lcd": "F003", "product": "abc", "price": ''},
                {"lcd": "F003", "product": "abc", "price": None}
            ], columns=["lcd", "product", "price"]
        )

        # 出力されて欲しいrecords
        expected_records = [
            {"lcd": "E001", "product": "abc", "price": 100},
            {"lcd": "E001", "product": "abc", "price": ''},
            {"lcd": "E001", "product": "abc", "price": None},
            {"lcd": "E002", "product": "abc", "price": ''},
            {"lcd": "E002", "product": "abc", "price": None},
            {"lcd": "E003", "product": "abc", "price": ''},
            {"lcd": "E003", "product": "abc", "price": None},
            {"lcd": "F001", "product": "abc", "price": 100},
            {"lcd": "F001", "product": "abc", "price": ''},
            {"lcd": "F001", "product": "abc", "price": None},
            {"lcd": "F002", "product": "abc", "price": ''},
            {"lcd": "F002", "product": "abc", "price": None},
            {"lcd": "F003", "product": "abc", "price": ''},
            {"lcd": "F003", "product": "abc", "price": None}
        ]

        # 出力されて欲しいcolumns
        expected_columns = ["lcd", "product", "price"]

        # dfm_to_records関数を実行
        result_records, result_columns = dfm_to_records_040.dfm_to_records(
            dfm)

        # 比較を行う
        eq_(result_records, expected_records)
        eq_(result_columns, expected_columns)
