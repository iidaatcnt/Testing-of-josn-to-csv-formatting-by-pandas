

```python
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
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cd</th>
      <th>val</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>F001</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>E001</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>X001</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>F001</td>
      <td></td>
    </tr>
    <tr>
      <th>4</th>
      <td>E001</td>
      <td></td>
    </tr>
    <tr>
      <th>5</th>
      <td>X001</td>
      <td></td>
    </tr>
    <tr>
      <th>6</th>
      <td>F001</td>
      <td>100</td>
    </tr>
    <tr>
      <th>7</th>
      <td>E001</td>
      <td>200</td>
    </tr>
    <tr>
      <th>8</th>
      <td>X001</td>
      <td>300</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cd</th>
      <th>val</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>F001</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>E001</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>X001</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>F001</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>E001</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>X001</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>F001</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>E001</td>
      <td>200.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>X001</td>
      <td>300.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cd</th>
      <th>val</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>F001</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>E001</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>X001</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>F001</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>E001</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>X001</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>F001</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>E001</td>
      <td>200.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>X001</td>
      <td>300.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# ルール１　tblのvalの欠損値の時に穴埋め処理をする。具体的なルールは以下の３つ（ルール２からルール４）。
# ルール２　tblのcdの値がFで始まる文字列の場合（例：F001）の場合は、fmstのval値で（例：F001なので1）欠損値の穴埋めをする
# ルール３　tblのcdの値がEで始まる文字列の場合（例：E001）の場合は、emstのval値で（例：E001なので4）欠損値の穴埋めをする
# ルール４　tblのcdの値の始まりがFでもEでもない場合（例：X001）は欠損値のままにしておく。
```


```python
# 実験１：tblのcdがFで始まる文字列
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
tbl[tbl['cd'].str.startswith("F")]
# 結果はOKなようです

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cd</th>
      <th>val</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>F001</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>F001</td>
      <td></td>
    </tr>
    <tr>
      <th>6</th>
      <td>F001</td>
      <td>100</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 実験２：tblのvalが欠損値
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
tbl['val'].isnull()
#　結果はOKなようです
```




    0     True
    1     True
    2     True
    3    False
    4    False
    5    False
    6    False
    7    False
    8    False
    Name: val, dtype: bool




```python
# 実験３
# tblでcdがFで始まる文字列のValにスカラー値を代入する
# 参考情報　https://note.nkmk.me/python-pandas-where-mask/
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
tbl.loc[tbl['cd'].str.startswith("F"),'val' ] = -100
tbl
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cd</th>
      <th>val</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>F001</td>
      <td>-100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>E001</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>X001</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>F001</td>
      <td>-100</td>
    </tr>
    <tr>
      <th>4</th>
      <td>E001</td>
      <td></td>
    </tr>
    <tr>
      <th>5</th>
      <td>X001</td>
      <td></td>
    </tr>
    <tr>
      <th>6</th>
      <td>F001</td>
      <td>-100</td>
    </tr>
    <tr>
      <th>7</th>
      <td>E001</td>
      <td>200</td>
    </tr>
    <tr>
      <th>8</th>
      <td>X001</td>
      <td>300</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 実験４
# blでcdがFで始まる文字列で、valがNanにスカラー値を代入する
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
#tbl.loc[ tbl['cd'].str.startswith("F") & True ,'val' ] = -100
#
# このTrueにtbl.isnull()
#
tbl.loc[ tbl['cd'].str.startswith("F") & tbl['val'].isnull() ,'val' ] = -100
tbl
#
# ここまではできました。
#  cdの文字列の初めの文字は判断できます
#  valが欠損値なのも判断できます
# その条件に剃ってスカラー値を代入することもできます
```


```python

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cd</th>
      <th>val</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>F001</td>
      <td>-10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>E001</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>X001</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>F001</td>
      <td></td>
    </tr>
    <tr>
      <th>4</th>
      <td>E001</td>
      <td></td>
    </tr>
    <tr>
      <th>5</th>
      <td>X001</td>
      <td></td>
    </tr>
    <tr>
      <th>6</th>
      <td>F001</td>
      <td>100</td>
    </tr>
    <tr>
      <th>7</th>
      <td>E001</td>
      <td>200</td>
    </tr>
    <tr>
      <th>8</th>
      <td>X001</td>
      <td>300</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 実験５　参照用dfから値を取得する
#

# 参照df その１
fmst = pd.DataFrame(
    [
    {"cd":"F001","val":1}, 
    {"cd":"F002","val":2},
    {"cd":"F003","val":3}
    ],columns=["cd","val"]
)
key = "F002"
fmst['cd'] == key 

# tblの埋めに使う値はcdをキーに参照用dfから持ってくる必要があります。
```




    0    False
    1     True
    2    False
    Name: cd, dtype: bool


