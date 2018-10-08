import numpy as np
import pandas as pd
import math

# init
mst_init = 99

# 参照df その１
emst = pd.DataFrame(
    [
    {"lcd":"E001","price":1},
    {"lcd":"E002","price":3}
    ],columns=["lcd","price"]
)
# 参照df その２
fmst = pd.DataFrame(
    [
    {"lcd":"F001","price":2},
    {"lcd":"F002","price":4}
    ],columns=["lcd","price"]
)

# 更新tbl
def create_tbl():
    tbl = pd.DataFrame(
        [
        {"lcd": "E001", "product": "abc", "price": 100},
        {"lcd": "E001", "product": "abc", "price": ''},
        {"lcd": "E001", "product": "abc", "price": None},
        {"lcd": "E002", "product": "abc", "price": ''},
        {"lcd": "E002", "product": "abc", "price": None},
        {"lcd": "E003", "product": "abc", "price": ''},
        {"lcd": "E003", "product": "abc", "price": None},
        {"lcd": "F001", "product": "abc", "price": 200},
        {"lcd": "F001", "product": "abc", "price": ''},
        {"lcd": "F001", "product": "abc", "price": None},
        {"lcd": "F002", "product": "abc", "price": ''},
        {"lcd": "F002", "product": "abc", "price": None},
        {"lcd": "F003", "product": "abc", "price": ''},
        {"lcd": "F003", "product": "abc", "price": None}
        ],columns=["lcd", "product", "price"]
    )
    tbl = tbl.replace({'': None})
    return tbl

tbl = create_tbl()
print('--create_tbl()\n',tbl)

def is_not_nan(x):
    """
    func
    mapメソッドのために「NaNでなければTrueを返す」関数
    In
    x ; NaNでないことを判定したい値
    Out
    bool値
    """
    return not math.isnan(x)


def set_new_vel(tbl_merged, x_price):
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
    tbl_merged.loc[tbl_merged["price"].map(math.isnan) & tbl_merged[x_price].map(is_not_nan), "new_price"] = \
        tbl_merged.loc[tbl_merged["price"].map(math.isnan) & tbl_merged[x_price].map(is_not_nan), x_price]

def fillnan_mst(tbl, fmst, emst):
    """
    func
    tblのpriceがNanのとき、
    lcdが'F'で始まる時は、fmstのpriceで補完埋めします
    lcdが'E'で始まる時は、emstのpriceで補完埋めします
    それ以外のときはNanのままにします。
    In
    tbl : columns=["lcd","price"]のpd.DataFrame（穴埋め更新対象）
    fmst : columns=["lcd","price"]のpd.DataFrame（参照用）
    emst : columns=["lcd","price"]のpd.DataFrame（参照用）
    Out
    fmst, emstを参照してNanを補完埋めしたtbl
    """
    # tblのprice列と区別するためにfmst, emstのprice列の列名を変更
    fmst_fprice = fmst.rename(columns={'price': 'f_price'})
    emst_eprice = emst.rename(columns={'price': 'e_price'})

    # tblにfmst, emstをマージ（結合）する
    tbl_merged = pd.merge(tbl, fmst_fprice, on='lcd', how='left')
    tbl_merged = pd.merge(tbl_merged, emst_eprice, on='lcd', how='left')

    # 各行から適切なprice値を抽出し、new_price列に保存
    set_new_vel(tbl_merged, "f_price")
    set_new_vel(tbl_merged, "e_price")
    tbl_merged.loc[tbl_merged["price"].map(is_not_nan), "new_price"] = \
        tbl_merged.loc[tbl_merged["price"].map(is_not_nan), "price"]

    # 必要な列のみを抽出し、新しいdfを作成
    tbl = tbl_merged[["lcd", "new_price"]]
    tbl = tbl.rename(columns={'new_price': 'price'})

    return tbl


# 準備
tbl = create_tbl()

# 補完処理
tbl = fillnan_mst(tbl, fmst, emst)

print('--fillnan_mst()\n', tbl)
