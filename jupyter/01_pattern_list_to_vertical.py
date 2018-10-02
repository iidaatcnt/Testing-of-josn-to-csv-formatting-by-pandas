
# coding: utf-8

# In[2]:


# 以下のReserveのように横持（リスト）を縦持ちに展開する関数を作成してください

import numpy as np
import pandas as pd
dfm = pd.DataFrame(
    [
    {"Pos":"QB","regular":12,"Reserve":[9,8]},
    {"Pos":"CB","regular":28,"Reserve":[37,23,38,20]},
    {"Pos":"WR","regular":19,"Reserve":[83,82,81,17,18]},
    {"Pos":"T","regular":69,"Reserve":[75,78]},
    {"Pos":"S","regular":36,"Reserve":[35,21,29,27]},
    {"Pos":"RB","regular":22,"Reserve":[33,88,30]}
    ]
     ,columns=["Pos","regular","Reserve"]
)
dfm


# In[4]:


# 横持（リスト部分だった部分）を縦持に整形する
import numpy as np
import pandas as pd
dfm = pd.DataFrame(
    [
    {"Pos":"QB","regular":12,"Reserve":[9]},
    {"Pos":"QB","regular":12,"Reserve":[8]},
    {"Pos":"CB","regular":28,"Reserve":[37]},
    {"Pos":"CB","regular":28,"Reserve":[23]},
    {"Pos":"CB","regular":28,"Reserve":[38]},
    {"Pos":"CB","regular":28,"Reserve":[20]},
    {"Pos":"WR","regular":19,"Reserve":[83]},
    {"Pos":"WR","regular":19,"Reserve":[82]},
    {"Pos":"WR","regular":19,"Reserve":[81]},
    {"Pos":"WR","regular":19,"Reserve":[17]},
    {"Pos":"T","regular":69,"Reserve":[75]},
    {"Pos":"T","regular":69,"Reserve":[78]},
    {"Pos":"S","regular":36,"Reserve":[35]},
    {"Pos":"S","regular":36,"Reserve":[21]},
    {"Pos":"S","regular":36,"Reserve":[29]},
    {"Pos":"S","regular":36,"Reserve":[27]},
    {"Pos":"RB","regular":22,"Reserve":[33]},
    {"Pos":"RB","regular":22,"Reserve":[88]},
    {"Pos":"RB","regular":22,"Reserve":[30]}
    ]
     ,columns=["Pos","regular","Reserve"]
)
dfm


# In[ ]:


# 01_pattern_list_to_vertical.py
dfm = pd.DataFrame(
    [
    {"Pos":"QB","regular":12,"Reserve":[9,8]},
    {"Pos":"CB","regular":28,"Reserve":[37,23,38,20]},
    {"Pos":"WR","regular":19,"Reserve":[83,82,81,17,18]},
    {"Pos":"T","regular":69,"Reserve":[75,78]},
    {"Pos":"S","regular":36,"Reserve":[35,21,29,27]},
    {"Pos":"RB","regular":22,"Reserve":[33,88,30]}
    ]
)
to_vertical_columns = '"Reserve"
outname = pattern_list_to_vertical.csv

import numpy as np
import pandas as pd

def pattern_list_to_vertical(dfm, to_vertical_column, outname)
  """
  input
    dfm
    to_vertical_columns
  output
    pattern_list_to_vertical.csv
  """
   :
    ここに処理を書く
　：    
  to_csv(outname)
        


