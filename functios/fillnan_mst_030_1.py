"""
030-1
以下の条件に沿って、参照dfmを元に欠損値を埋める
- tblのvalの欠損値の時に穴埋め処理をする。
  具体的なルールは以下の３つ（ルール２からルール４）。
- tblのcdの値がFで始まる文字列の場合（例：F001）の場合は、
  fmstのval値で（例：F001なので1）欠損値の穴埋めをする
- tblのcdの値がEで始まる文字列の場合（例：E001）の場合は、
  emstのval値で（例：E001なので4）欠損値の穴埋めをする
- tblのcdの値の始まりがFでもEでもない場合（例：X001）は欠損値のままにしておく。

for文による処理版
行方向への繰り返し処理のため、処理が遅くなりがち
マージ（結合）による処理ができたのでfor文による処理は不要
コードは短く、理解しやすい
参考程度
"""

import math


def fillnan_mst_for(tbl, fmst, emst):
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
    out
    fmst, emstを参照してNanを補完埋めしたpd.DataFrame
    """
    for i in range(len(tbl)):
        # ''をNoneに置き換え
        tbl = tbl.replace({'': None})
        if math.isnan(tbl.loc[i, "val"]):
            if tbl.loc[i, "cd"].startswith("F"):
                tbl.loc[i, "val"] = fmst[
                    fmst["cd"] == tbl.loc[i, "cd"]]["val"].values[0]
            elif tbl.loc[i, "cd"].startswith("E"):
                tbl.loc[i, "val"] = emst[
                    emst["cd"] == tbl.loc[i, "cd"]]["val"].values[0]

    return tbl
