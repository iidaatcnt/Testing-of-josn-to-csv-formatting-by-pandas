"""
032_part
emst, fmstをマージ後のdfmについて、
（ tbl_merged.priceがNone）　and  （lcd がEで始まる）ときに
tbl_merged.priceにe_priceを代入
（実際にはNoneではなくNaNに対しての処理）
"""

import math
import numpy as np


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


def fillnan_e_price(tbl_merged, cols):
    """
    func
    マージ後のdfmについて、
    （ tbl_merged.priceがNone）　and  （lcd がEで始まる）時に
    tbl_merged.priceにe_priceを代入
    In
    tbl_merged : マージ後のpd.DataFrame（穴埋め更新対象）
    cols : キーとして使用するlcd、欠損値を埋めるprice、
           欠損値を埋める参考にするe_priceについて、
           適切な列名をdictで指定する
           {"lcd": "...", "price": "...", "e_price": "..."}
    Out
    欠損値をemstで補完埋めし、必要な列だけ抽出したpd.DataFrame
    """

    # dfm.priceの""をNaNで埋める
    nan_replace_list = tbl_merged.columns
    for col_name in nan_replace_list:
        tbl_merged[col_name] = tbl_merged[col_name].replace("", np.nan)
        tbl_merged.loc[tbl_merged[col_name].isnull(), col_name] = np.nan

    # 処理に必要な列名を変数に代入
    x_price = cols["e_price"]
    price = cols["price"]
    lcd = cols["lcd"]

    # （ tbl_merged.priceがNone）　and  （lcd がEで始まる）ときに
    # tbl_merged.priceにe_priceを代入
    tbl_merged.loc[tbl_merged[price].map(math.isnan) & \
     tbl_merged[x_price].map(is_not_nan), "new_price"] = \
     tbl_merged.loc[tbl_merged[price].map(math.isnan) & \
     tbl_merged[x_price].map(is_not_nan), x_price]

    # それ以外のときにもとの値を置いておく
    tbl_merged.loc[tbl_merged[price].map(is_not_nan), "new_price"] = \
     tbl_merged.loc[tbl_merged[price].map(is_not_nan), price]

    # 必要な列を抽出
    tbl = tbl_merged[[lcd, "product", "new_price"]]

    # 列名を整える
    tbl = tbl.rename(columns={lcd: "lcd", "new_price": "price"})

    return tbl
