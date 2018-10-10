"""
fillnan_mst_for()関数をテスト
"""

import sys
import os
from nose.tools import with_setup
import numpy as np
import pandas as pd
from pandas.util.testing import assert_frame_equal

# functiosディレクトリのpyファイルをインポートするためにパスを追加
PATH = os.path.dirname(os.path.abspath(__file__)).split("\\")
PATH = "\\".join(PATH[:-1])
sys.path.append(PATH)

from functios import fillnan_mst_030_1


class TestFillnanMst:
    """
    030_1のfillnan_mst_for()関数をテストするために共通に必要な値や
    dfを設定しておく
    """
    # 参照df その１
    FMST = pd.DataFrame(
        [
            {"cd": "F001", "val": 1},
            {"cd": "F002", "val": 2},
            {"cd": "F003", "val": 3}
            ], columns=["cd", "val"]
    )

    # 参照df その２
    EMST = pd.DataFrame(
        [
            {"cd": "E001", "val": 4},
            {"cd": "E002", "val": 5},
            {"cd": "E003", "val": 6}
        ], columns=["cd", "val"]
    )

    def test_fillnan_mst_for_small(self):
        """
        最初に与えられた例でfillnan_mst_for()をテスト
        """
        # 更新tbl
        test_tbl = pd.DataFrame(
            [
                {"cd": "F001", "val": None},
                {"cd": "E001", "val": None},
                {"cd": "X001", "val": None},
                {"cd": "F001", "val": ''},
                {"cd": "E001", "val": ''},
                {"cd": "X001", "val": ''},
                {"cd": "F001", "val": 100},
                {"cd": "E001", "val": 200},
                {"cd": "X001", "val": 300}
            ], columns=["cd", "val"]
        )

        # 出力されて欲しいdf
        expected_table = pd.DataFrame(
            [
                {"cd": "F001", "val": 1},
                {"cd": "E001", "val": 4},
                {"cd": "X001", "val": np.nan},
                {"cd": "F001", "val": 1},
                {"cd": "E001", "val": 4},
                {"cd": "X001", "val": np.nan},
                {"cd": "F001", "val": 100},
                {"cd": "E001", "val": 200},
                {"cd": "X001", "val": 300}
            ], columns=["cd", "val"]
        )

        # expected_tableのprice列のデータ型をint型に変換
        # PRICE_TYPE = int
        # expected_table = expected_table.astype({"price": PRICE_TYPE})

        # fillnan_mst_for関数を実行
        result_table = fillnan_mst_030_1.fillnan_mst_for(
            test_tbl,
            TestFillnanMst.FMST,
            TestFillnanMst.EMST
            )

        # pandasのdfの比較を行う
        assert_frame_equal(result_table, expected_table)

    def test_fillnan_mst_for_large(self):
        """
        cdにバリエーションのある例でfillnan_mst_for()をテスト
        """
        # 更新tbl
        test_tbl = pd.DataFrame(
            [
                {"cd": "F001", "val": None},
                {"cd": "E001", "val": None},
                {"cd": "X001", "val": None},
                {"cd": "F001", "val": ''},
                {"cd": "E001", "val": ''},
                {"cd": "X001", "val": ''},
                {"cd": "F001", "val": 100},
                {"cd": "E001", "val": 200},
                {"cd": "X001", "val": 300},
                {"cd": "F002", "val": None},
                {"cd": "E002", "val": None},
                {"cd": "X002", "val": None},
                {"cd": "F002", "val": ''},
                {"cd": "E002", "val": ''},
                {"cd": "X002", "val": ''},
                {"cd": "F002", "val": 100},
                {"cd": "E002", "val": 200},
                {"cd": "X002", "val": 300},
                {"cd": "F003", "val": None},
                {"cd": "E003", "val": None},
                {"cd": "X003", "val": None},
                {"cd": "F003", "val": ''},
                {"cd": "E003", "val": ''},
                {"cd": "X003", "val": ''},
                {"cd": "F003", "val": 100},
                {"cd": "E003", "val": 200},
                {"cd": "X003", "val": 300}
                ], columns=["cd", "val"]
        )

        # 出力されて欲しいdf
        expected_table = pd.DataFrame(
            [
                {"cd": "F001", "val": 1},
                {"cd": "E001", "val": 4},
                {"cd": "X001", "val": np.nan},
                {"cd": "F001", "val": 1},
                {"cd": "E001", "val": 4},
                {"cd": "X001", "val": np.nan},
                {"cd": "F001", "val": 100},
                {"cd": "E001", "val": 200},
                {"cd": "X001", "val": 300},
                {"cd": "F002", "val": 2},
                {"cd": "E002", "val": 5},
                {"cd": "X002", "val": np.nan},
                {"cd": "F002", "val": 2},
                {"cd": "E002", "val": 5},
                {"cd": "X002", "val": np.nan},
                {"cd": "F002", "val": 100},
                {"cd": "E002", "val": 200},
                {"cd": "X002", "val": 300},
                {"cd": "F003", "val": 3},
                {"cd": "E003", "val": 6},
                {"cd": "X003", "val": np.nan},
                {"cd": "F003", "val": 3},
                {"cd": "E003", "val": 6},
                {"cd": "X003", "val": np.nan},
                {"cd": "F003", "val": 100},
                {"cd": "E003", "val": 200},
                {"cd": "X003", "val": 300}
                ], columns=["cd", "val"]
        )
        # expected_tableのprice列のデータ型をint型に変換
        # PRICE_TYPE = int
        # expected_table = expected_table.astype({"price": PRICE_TYPE})

        # fillnan_mst_for関数を実行
        result_table = fillnan_mst_030_1.fillnan_mst_for(
            test_tbl,
            TestFillnanMst.FMST,
            TestFillnanMst.EMST
            )

        # pandasのdfの比較を行う
        assert_frame_equal(result_table, expected_table)
