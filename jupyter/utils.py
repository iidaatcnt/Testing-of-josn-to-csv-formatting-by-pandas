"""
複数のpyファイルで使用する関数
"""

import pandas as pd


def transform_datetime(dfm, date_columns):
    """
    func
    指定した列をdatetime64型に変換する
    In
    dfm : pd.DataFrame（変換用）
    date_columns : 変換する列のリスト[list]
    Out
    added_dfm : 変換後のpd.DataFrame
    """
    added_dfm = dfm.copy()
    for col in date_columns:
        added_dfm[col] = pd.to_datetime(added_dfm[col])

    return added_dfm


def transform_object(added_dfm, date_columns):
    """
    func
    指定した列をobject型に変換する
    In
    added_dfm : pd.DataFrame（変換用）
    date_columns : 変換する列のリスト[list]
    Out
    added_dfm : 変換後のpd.DataFrame
    """
    str_transform = lambda x: x.strftime("%Y-%m-%d")
    for col in date_columns:
        added_dfm[col] = added_dfm[col].map(str_transform)

    return added_dfm
