import numpy as np
import pandas as pd

# 更新用df
df = pd.DataFrame(
    [
    {"lcd":"E001","price":100},
    {"lcd":"E002","price":''},
    {"lcd":"E003","price":None},
    {"lcd":"F001","price":100},
    {"lcd":"F002","price":''},
    {"lcd":"F003","price":None}
    ],columns=["lcd","price"]
)
# 参照df その１
emst = pd.DataFrame(
    [
    {"lcd":"E001","price":2},
    {"lcd":"E003","price":''}
    ],columns=["lcd","price"]
)

# 参照df その２
fmst = pd.DataFrame(
    [
    {"lcd":"F001","price":1}, 
    {"lcd":"F003","price":''}
    ],columns=["lcd","price"]
)

print('--df--befor\n',df)

fmst = fmst.rename(columns={'price': 'eprice'})
emst = emst.rename(columns={'price': 'fprice'})
print('--emst--\n',emst)
print('--fmst--\n',fmst)

# df = df.merge(df, emst, on='lcd', how='left')
# df = df.merge(df, fmst, on='lcd', how='left')

print('--df--after\n',df)
