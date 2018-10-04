

```python
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
      <th>Pos</th>
      <th>regular</th>
      <th>Reserve</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>QB</td>
      <td>12</td>
      <td>[9, 8]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>CB</td>
      <td>28</td>
      <td>[37, 23, 38, 20]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>WR</td>
      <td>19</td>
      <td>[83, 82, 81, 17, 18]</td>
    </tr>
    <tr>
      <th>3</th>
      <td>T</td>
      <td>69</td>
      <td>[75, 78]</td>
    </tr>
    <tr>
      <th>4</th>
      <td>S</td>
      <td>36</td>
      <td>[35, 21, 29, 27]</td>
    </tr>
    <tr>
      <th>5</th>
      <td>RB</td>
      <td>22</td>
      <td>[33, 88, 30]</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
      <th>Pos</th>
      <th>regular</th>
      <th>Reserve</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>QB</td>
      <td>12</td>
      <td>[9]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>QB</td>
      <td>12</td>
      <td>[8]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>CB</td>
      <td>28</td>
      <td>[37]</td>
    </tr>
    <tr>
      <th>3</th>
      <td>CB</td>
      <td>28</td>
      <td>[23]</td>
    </tr>
    <tr>
      <th>4</th>
      <td>CB</td>
      <td>28</td>
      <td>[38]</td>
    </tr>
    <tr>
      <th>5</th>
      <td>CB</td>
      <td>28</td>
      <td>[20]</td>
    </tr>
    <tr>
      <th>6</th>
      <td>WR</td>
      <td>19</td>
      <td>[83]</td>
    </tr>
    <tr>
      <th>7</th>
      <td>WR</td>
      <td>19</td>
      <td>[82]</td>
    </tr>
    <tr>
      <th>8</th>
      <td>WR</td>
      <td>19</td>
      <td>[81]</td>
    </tr>
    <tr>
      <th>9</th>
      <td>WR</td>
      <td>19</td>
      <td>[17]</td>
    </tr>
    <tr>
      <th>10</th>
      <td>T</td>
      <td>69</td>
      <td>[75]</td>
    </tr>
    <tr>
      <th>11</th>
      <td>T</td>
      <td>69</td>
      <td>[78]</td>
    </tr>
    <tr>
      <th>12</th>
      <td>S</td>
      <td>36</td>
      <td>[35]</td>
    </tr>
    <tr>
      <th>13</th>
      <td>S</td>
      <td>36</td>
      <td>[21]</td>
    </tr>
    <tr>
      <th>14</th>
      <td>S</td>
      <td>36</td>
      <td>[29]</td>
    </tr>
    <tr>
      <th>15</th>
      <td>S</td>
      <td>36</td>
      <td>[27]</td>
    </tr>
    <tr>
      <th>16</th>
      <td>RB</td>
      <td>22</td>
      <td>[33]</td>
    </tr>
    <tr>
      <th>17</th>
      <td>RB</td>
      <td>22</td>
      <td>[88]</td>
    </tr>
    <tr>
      <th>18</th>
      <td>RB</td>
      <td>22</td>
      <td>[30]</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
        


```
