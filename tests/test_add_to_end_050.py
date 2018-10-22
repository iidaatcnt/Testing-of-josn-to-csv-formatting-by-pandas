"""
add_to_end()関数をテスト
"""

import sys
import os
import pandas as pd
from pandas.util.testing import assert_frame_equal

# functiosディレクトリのpyファイルをインポートするためにパスを追加
PATH = os.path.dirname(os.path.abspath(__file__)).split("\\")
PATH = "\\".join(PATH[:-1])
sys.path.append(PATH)

from functios import add_to_end_050


class TestAddToEnd:
    """
    050のadd_to_end()関数をテストするために共通に必要な値や
    dfを設定しておく
    """
    def test_add_to_end(self):
        """
        add_to_endをテスト
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
                 "end": "2018-10-09", "add": -1},
                {"id": "a00", "fire": "2018-10-01", "start": "2018-10-01",
                 "end": "2018-10-10", "add": 0},
                {"id": "a01", "fire": "2018-10-05", "start": "2018-10-01",
                 "end": "2018-10-11", "add": 1},
                {"id": "a02", "fire": "2018-10-10", "start": "2018-10-01",
                 "end": "2018-10-15", "add": 5},
                {"id": "a03", "fire": "2018-10-15", "start": "2018-10-01",
                 "end": "2018-10-20", "add": 10},
                {"id": "a04", "fire": "2018-10-20", "start": "2018-10-01",
                 "end": "2018-10-25", "add": 15},
                {"id": "a05", "fire": "2018-11-01", "start": "2018-10-01",
                 "end": "2018-10-30", "add": 20},
                {"id": "a06", "fire": "2018-11-05", "start": "2018-10-01",
                 "end": "2018-11-09", "add": 30},
                {"id": "a07", "fire": "2018-11-10", "start": "2018-10-01",
                 "end": "2018-11-29", "add": 50},
                {"id": "a08", "fire": "2019-10-01", "start": "2018-10-01",
                 "end": "2019-01-18", "add": 100},
                {"id": "a09", "fire": "2019-10-05", "start": "2018-10-01",
                 "end": "2023-07-07", "add": 1000}
            ], columns=["id", "fire", "start", "end", "add"]
        )

        # add_to_end関数を実行
        result_df = add_to_end_050.add_to_end(test_df)

        # pandasのdfの比較を行う
        assert_frame_equal(result_df, expected_df)
