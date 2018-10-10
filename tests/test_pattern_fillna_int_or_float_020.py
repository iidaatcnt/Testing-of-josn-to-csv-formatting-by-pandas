"""
pattern_fillna_int_or_float()関数をテスト
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

from functios import pattern_fillna_int_or_float_020


class TestFillnanMst:
    """
    020のpattern_fillna_int_or_float()関数をテストするために共通に必要な値や
    dfを設定しておく
    """

    # 既定値を設定
    AGE_DEFAULT = 99  # int型
    WT_DEFAULT = 99.9  # float型

    # 列名と既定値のペアを辞書型で作成
    default_val_dict = {'age': AGE_DEFAULT, 'wt': WT_DEFAULT}

    def test_pattern_fillna_int_or_float(self):
        """
        最初に与えられた例でpattern_fillna_int_or_float()をテスト
        """
        # 更新tbl
        test_tbl = pd.DataFrame(
            [
                {"hash": 10, "age": 28, "wt": 56.1},
                {"hash": 20, "age": None, "wt": None},
                {"hash": 30, "age": '', "wt": ''},
                {"hash": 40, "name": 33, "wt": 100}
            ], columns=["hash", "age", "wt"]
        )

        # 出力されて欲しいdf
        expected_table = pd.DataFrame(
            [
                {"hash": 10, "age": 28, "wt": 56.1},
                {"hash": 20, "age": 99, "wt": 99.9},
                {"hash": 30, "age": 99, "wt": 99.9},
                {"hash": 40, "age": np.nan, "wt": 100}
            ], columns=["hash", "age", "wt"]
        )

        # expected_tableのデータ型を期待される型に変換
        # データ型が自動で変更されないように、一時的にstr型の行を追加する
        expected_table.loc[len(expected_table)] = ['tmp'] * len(
            expected_table.columns
            )
        # データ型を変換
        expected_table.loc[0, "age"] = int(expected_table.loc[0, "age"])
        expected_table.loc[1, "age"] = int(expected_table.loc[1, "age"])
        expected_table.loc[2, "age"] = int(expected_table.loc[2, "age"])
        expected_table.loc[3, "wt"] = int(expected_table.loc[3, "wt"])
        # データ型が自動で変更されないように追加した行を削除
        expected_table = expected_table.drop(len(expected_table)-1, axis=0)

        # fillnan_mst関数を実行
        result_table = \
            pattern_fillna_int_or_float_020.pattern_fillna_int_or_float(
                test_tbl,
                TestFillnanMst.default_val_dict
                )

        # pandasのdfの比較を行う
        assert_frame_equal(result_table, expected_table)
