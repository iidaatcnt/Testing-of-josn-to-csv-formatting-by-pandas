import pandas as pd
import numpy as np
import math

init_val = 99

df = pd.DataFrame(
    [
     {"lcd": "E00", "product": "item1", "price": 100},
     {"lcd": "E01", "product": "item1", "price": ''},
     {"lcd": "E02", "product": "item1", "price": ''},
     {"lcd": "F00", "product": "item1", "price": 300},
     {"lcd": "F01", "product": "item1", "price": ''},
     {"lcd": "F02", "product": "item1", "price": ''}
     ],
    columns=["lcd", "product", "price"]
)

mst_e = pd.DataFrame(
    [{"lcd": "E01", "price": 123}],
    columns=["lcd", "price"]
)

mst_o = pd.DataFrame(
    [{"lcd": "F01", "price": 456}],
    columns=["lcd", "price"]
)

# df2 = pd.DataFrame(
#     {
#         "lcd": ["E00", "E00","E00", "E00"],
#         "price": [100, 100, 100, 200]
#     }
# )

# print(mst_e)
# print(mst_o)
# print(df)

mst_e = mst_e.rename(columns={'price': 'e_price'})
mst_o = mst_o.rename(columns={'price': 'o_price'})
# print(mst_e)
# print(mst_o)

# print(pd.concat([mst_e, mst_o]))
# print(pd.concat([df, mst_o], axis=1))

# df = pd.concat([df, mst_o], axis=1, join_axes=[df.index])
# df = pd.concat([df, mst_e], axis=1, join_axes=[df.index])
# df = pd.merge(df, mst_o, on='lcd')

# df <- df + mst_o + mst_e
df = pd.merge(df, mst_o, on='lcd', how='left')
df = pd.merge(df, mst_e, on='lcd', how='left')

# ''() -> None
# df = df.replace({'': None})


print('--df--1\n', df)

# df.loc[df["price"]., "e_price"] = \
#     tbl_merged.loc[tbl_merged["val"].map(math.isnan) & tbl_merged[x_val].map(is_not_nan), x_val]

# Nanがあるか判断する
# print('--df--add\n',df.isnull())

# loc でブールインデックス参照
# df.loc[df['price'] == '', 'price'] = -10
# https://qiita.com/knknkn1162/items/f4b706d6d678d32ce08f

# df.loc[(df['price'] == ''& df['lcd'].startswith('E')), 'price'] = df['e_price']
# print(df.isnull(df.at[0,'price']))
# print(df.loc['price'].isnull())

# fill na
# df['price'] = df['price'].fillna(init_val)

print('--df--2\n', df)

