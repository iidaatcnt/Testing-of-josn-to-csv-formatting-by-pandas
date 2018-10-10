"""
pattern_list_to_vertical()関数をテスト
"""

import sys
import os
from nose.tools import with_setup
import pandas as pd
from pandas.util.testing import assert_frame_equal

# functiosディレクトリのpyファイルをインポートするためにパスを追加
PATH = os.path.dirname(os.path.abspath(__file__)).split("\\")
PATH = "\\".join(PATH[:-1])
sys.path.append(PATH)

from functios import pattern_list_to_vertical_010


class TestFillnanMst:
    """
    pattern_list_to_vertical()関数をテストするために共通に必要な値や
    dfを設定しておく
    """

    # 横持ちから縦持ちに変換する列名を指定
    to_vertical_column = "Reserve"

    def test_pattern_list_to_vertical(self):
        """
        最初に与えられた例でpattern_list_to_vertical()をテスト
        """
        # 更新tbl
        test_tbl = pd.DataFrame(
            [
                {"Pos": "QB", "regular": 12, "Reserve": [9, 8]},
                {"Pos": "CB", "regular": 28, "Reserve": [37, 23, 38, 20]},
                {"Pos": "WR", "regular": 19, "Reserve": [83, 82, 81, 17, 18]},
                {"Pos": "T", "regular": 69, "Reserve": [75, 78]},
                {"Pos": "S", "regular": 36, "Reserve": [35, 21, 29, 27]},
                {"Pos": "RB", "regular": 22, "Reserve": [33, 88, 30]}
            ], columns=["Pos", "regular", "Reserve"]
        )

        # 出力されて欲しいdf
        expected_table = pd.DataFrame(
            [
                {"Pos": "QB", "regular": 12, "Reserve": [9]},
                {"Pos": "QB", "regular": 12, "Reserve": [8]},
                {"Pos": "CB", "regular": 28, "Reserve": [37]},
                {"Pos": "CB", "regular": 28, "Reserve": [23]},
                {"Pos": "CB", "regular": 28, "Reserve": [38]},
                {"Pos": "CB", "regular": 28, "Reserve": [20]},
                {"Pos": "WR", "regular": 19, "Reserve": [83]},
                {"Pos": "WR", "regular": 19, "Reserve": [82]},
                {"Pos": "WR", "regular": 19, "Reserve": [81]},
                {"Pos": "WR", "regular": 19, "Reserve": [17]},
                {"Pos": "WR", "regular": 19, "Reserve": [18]},
                {"Pos": "T", "regular": 69, "Reserve": [75]},
                {"Pos": "T", "regular": 69, "Reserve": [78]},
                {"Pos": "S", "regular": 36, "Reserve": [35]},
                {"Pos": "S", "regular": 36, "Reserve": [21]},
                {"Pos": "S", "regular": 36, "Reserve": [29]},
                {"Pos": "S", "regular": 36, "Reserve": [27]},
                {"Pos": "RB", "regular": 22, "Reserve": [33]},
                {"Pos": "RB", "regular": 22, "Reserve": [88]},
                {"Pos": "RB", "regular": 22, "Reserve": [30]}
            ], columns=["Pos", "regular", "Reserve"]
        )

        # fillnan_mst関数を実行
        result_table = pattern_list_to_vertical_010.pattern_list_to_vertical(
            test_tbl,
            TestFillnanMst.to_vertical_column
            )

        # pandasのdfの比較を行う
        assert_frame_equal(result_table, expected_table)
