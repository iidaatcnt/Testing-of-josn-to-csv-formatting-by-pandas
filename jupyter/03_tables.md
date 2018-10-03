

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

emst
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
      <td>E001</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>E001</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>E001</td>
      <td>6</td>
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


