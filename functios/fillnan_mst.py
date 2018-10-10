#!/usr/bin/env python
# coding: utf-8

# # 032_欠損値を複数の参照dfを参照して穴埋めする関数を作成(その２)
#
# ## 目的
#
# - 更新用データフレームの欠損値を別にある参照用データフレームの値で
#   穴埋めしたい
#
# ## 条件
#
# - 使用する情報は、データフレームは更新用（tbl）と
#   参照用データフレームが２つ(emst、fmst)、priceの初期値（固定値）
# - tbl.priceが欠損値の時に以下の条件で穴埋め処理を行う
#
# ### ルール１
# - tbl.lcdがEで始まる時は、emstのpriceで埋めます
# - tbl.lcdがE始まりではないときは、fmstのpriceで埋めます
#
# ### ルール２
# - emst.lcd、fmst.lcdにtbl.mstと同じlcdがない場合があります。
# - emst.lcd、fmst.lcdにtbl.mstと同じlcdがあっても該当するpriceの値が
#   入っていない場合があります。
#
# ### ルール３
# - 上のルールで価が決まらない場合には、予め決めて置いた固定値で
#   埋めてしまいます
#


import math
import numpy as np
import pandas as pd


# ## 処理：参照dfを使用して欠損値を埋める

def is_e_start(lcd):
    """
    func
    tbl.lcdがE始まりではないときに、先頭の1文字（アルファベット）を除外する
    In
    lcd : 先頭がEかどうかを判定したい値
    Out
    lcdの値（str型）
    """
    start_str = "E"
    index = 1

    if lcd.startswith(start_str):
        return lcd
    else:
        return lcd[index:]


def is_not_nan(val):
    """
    func
    mapメソッドのために「NaNでなければTrueを返す」関数
    In
    x : NaNでないことを判定したい値
    Out
    bool値
    """
    return not math.isnan(val)


def set_new_price(tbl_merged, x_price):
    """
    func
    マージ後のdfにおいて、price列がNaNかつfmstまたはemstの値があるとき、
    dfのnew_price列にfmstまたはemstの値を代入する
    In
    tbl_merged : fmst, emstをマージしたtbl
    x_price : "f_price"または"e_price"を指定
    Out
    なし（tbl_mergedが直接修正される）
    """
    tbl_merged.loc[tbl_merged["price"].map(math.isnan) & \
        tbl_merged[x_price].map(is_not_nan), "new_price"] = \
        tbl_merged.loc[tbl_merged["price"].map(math.isnan) & \
        tbl_merged[x_price].map(is_not_nan), x_price]


