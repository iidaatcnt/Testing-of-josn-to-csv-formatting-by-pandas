"""
020
以下の条件に沿って、欠損値を穴埋め
- 既定値の値もデータ型もそのまま変えずに穴埋め
- 欠損箇所を埋める既定値は列ごとにある
- データはintとflortの場合がある
- 列内のNoneのところだけに穴埋め処理し、他は影響なし
- 空文字はNone扱い
- 列名ミスなどでNaNとなっている部分は放置
- 穴埋めの既定値は基本的にint型。
- float型で穴埋めしたい列名を引数でリスト形式で指定
    - 未対応
    - （既定値を99.0のようにfloatにすればfloat型で埋まるが、それでは不足か）
"""


def fill_none(dfm, col_name, default_val):
    """
    func
    データ型を確認し、'NoneType'の場合のみ代入する関数
    In
    dfm : 更新対象のpd.DataFrame
    col_name : 処理を行う列名[str]
    default_val : 既定値[int or float]
    Out
    代入が完了したpd.DataFrame
    """
    default_value = default_val

    def set_default(val):
        """
        func
        値のデータ型を確認し、'NoneType'の場合は既定値を返す
        それ以外は値自身を返す関数
        In
        val : データ型を確認する値[データ型不問]
        Out
        既定値または値自身
        """
        if isinstance(val, type(None)):
            return default_value
        else:
            return val

    # 欠損値（None）を穴埋め
    dfm[col_name] = dfm[col_name].map(set_default)

    return dfm


def set_type(dfm, dfm_type, col_name, default_val):
    """
    func
    保持しておいたデータ型をdfmに適用する関数
    In
    dfm : 更新対象のpd.DataFrame
    dfm_type : 元のdfmのそれぞれの要素のデータ型を保持したpd.DataFrame
    col_name : 処理対象の列名[str]
    default_val : 既定値[int or float]
    Out
    データ型を保持しておいたものに復元したpd.DataFrame
    """
    for i in range(len(dfm_type)):
        pre_type = dfm_type.loc[i, col_name]  # dfmの各要素のデータ型を取得
        # 代入する値のデータ型を復元
        # 元のデータ型がNoneで代入したときは少し面倒
        if isinstance(pre_type, type(None)):
            if isinstance(default_val, int):
                dfm.loc[i, col_name] = int(dfm.loc[i, col_name])
            elif isinstance(default_val, float):
                dfm.loc[i, col_name] = float(dfm.loc[i, col_name])
        # 代入していなくてもデータ型が変化していることがあるため、元のデータ型を復元
        elif isinstance(pre_type, int):
            dfm.loc[i, col_name] = int(dfm.loc[i, col_name])
        # 代入していなくてもデータ型が変化していることがあるため、元のデータ型を復元
        elif isinstance(pre_type, float):
            dfm.loc[i, col_name] = float(dfm.loc[i, col_name])

    return dfm


def pattern_fillna_int_or_float(update_dfm, default_val_dict):
    """
    func
    他の要素に影響を与えることなくNoneを列ごとの既定値で埋める
    データ型も元の値や既定値から変化させない
    In
    update_dfm : 更新対象のpd.DataFrame
    default_val_dict : 列名と既定値のセット[dict]{列名: 既定値}
    Out
    列ごとの既定値でNoneを埋めたpd.DataFrame
    """
    # データ型を保持しておくデータフレームを作成
    update_dfm_type = update_dfm.copy()
    update_dfm_type = update_dfm_type.applymap(type)

    # 空文字をNoneに置換
    update_dfm = update_dfm.replace('', None)

    # データ型が自動で変更されないように、一時的にstr型の行を追加する
    update_dfm.loc[len(update_dfm)] = ['tmp'] * len(update_dfm.columns)

    # データ型に影響を与えずに欠損値の穴埋めを行う
    for col_name, default_val in default_val_dict.items():
        update_dfm = fill_none(update_dfm, col_name, default_val)
        set_type(update_dfm, update_dfm_type, col_name, default_val)

    # データ型が自動で変更されないように追加した行を削除
    update_dfm = update_dfm.drop(len(update_dfm)-1, axis=0)

    return update_dfm
