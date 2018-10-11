
# 032_欠損値を複数の参照dfを参照して穴埋めする関数を作成(その２)

## 目的

- 更新用データフレームの欠損値を別にある参照用データフレームの値で穴埋めしたい

## 条件

- 使用する情報は、データフレームは更新用（tbl）と参照用データフレームが２つ(emst、fmst)、priceの初期値（固定値）
- tbl.priceが欠損値の時に以下の条件で穴埋め処理を行う

### ルール１
- tbl.lcdがEで始まる時は、emstのpriceで埋めます
- tbl.lcdがE始まりではないときは、fmstのpriceで埋めます

### ルール２
- emst.lcd、fmst.lcdにtbl.mstと同じlcdがない場合があります。
- emst.lcd、fmst.lcdにtbl.mstと同じlcdがあっても該当するpriceの値が入っていない場合があります。

### ルール３
- 上のルールで価が決まらない場合には、予め決めて置いた固定値でで埋めてしまいます


## 1. 入力：データフレームを作成


```python
import pandas as pd


# init
mst_init = 99

# 参照df その１
emst = pd.DataFrame(
    [
    {"lcd":"E001","price":1},
    {"lcd":"E002","price":''}
    ],columns=["lcd","price"]
)
# 参照df その２
fmst = pd.DataFrame(
    [
    {"lcd":"F001","price":2},
    {"lcd":"F002","price":''}
    ],columns=["lcd","price"]
)

# 更新tbl
def create_tbl():
    tbl = pd.DataFrame(
        [
        {"lcd": "E001", "product": "abc", "price": 100},
        {"lcd": "E001", "product": "abc", "price": ''},
        {"lcd": "E001", "product": "abc", "price": None},
        {"lcd": "E002", "product": "abc", "price": ''},
        {"lcd": "E002", "product": "abc", "price": None},
        {"lcd": "E003", "product": "abc", "price": ''},
        {"lcd": "E003", "product": "abc", "price": None},
        {"lcd": "F001", "product": "abc", "price": 100},
        {"lcd": "F001", "product": "abc", "price": ''},
        {"lcd": "F001", "product": "abc", "price": None},
        {"lcd": "F002", "product": "abc", "price": ''},
        {"lcd": "F002", "product": "abc", "price": None},
        {"lcd": "F003", "product": "abc", "price": ''},
        {"lcd": "F003", "product": "abc", "price": None}
        ],columns=["lcd", "product", "price"]
    )
    return tbl

tbl = create_tbl()
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
      <th>lcd</th>
      <th>product</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>E001</td>
      <td>abc</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>E001</td>
      <td>abc</td>
      <td></td>
    </tr>
    <tr>
      <th>2</th>
      <td>E001</td>
      <td>abc</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>E002</td>
      <td>abc</td>
      <td></td>
    </tr>
    <tr>
      <th>4</th>
      <td>E002</td>
      <td>abc</td>
      <td>None</td>
    </tr>
    <tr>
      <th>5</th>
      <td>E003</td>
      <td>abc</td>
      <td></td>
    </tr>
    <tr>
      <th>6</th>
      <td>E003</td>
      <td>abc</td>
      <td>None</td>
    </tr>
    <tr>
      <th>7</th>
      <td>F001</td>
      <td>abc</td>
      <td>100</td>
    </tr>
    <tr>
      <th>8</th>
      <td>F001</td>
      <td>abc</td>
      <td></td>
    </tr>
    <tr>
      <th>9</th>
      <td>F001</td>
      <td>abc</td>
      <td>None</td>
    </tr>
    <tr>
      <th>10</th>
      <td>F002</td>
      <td>abc</td>
      <td></td>
    </tr>
    <tr>
      <th>11</th>
      <td>F002</td>
      <td>abc</td>
      <td>None</td>
    </tr>
    <tr>
      <th>12</th>
      <td>F003</td>
      <td>abc</td>
      <td></td>
    </tr>
    <tr>
      <th>13</th>
      <td>F003</td>
      <td>abc</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>



## 2. 出力


```python
# tblを作成する
tbl = create_tbl()

# tblを穴埋めしdfへ返す
df = fillnan_mst(tbl, fmst, emst)

df

# # 期待する結果の更新用df状態です
# 	lcd	product	price
# 0	  E001	abc	100
# 1	  E001	abc	1
# 2	  E001	abc	1
# 3	  E002	abc	99
# 4	  E002	abc	99
# 5	  E003	abc	99
# 6	  E003	abc	99
# 7	  F001	abc	200
# 8	  F001	abc	2
# 9	  F001	abc	2
# 10	F002	abc	99
# 11	F002	abc	99
# 12	F003	abc	99
# 13	F003	abc	99
```
