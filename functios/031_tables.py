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
fmst = pd.DataFrame(
    [
    {"lcd":"F001","price":1}, 
    {"lcd":"F003","price":''}
    ],columns=["lcd","price"]
)
# 参照df その２
emst = pd.DataFrame(
    [
    {"lcd":"E001","price":2},
    {"lcd":"E003","price":''}
    ],columns=["lcd","price"]
)

print('--df--\n',df)
print('--emst--\n',emst)
print('--fmst--\n',fmst)
