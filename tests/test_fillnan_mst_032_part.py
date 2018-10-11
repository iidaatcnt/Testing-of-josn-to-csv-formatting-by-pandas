"""
fillnan_e_price()関数をテスト
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

from functios import fillnan_mst_032_part


class TestFillnanMst:
    """
    032_partのfillnan_e_price()関数をテストするために共通に必要な値や
    dfを設定しておく
    """

    # 列名を指定
    cols = {"lcd": "lcd_x", "price": "price", "e_price": "e_price"}

    def test_fillnan_e_price_small(self):
        """
        最初に与えられた例でfillnan_e_priceをテスト
        """
        # 更新tbl
        test_tbl = pd.DataFrame(
            [
                {"lcd_x": "E001", "product": "abc", "price": 100, "e_price": 1,
                 "not_E_lcd": "E001", "lcd_y": np.nan, "f_price": np.nan},
                {"lcd_x": "E001", "product": "abc", "price": '', "e_price": 1,
                 "not_E_lcd": "E001", "lcd_y": np.nan, "f_price": np.nan},
                {"lcd_x": "E001", "product": "abc", "price": None,
                 "e_price": 1, "not_E_lcd": "E001", "lcd_y": np.nan,
                 "f_price": np.nan},
                {"lcd_x": "E002", "product": "abc", "price": '', "e_price": "",
                 "not_E_lcd": "E002", "lcd_y": np.nan, "f_price": np.nan},
                {"lcd_x": "E002", "product": "abc", "price": None,
                 "e_price": "", "not_E_lcd": "E002", "lcd_y": np.nan,
                 "f_price": np.nan},
                {"lcd_x": "E003", "product": "abc", "price": '',
                 "e_price": np.nan, "not_E_lcd": "E003", "lcd_y": np.nan,
                 "f_price": np.nan},
                {"lcd_x": "E003", "product": "abc", "price": None,
                 "e_price": np.nan, "not_E_lcd": "E003", "lcd_y": np.nan,
                 "f_price": np.nan},
                {"lcd_x": "F001", "product": "abc", "price": 100,
                 "e_price": np.nan, "not_E_lcd": "001", "lcd_y": "F001",
                 "f_price": 2},
                {"lcd_x": "F001", "product": "abc", "price": '',
                 "e_price": np.nan, "not_E_lcd": "001", "lcd_y": "F001",
                 "f_price": 2},
                {"lcd_x": "F001", "product": "abc", "price": None,
                 "e_price": np.nan, "not_E_lcd": "001", "lcd_y": "F001",
                 "f_price": 2},
                {"lcd_x": "F002", "product": "abc", "price": '',
                 "e_price": np.nan, "not_E_lcd": "002", "lcd_y": "F002",
                 "f_price": ""},
                {"lcd_x": "F002", "product": "abc", "price": None,
                 "e_price": np.nan, "not_E_lcd": "002", "lcd_y": "F002",
                 "f_price": ""},
                {"lcd_x": "F003", "product": "abc", "price": '',
                 "e_price": np.nan, "not_E_lcd": "003", "lcd_y": np.nan,
                 "f_price": np.nan},
                {"lcd_x": "F003", "product": "abc", "price": None,
                 "e_price": np.nan, "not_E_lcd": "003", "lcd_y": np.nan,
                 "f_price": np.nan}
            ], columns=["lcd_x", "product", "price", "e_price", "not_E_lcd",
                        "lcd_y", "f_price"]
        )

        # 出力されて欲しいdf
        expected_table = pd.DataFrame(
            [
                {"lcd": "E001", "product": "abc", "price": 100},
                {"lcd": "E001", "product": "abc", "price": 1},
                {"lcd": "E001", "product": "abc", "price": 1},
                {"lcd": "E002", "product": "abc", "price": np.nan},
                {"lcd": "E002", "product": "abc", "price": np.nan},
                {"lcd": "E003", "product": "abc", "price": np.nan},
                {"lcd": "E003", "product": "abc", "price": np.nan},
                {"lcd": "F001", "product": "abc", "price": 100},
                {"lcd": "F001", "product": "abc", "price": np.nan},
                {"lcd": "F001", "product": "abc", "price": np.nan},
                {"lcd": "F002", "product": "abc", "price": np.nan},
                {"lcd": "F002", "product": "abc", "price": np.nan},
                {"lcd": "F003", "product": "abc", "price": np.nan},
                {"lcd": "F003", "product": "abc", "price": np.nan}
            ], columns=["lcd", "product", "price"]
        )

        # fillnan_e_price関数を実行
        result_table = fillnan_mst_032_part.fillnan_e_price(
            test_tbl,
            TestFillnanMst.cols)

        # pandasのdfの比較を行う
        assert_frame_equal(result_table, expected_table)
