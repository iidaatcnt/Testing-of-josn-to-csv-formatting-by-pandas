import numpy as np
import pandas as pd
import math

# 更新用df
tbl = pd.DataFrame(
    [
    {"cd":"F001","val":None},
    {"cd":"E001","val":None},
    {"cd":"X001","val":None},
    {"cd":"F001","val":''},
    {"cd":"E001","val":''},
    {"cd":"X001","val":''},
    {"cd":"F001","val":100},
    {"cd":"E001","val":200},
    {"cd":"X001","val":300}
    ],columns=["cd","val"]
)
# 参照df その１
fmst = pd.DataFrame(
    [
    {"cd":"F001","val":1},
    {"cd":"F002","val":2},
    {"cd":"F003","val":3}
    ],columns=["cd","val"]
)
# 参照df その２
emst = pd.DataFrame(
    [
    {"cd":"E001","val":4},
    {"cd":"E002","val":5}, # "cd":"E001" となっていたので"cd":"E002"に修正しました。
    {"cd":"E003","val":6} # "cd":"E001" となっていたので"cd":"E003"に修正しました。
    ],columns=["cd","val"]
)

# 後の確認等をやりやすくするために関数化しました。
def create_tbl():
    tbl = pd.DataFrame(
        [
        {"cd":"F001","val":None},
        {"cd":"E001","val":None},
        {"cd":"X001","val":None},
        {"cd":"F001","val":''},
        {"cd":"E001","val":''},
        {"cd":"X001","val":''},
        {"cd":"F001","val":100},
        {"cd":"E001","val":200},
        {"cd":"X001","val":300}
        ],columns=["cd","val"]
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


def set_new_vel(tbl_merged, x_val):
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
    tbl_merged.loc[tbl_merged["val"].map(math.isnan) & tbl_merged[x_val].map(is_not_nan), "new_val"] = \
        tbl_merged.loc[tbl_merged["val"].map(math.isnan) & tbl_merged[x_val].map(is_not_nan), x_val]

def fillnan_mst(tbl, fmst, emst):
    """
    func
    tblのvalがNanのとき、
    cdが'F'で始まる時は、fmstのvalで補完埋めします
    cdが'E'で始まる時は、emstのvalで補完埋めします
    それ以外のときはNanのままにします。
    In
    tbl : columns=["cd","val"]のpd.DataFrame（穴埋め更新対象）
    fmst : columns=["cd","val"]のpd.DataFrame（参照用）
    emst : columns=["cd","val"]のpd.DataFrame（参照用）
    Out
    fmst, emstを参照してNanを補完埋めしたtbl
    """
    # tblのval列と区別するためにfmst, emstのval列の列名を変更
    fmst_fval = fmst.rename(columns={'val': 'f_val'})
    emst_eval = emst.rename(columns={'val': 'e_val'})

    # tblにfmst, emstをマージ（結合）する
    tbl_merged = pd.merge(tbl, fmst_fval, on='cd', how='left')
    tbl_merged = pd.merge(tbl_merged, emst_eval, on='cd', how='left')

    # 各行から適切なval値を抽出し、new_val列に保存
    set_new_vel(tbl_merged, "f_val")
    set_new_vel(tbl_merged, "e_val")
    tbl_merged.loc[tbl_merged["val"].map(is_not_nan), "new_val"] = \
        tbl_merged.loc[tbl_merged["val"].map(is_not_nan), "val"]

    # 必要な列のみを抽出し、新しいdfを作成
    tbl = tbl_merged[["cd", "new_val"]]
    tbl = tbl.rename(columns={'new_val': 'val'})

    return tbl

tbl = create_tbl()

tbl = fillnan_mst(tbl, fmst, emst)

print('--fillnan_mst()\n', tbl)


def create_table_large():
    tbl_large = pd.DataFrame(
        [
            {"cd": "F001", "val": None},
            {"cd": "E001", "val": None},
            {"cd": "X001", "val": None},
            {"cd": "F001", "val": ''},
            {"cd": "E001", "val": ''},
            {"cd": "X001", "val": ''},
            {"cd": "F001", "val": 100},
            {"cd": "E001", "val": 200},
            {"cd": "X001", "val": 300},
            {"cd": "F002", "val": None},
            {"cd": "E002", "val": None},
            {"cd": "X002", "val": None},
            {"cd": "F002", "val": ''},
            {"cd": "E002", "val": ''},
            {"cd": "X002", "val": ''},
            {"cd": "F002", "val": 100},
            {"cd": "E002", "val": 200},
            {"cd": "X002", "val": 300},
            {"cd": "F003", "val": None},
            {"cd": "E003", "val": None},
            {"cd": "X003", "val": None},
            {"cd": "F003", "val": ''},
            {"cd": "E003", "val": ''},
            {"cd": "X003", "val": ''},
            {"cd": "F003", "val": 100},
            {"cd": "E003", "val": 200},
            {"cd": "X003", "val": 300},
        ], columns=["cd", "val"]
    )
    tbl_large = tbl_large.replace({'': None})

    return tbl_large

tbl_large = create_table_large()

tbl_large = fillnan_mst(tbl_large, fmst, emst)

print('--fillnan_mst()\n',tbl_large)
