
# coding: utf-8

# In[27]:


# 欠損値の穴埋め
import numpy as np
import pandas as pd
dfm = pd.DataFrame(
    [
    {"hash":10,"age":28,"wt":56.1},
    {"hash":20,"age":None,"wt":None},
    {"hash":30,"age":'',"wt":''},
    {"hash":40,"name":33,"wt":100}
    ],columns=["hash","age","wt"]
)
dfm



# In[28]:


dfm['wt'].map(type)


# In[30]:


# 空文字はNone扱い
dfm = dfm.replace('', None)
dfm


# In[34]:


# 欠損箇所を埋める既定値には列ごとにある。データはintとflortの場合がある
# これはダメなケース
AGE_DEFAULT = 99
WT_DEFAULT = 99.9

dfm = dfm.fillna(99)

dfm


# In[ ]:


# 仕様検討中
# 　既定値の値もデータ型もそのまま変えずに穴埋めをしたい。
# 　穴埋めの既定値を基本的にint型として、float型で穴埋めしたい列名はリストにして引数で指定する
#　列内のNoneのところだけに穴埋め処理し、他は影響しないようにしたい

