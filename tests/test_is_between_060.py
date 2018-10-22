"""
is_between()関数をテスト
"""

import sys
import os
import pandas as pd
from pandas.util.testing import assert_frame_equal

# functiosディレクトリのpyファイルをインポートするためにパスを追加
PATH = os.path.dirname(os.path.abspath(__file__)).split("\\")
PATH = "\\".join(PATH[:-1])
sys.path.append(PATH)

from functios import is_between_060


class TestIsBetween:
    """
    060のis_between()関数をテストするために共通に必要な値や
    dfを設定しておく
    """
    def test_is_between(self):
        """
        is_betweenをテスト
        """
        # 入力用df
        test_df = pd.DataFrame(
            [
                {"id": "a00", "fire": "2018-09-30", "start": "2018-10-01",
                 "end": "2018-10-10", "add": -1},
                {"id": "a00", "fire": "2018-10-01", "start": "2018-10-01",
                 "end": "2018-10-10", "add": 0},
                {"id": "a01", "fire": "2018-10-05", "start": "2018-10-01",
                 "end": "2018-10-10", "add": 1},
                {"id": "a02", "fire": "2018-10-10", "start": "2018-10-01",
                 "end": "2018-10-10", "add": 5},
                {"id": "a03", "fire": "2018-10-15", "start": "2018-10-01",
                 "end": "2018-10-10", "add": 10},
                {"id": "a04", "fire": "2018-10-20", "start": "2018-10-01",
                 "end": "2018-10-10", "add": 15},
                {"id": "a05", "fire": "2018-11-01", "start": "2018-10-01",
                 "end": "2018-10-10", "add": 20},
                {"id": "a06", "fire": "2018-11-05", "start": "2018-10-01",
                 "end": "2018-10-10", "add": 30},
                {"id": "a07", "fire": "2018-11-10", "start": "2018-10-01",
                 "end": "2018-10-10", "add": 50},
                {"id": "a08", "fire": "2019-10-01", "start": "2018-10-01",
                 "end": "2018-10-10", "add": 100},
                {"id": "a09", "fire": "2019-10-05", "start": "2018-10-01",
                 "end": "2020-10-10", "add": 1000}
            ], columns=["id", "fire", "start", "end", "add"]
        )

        # 出力されて欲しいdf
        expected_df = pd.DataFrame(
            [
                {"id": "a00", "fire": "2018-09-30", "start": "2018-10-01",
                 "end": "2018-10-10", "add": -1, "chk": False},
                {"id": "a00", "fire": "2018-10-01", "start": "2018-10-01",
                 "end": "2018-10-10", "add": 0, "chk": True},
                {"id": "a01", "fire": "2018-10-05", "start": "2018-10-01",
                 "end": "2018-10-10", "add": 1, "chk": True},
                {"id": "a02", "fire": "2018-10-10", "start": "2018-10-01",
                 "end": "2018-10-10", "add": 5, "chk": True},
                {"id": "a03", "fire": "2018-10-15", "start": "2018-10-01",
                 "end": "2018-10-10", "add": 10, "chk": False},
                {"id": "a04", "fire": "2018-10-20", "start": "2018-10-01",
                 "end": "2018-10-10", "add": 15, "chk": False},
                {"id": "a05", "fire": "2018-11-01", "start": "2018-10-01",
                 "end": "2018-10-10", "add": 20, "chk": False},
                {"id": "a06", "fire": "2018-11-05", "start": "2018-10-01",
                 "end": "2018-10-10", "add": 30, "chk": False},
                {"id": "a07", "fire": "2018-11-10", "start": "2018-10-01",
                 "end": "2018-10-10", "add": 50, "chk": False},
                {"id": "a08", "fire": "2019-10-01", "start": "2018-10-01",
                 "end": "2018-10-10", "add": 100, "chk": False},
                {"id": "a09", "fire": "2019-10-05", "start": "2018-10-01",
                 "end": "2020-10-10", "add": 1000, "chk": True}
            ], columns=["id", "fire", "start", "end", "add", "chk"]
        )

        # is_between関数を実行
        result_df = is_between_060.is_between(test_df)

        # pandasのdfの比較を行う
        assert_frame_equal(result_df, expected_df)
