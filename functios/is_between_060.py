"""
060_is_between
日付fireがstartとendの範囲内にあるか無いか真偽値を末尾にchkという列に追加
- fireがstart, endの境界上にある場合、「ある」と判定
"""

from functios.utils import transform_datetime, transform_object


def is_between(dfm):
    """
    func
    日付fireがstartとendの範囲内にあるか無いか真偽値を末尾にchkという列に追加
    - fireがstart, endの境界上にある場合、「ある」と判定
    In
    dfm : pd.DataFrame（変換用）
    Out
    added_dfm : chk列を追加した後のpd.DataFrame
    """
    # fire, start, end列をdatetime64型に変換する
    date_columns = ["fire", "start", "end"]
    added_dfm = transform_datetime(dfm, date_columns)

    # 日付fireがstartとendの範囲内にあるか無いか真偽値を末尾にchkという列に追加
    added_dfm["chk"] = (
        added_dfm["start"] <= added_dfm["fire"]
        ) & (added_dfm["fire"] <= added_dfm["end"])

    # fire, start, end列を元の文字列型に直す
    added_dfm = transform_object(added_dfm, date_columns)

    return added_dfm
