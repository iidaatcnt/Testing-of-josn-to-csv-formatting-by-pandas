
# coding: utf-8

# In[6]:


# はじめに
#
# この一連の欠損値の穴埋めをみてください

import numpy as np
import pandas as pd

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
    {"cd":"E001","val":5},
    {"cd":"E001","val":6}
    ],columns=["cd","val"]
)

emst


# In[7]:


# 期待する結果の更新用df状態です
tbl = pd.DataFrame(
    [
    {"cd":"F001","val":1}, 
    {"cd":"E001","val":4},
    {"cd":"X001","val":None},
    {"cd":"F001","val":1}, 
    {"cd":"E001","val":4},
    {"cd":"X001","val":None},
    {"cd":"F001","val":100}, 
    {"cd":"E001","val":200},
    {"cd":"X001","val":300}
    ],columns=["cd","val"]
)
tbl


# In[13]:


# 'いけね、'(空文字)は欠損値ではないのか？この対処はこちらでやります。
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
tbl

