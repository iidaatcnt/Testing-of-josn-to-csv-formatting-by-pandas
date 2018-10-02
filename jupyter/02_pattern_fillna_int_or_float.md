

```python
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
      <th>hash</th>
      <th>age</th>
      <th>wt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10</td>
      <td>28</td>
      <td>56.1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>30</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>3</th>
      <td>40</td>
      <td>NaN</td>
      <td>100</td>
    </tr>
  </tbody>
</table>
</div>




```python
dfm['wt'].map(type)

```




    0       <class 'float'>
    1    <class 'NoneType'>
    2         <class 'str'>
    3         <class 'int'>
    Name: wt, dtype: object




```python
# 空文字はNone扱い
dfm = dfm.replace('', None)
dfm

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
      <th>hash</th>
      <th>age</th>
      <th>wt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10</td>
      <td>28</td>
      <td>56.1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>30</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>40</td>
      <td>NaN</td>
      <td>100</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 欠損箇所を埋める既定値には列ごとにある。データはintとflortの場合がある
# これはダメなケース
AGE_DEFAULT = 99
WT_DEFAULT = 99.9

dfm = dfm.fillna(99)

dfm
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
      <th>hash</th>
      <th>age</th>
      <th>wt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10</td>
      <td>28</td>
      <td>56.1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20</td>
      <td>99</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>30</td>
      <td>99</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>40</td>
      <td>99</td>
      <td>100.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 仕様検討中
# 　既定値の値もデータ型もそのまま変えずに穴埋めをしたい。
# 　穴埋めの既定値を基本的にint型として、float型で穴埋めしたい列名はリストにして引数で指定する
#　列内のNoneのところだけに穴埋め処理し、他は影響しないようにしたい

```
