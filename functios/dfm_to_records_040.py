"""
040_dfm_to_records
df = pd.daraframe(recrds)したdfを再びrecordsに戻す。
"""

import json


def dfm_to_records(dfm):
    """
    func
    df = pd.daraframe(recrds)したdfを再びrecordsに戻す
    In
    dfm : pd.DataFrame（recordsへの変換用）
    Out
    records : [{キー:値, ...},{キー:値, ...},{キー:値, ...},...]に変換されたリスト
    columns_list : 元のdfmの列名のリスト
    """
    # dfmをjson形式（recordsの形）に変換
    records = dfm.to_json(orient="records")
    # 得られたjson文字列をリストに修正
    records = json.loads(records)

    # dfmの列名を取得
    columns = list(dfm.columns)

    return records, columns