def fillnan_mst(update_tbl, emst, fmst, mst_init):
    """
    func
    update_tblのpriceがNan、""のとき、
    1. df.lcdがEで始まる時は、該当するdf.epriceで値を埋めます。
    2. df.lcdがE始まりではない時は、該当するdf.fpriceで値を埋めます。
    3. emst、fmstにキーがない、またはあっても値が入っていない場合、
       固定値（mst_init）で埋めます。
    In
    update_tbl : columns=["lcd", "product", "price"]のpd.DataFrame（穴埋め更新対象）
    emst : columns=["lcd","price"]のpd.DataFrame（参照用）
    fmst : columns=["lcd","price"]のpd.DataFrame（参照用）
    mst_init : 固定値
    Out
    emst, fmst, mst_initを参照してNanを補完埋めしたupdate_tbl
    """
    # 1,. 処理の準備
    # df <- update_tbl + emst.price + fmst.price のように結合します。

    # update_tblのprice列と区別するためにfmst, emstのprice列の列名を変更
    emst_eprice = emst.rename(columns={"price": "e_price"})
    fmst_fprice = fmst.rename(columns={"price": "f_price"})

    # update_tblにfmst, emstをマージ（結合）する
    # update_tblにemstをマージ（結合）
    tbl_merged = pd.merge(update_tbl, emst_eprice, on="lcd", how="left")

    # update_tblにfmstをマージ（結合）
    # update_tbl.lcdがE始まりではないときに、fmstのpriceで埋めるためにマージを工夫
    # 先頭のアルファベット1文字は無視し、数値の一致のみで判断する。
    tbl_merged["not_E_lcd"] = tbl_merged["lcd"]
    tbl_merged["not_E_lcd"] = tbl_merged["not_E_lcd"].map(is_e_start)
    fmst_fprice["not_E_lcd"] = fmst_fprice["lcd"]
    fmst_fprice["not_E_lcd"] = fmst_fprice["not_E_lcd"].map(is_e_start)
    tbl_merged = pd.merge(tbl_merged, fmst_fprice, on="not_E_lcd", how="left")

    # df.priceの""をNaNで埋める。Noneがある場合はNaNに揃える。
    nan_replace_list = ["price", "e_price", "f_price"]
    for col_name in nan_replace_list:
        tbl_merged[col_name] = tbl_merged[col_name].replace("", np.nan)
        tbl_merged.loc[tbl_merged[col_name].isnull(), col_name] = np.nan

    # 2.  emstとfmstの値で埋める
    # new_price列に値を入れていく
    # 2-1. df.priceが欠損している時、df.lcdがEで始まる時は、
    #      該当するdf.epriceで値を埋めます。
    # 2-2.E始まりではない時は、該当するdf.fpriceで値を埋めます。
    set_new_price(tbl_merged, "e_price")
    set_new_price(tbl_merged, "f_price")
    # 元からある値をコピーします。
    tbl_merged.loc[tbl_merged["price"].map(is_not_nan), "new_price"] = \
        tbl_merged.loc[tbl_merged["price"].map(is_not_nan), "price"]
    # 3.df.priceが欠損していたら固定値で埋めます
    tbl_merged["new_price"] = tbl_merged["new_price"].fillna(mst_init)

    # 必要な列のみを抽出し、新しいdfを作成
    update_tbl = tbl_merged[["lcd_x", "product", "new_price"]]
    update_tbl = tbl.rename(columns={"lcd_x": "lcd", "new_price": "price"})

    return update_tbl


if __name__ == "__main__":
    # init
    MST_INIT = 99

    # 参照df その１
    EMST = pd.DataFrame(
        [
            {"lcd": "E001", "price": 1},
            {"lcd": "E002", "price": ''}
        ], columns=["lcd", "price"]
    )
    # 参照df その２
    FMST = pd.DataFrame(
        [
            {"lcd": "F001", "price": 2},
            {"lcd": "F002", "price": ''}
        ], columns=["lcd", "price"]
    )

    # 更新tbl
    def create_tbl():
        """
        func
        テスト用のテーブルを作成
        In
        no input
        Out
        テスト用テーブル
        """
        test_tbl = pd.DataFrame(
            [
                {"lcd": "E001", "product": "abc", "price": 100},
                {"lcd": "E001", "product": "abc", "price": ''},
                {"lcd": "E001", "product": "abc", "price": None},
                {"lcd": "E002", "product": "abc", "price": ''},
                {"lcd": "E002", "product": "abc", "price": None},
                {"lcd": "E003", "product": "abc", "price": ''},
                {"lcd": "E003", "product": "abc", "price": None},
                {"lcd": "F001", "product": "abc", "price": 100},
                {"lcd": "F001", "product": "abc", "price": ''},
                {"lcd": "F001", "product": "abc", "price": None},
                {"lcd": "F002", "product": "abc", "price": ''},
                {"lcd": "F002", "product": "abc", "price": None},
                {"lcd": "F003", "product": "abc", "price": ''},
                {"lcd": "F003", "product": "abc", "price": None}
            ], columns=["lcd", "product", "price"]
        )
        return test_tbl

    TBL = create_tbl()
    print(TBL)
    print("============================")

    tbl = fillnan_mst(TBL, EMST, FMST, MST_INIT)

    print(tbl)
