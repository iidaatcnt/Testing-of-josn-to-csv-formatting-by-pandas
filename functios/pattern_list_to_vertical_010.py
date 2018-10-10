"""
010
指定した列内のリストを展開し、縦持ちの1行1データのデータフレームに変換
列名を指定して処理
"""

import numpy as np
import pandas as pd


def pattern_list_to_vertical(update_dfm, to_vertical_column):
    """
    func
    指定した列内のリストを展開し、縦持ちの1行1データのデータフレームに変換する
    In
    update_dfm : 横持ちを縦持ちに変換したいpd.DataFrame
    to_vertical_column : 横持ちを縦持ちに変換する列名[str]
    Out
    縦持ちに変換されたpd.DataFrame
    """
    # DataFrameの入れ物（update_dfm_vertical）を作成
    input_columns = update_dfm.columns  # インプットのdfmの列名
    update_dfm_vertical = pd.DataFrame(columns=input_columns)

    # 縦持ち展開したい要素それぞれを抽出
    for i in range(len(update_dfm)):
        # 要素内のリストの各要素を抽出
        for j in range(len(update_dfm.loc[i, to_vertical_column])):
            # リストを1要素に変換した行を作成
            update_dfm_tmp = update_dfm.loc[i].copy()
            update_dfm_tmp[to_vertical_column] = [
                update_dfm_tmp.loc[to_vertical_column][j]
                ]
            # 縦持ち版データフレームに新たに作成した行を追加
            update_dfm_vertical = update_dfm_vertical.append(update_dfm_tmp)
            # indexを振り直す
            update_dfm_vertical = update_dfm_vertical.reset_index(drop=True)

    # 各列のデータ型をインプットdfmに合わせる
    for col in update_dfm.columns:
        col_type = update_dfm[col].dtype
        update_dfm_vertical = update_dfm_vertical.astype({col: col_type})

    return update_dfm_vertical
