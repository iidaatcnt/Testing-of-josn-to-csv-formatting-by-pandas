import pandas as pd
import numpy as np

df = pd.DataFrame([
    {"kind": "A00", "cd": "100", "pri": 200, "sec": 20},
    {"kind": "A00", "cd": "100", "pri": 200, "sec": 20},
    {"kind": "A00", "cd": "100", "pri": 200, "sec": 20},
    {"kind": "B00", "cd": "100", "pri": 300, "sec": 30},
    {"kind": "C00", "cd": "100", "pri": 300, "sec": 30},
    {"kind": "D00", "cd": "100", "pri": 300, "sec": 30}
])


mst = pd.DataFrame([
    {"kind": "A00", "price": 200},
    {"kind": "A00", "price": 200},
    {"kind": "B00", "price": 300},
    {"kind": "C00", "price": 300}
])

df.loc[(df['kind'].str.startswith('A')), 'cd'] = mst['price']

print(df)

df = pd.DataFrame([
    {"cd": "a10", "price": 'x', "cd": 100, "price": 11},
    {"cd": "b10", "price": '', "cd": 100, "price": 22},
    {"cd": "b10", "price": '', "cd": 100, "price": 33},
    {"cd": "b10", "price": '', "cd": 100, "price": 44}
], columns=["cd","cd","price"])

# df.loc[(df['cd'].str.startswith('cd') & (df['price'].isnull())) ,'cd'] = df['price']
#
# print(df)
