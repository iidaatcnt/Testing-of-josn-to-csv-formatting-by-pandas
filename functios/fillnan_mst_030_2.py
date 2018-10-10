"""
030-2
以下の条件に沿って、参照dfmを元に欠損値を埋める
- tblのvalの欠損値の時に穴埋め処理をする。
  具体的なルールは以下の３つ（ルール２からルール４）。
- tblのcdの値がFで始まる文字列の場合（例：F001）の場合は、
  fmstのval値で（例：F001なので1）欠損値の穴埋めをする
- tblのcdの値がEで始まる文字列の場合（例：E001）の場合は、
  emstのval値で（例：E001なので4）欠損値の穴埋めをする
- tblのcdの値の始まりがFでもEでもない場合（例：X001）は欠損値のままにしておく。
"""

import math
import pandas as pd


def is_not_nan(val):
    """
    func
    mapメソッドのために「NaNでなければTrueを返す」関数
    In
    val ; NaNでないことを判定したい値
    Out
    bool値
    """
    return not math.isnan(val)


def set_new_val(tbl_merged, x_val):
    """
    func
    マージ後のdfにおいて、val列がNaNかつfmstまたはemstの値があるとき、
    dfのnew_val列にfmstまたはemstの値を代入する
    In
    tbl_merged : fmst, emstをマージしたtbl
    x_val : "f_val"または"e_val"を指定
    Out
    なし（tbl_mergedが直接修正される）
    """
    tbl_merged.loc[
        tbl_merged["val"].map(math.isnan) & tbl_merged[x_val].map(
            is_not_nan
            ), "new_val"] = tbl_merged.loc[
                tbl_merged["val"].map(math.isnan) & tbl_merged[x_val].map(
                    is_not_nan), x_val]


def fillnan_mst(tbl, fmst, emst):
    """
    func
    tblのvalがNanのとき、
    cdが'F'で始まる時は、fmstのvalで補完埋め
    cdが'E'で始まる時は、emstのvalで補完埋め
    それ以外のときはNanのまま
    In
    tbl : columns=["cd","val"]のpd.DataFrame（穴埋め更新対象）
    fmst : columns=["cd","val"]のpd.DataFrame（参照用）
    emst : columns=["cd","val"]のpd.DataFrame（参照用）
    Out
    fmst, emstを参照してNanを補完埋めしたpd.DataFrame
    """
    # ''をNoneに置き換え
    tbl = tbl.replace({'': None})

    # tblのval列と区別するためにfmst, emstのval列の列名を変更
    fmst_fval = fmst.rename(columns={'val': 'f_val'})
    emst_eval = emst.rename(columns={'val': 'e_val'})

    # tblにfmst, emstをマージ（結合）する
    tbl_merged = pd.merge(tbl, fmst_fval, on='cd', how='left')
    tbl_merged = pd.merge(tbl_merged, emst_eval, on='cd', how='left')

    # 各行から適切なval値を抽出し、new_val列に保存
    set_new_val(tbl_merged, "f_val")
    set_new_val(tbl_merged, "e_val")
    tbl_merged.loc[tbl_merged["val"].map(is_not_nan), "new_val"] = \
        tbl_merged.loc[tbl_merged["val"].map(is_not_nan), "val"]

    # 必要な列のみを抽出し、新しいdfを作成
    tbl = tbl_merged[["cd", "new_val"]]
    tbl = tbl.rename(columns={'new_val': 'val'})

    return tbl
