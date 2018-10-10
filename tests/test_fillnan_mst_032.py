"""
fillnan_mst()関数をテスト
欠損値処理を行う際、price列はint型であると仮定して最後にint型に変換している
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

from functios import fillnan_mst_032


class TestFillnanMst:
    """
    032のfillnan_mst()関数をテストするために共通に必要な値や
    dfを設定しておく
    """
    # init
    MST_INIT = 99

    # 参照df その１
    EMST = pd.DataFrame(
        [
            {"lcd": "E001", "price": 1},
            {"lcd": "E002", "price": ''}
        ], columns=["lcd", "price"]
    )
    # 参照df その２
    FMST = pd.DataFrame(
        [
            {"lcd": "F001", "price": 2},
            {"lcd": "F002", "price": ''}
        ], columns=["lcd", "price"]
    )

    def test_fillnan_mst_small(self):
        """
        最初に与えられた例でfillnan_mstをテスト
        """
        # 更新tbl
        test_tbl = pd.DataFrame(
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

        # 出力されて欲しいdf
        expected_table = pd.DataFrame(
            [
                {"lcd": "E001", "product": "abc", "price": 100},
                {"lcd": "E001", "product": "abc", "price": 1},
                {"lcd": "E001", "product": "abc", "price": 1},
                {"lcd": "E002", "product": "abc", "price": 99},
                {"lcd": "E002", "product": "abc", "price": 99},
                {"lcd": "E003", "product": "abc", "price": 99},
                {"lcd": "E003", "product": "abc", "price": 99},
                {"lcd": "F001", "product": "abc", "price": 100},
                {"lcd": "F001", "product": "abc", "price": 2},
                {"lcd": "F001", "product": "abc", "price": 2},
                {"lcd": "F002", "product": "abc", "price": 99},
                {"lcd": "F002", "product": "abc", "price": 99},
                {"lcd": "F003", "product": "abc", "price": 99},
                {"lcd": "F003", "product": "abc", "price": 99}
            ], columns=["lcd", "product", "price"]
        )

        # expected_tableのprice列のデータ型をint型に変換
        PRICE_TYPE = int
        expected_table = expected_table.astype({"price": PRICE_TYPE})

        # fillnan_mst関数を実行
        result_table = fillnan_mst_032.fillnan_mst(
            test_tbl,
            TestFillnanMst.EMST,
            TestFillnanMst.FMST,
            TestFillnanMst.MST_INIT)

        # pandasのdfの比較を行う
        assert_frame_equal(result_table, expected_table)

    def test_fillnan_mst_large(self):
        """
        lcdにバリエーションのある例でfillnan_mstをテスト
        """
        # 更新tbl
        test_tbl = pd.DataFrame(
            [
                {"lcd": "F001", "product": "abc", "price": None},
                {"lcd": "E001", "product": "abc", "price": None},
                {"lcd": "X001", "product": "abc", "price": None},
                {"lcd": "F001", "product": "abc", "price": ''},
                {"lcd": "E001", "product": "abc", "price": ''},
                {"lcd": "X001", "product": "abc", "price": ''},
                {"lcd": "F001", "product": "abc", "price": 100},
                {"lcd": "E001", "product": "abc", "price": 200},
                {"lcd": "X001", "product": "abc", "price": 300},
                {"lcd": "F002", "product": "abc", "price": None},
                {"lcd": "E002", "product": "abc", "price": None},
                {"lcd": "X002", "product": "abc", "price": None},
                {"lcd": "F002", "product": "abc", "price": ''},
                {"lcd": "E002", "product": "abc", "price": ''},
                {"lcd": "X002", "product": "abc", "price": ''},
                {"lcd": "F002", "product": "abc", "price": 100},
                {"lcd": "E002", "product": "abc", "price": 200},
                {"lcd": "X002", "product": "abc", "price": 300},
                {"lcd": "F003", "product": "abc", "price": None},
                {"lcd": "E003", "product": "abc", "price": None},
                {"lcd": "X003", "product": "abc", "price": None},
                {"lcd": "F003", "product": "abc", "price": ''},
                {"lcd": "E003", "product": "abc", "price": ''},
                {"lcd": "X003", "product": "abc", "price": ''},
                {"lcd": "F003", "product": "abc", "price": 100},
                {"lcd": "E003", "product": "abc", "price": 200},
                {"lcd": "X003", "product": "abc", "price": 300},
            ], columns=["lcd", "product", "price"]
        )

        # 出力されて欲しいdf
        expected_table = pd.DataFrame(
            [
                {"lcd": "F001", "product": "abc", "price": 2},
                {"lcd": "E001", "product": "abc", "price": 1},
                {"lcd": "X001", "product": "abc", "price": 2},
                {"lcd": "F001", "product": "abc", "price": 2},
                {"lcd": "E001", "product": "abc", "price": 1},
                {"lcd": "X001", "product": "abc", "price": 2},
                {"lcd": "F001", "product": "abc", "price": 100},
                {"lcd": "E001", "product": "abc", "price": 200},
                {"lcd": "X001", "product": "abc", "price": 300},
                {"lcd": "F002", "product": "abc", "price": 99},
                {"lcd": "E002", "product": "abc", "price": 99},
                {"lcd": "X002", "product": "abc", "price": 99},
                {"lcd": "F002", "product": "abc", "price": 99},
                {"lcd": "E002", "product": "abc", "price": 99},
                {"lcd": "X002", "product": "abc", "price": 99},
                {"lcd": "F002", "product": "abc", "price": 100},
                {"lcd": "E002", "product": "abc", "price": 200},
                {"lcd": "X002", "product": "abc", "price": 300},
                {"lcd": "F003", "product": "abc", "price": 99},
                {"lcd": "E003", "product": "abc", "price": 99},
                {"lcd": "X003", "product": "abc", "price": 99},
                {"lcd": "F003", "product": "abc", "price": 99},
                {"lcd": "E003", "product": "abc", "price": 99},
                {"lcd": "X003", "product": "abc", "price": 99},
                {"lcd": "F003", "product": "abc", "price": 100},
                {"lcd": "E003", "product": "abc", "price": 200},
                {"lcd": "X003", "product": "abc", "price": 300},
            ], columns=["lcd", "product", "price"]
        )

        # expected_tableのprice列のデータ型をint型に変換
        PRICE_TYPE = int
        expected_table = expected_table.astype({"price": PRICE_TYPE})

        # fillnan_mst関数を実行
        result_table = fillnan_mst_032.fillnan_mst(
            test_tbl,
            TestFillnanMst.EMST,
            TestFillnanMst.FMST,
            TestFillnanMst.MST_INIT)

        # pandasのdfの比較を行う
        assert_frame_equal(result_table, expected_table)
