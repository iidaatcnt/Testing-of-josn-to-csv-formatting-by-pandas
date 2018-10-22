"""
050_add_to_end
行毎にend列にadd列の日数を加算してend列を更新
"""

import datetime
from functios.utils import transform_datetime, transform_object


def add_to_end(dfm):
    """
    func
    行毎にend列にadd列の日数を加算してend列を更新
    In
    dfm : pd.DataFrame（変換用）
    Out
    added_dfm : end列を更新した後のpd.DataFrame
    """
    # end列をdatetime64型に変換する
    date_columns = ["end"]
    added_dfm = transform_datetime(dfm, date_columns)

    # end列にadd列分の日数を加算してend列を更新する
    added_dfm["end"] = added_dfm["end"] +\
        added_dfm["add"].map(datetime.timedelta)

    # end列を元の文字列型に直す
    added_dfm = transform_object(added_dfm, date_columns)

    return added_dfm
