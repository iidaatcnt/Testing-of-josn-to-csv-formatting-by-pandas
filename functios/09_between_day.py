import pandas as pd
import datetime

df = pd.DataFrame(
    [
        {"cd": "a01", "fire": "2018-11-05", "start": "2018-10-10", "end": "2018-10-30", "add": 10},
        {"cd": "a02", "fire": "2018-11-15", "start": "2018-10-10", "end": "2018-10-30", "add": 10},
        {"cd": "a03", "fire": "2018-11-05", "start": "2018-10-10", "end": "2018-10-30", "add": 10},
        {"cd": "a04", "fire": "2018-11-15", "start": "2018-10-10", "end": "2018-10-30", "add": 10},
        {"cd": "a05", "fire": "2018-11-05", "start": "2018-10-10", "end": "2018-10-30", "add": 10}
    ], columns=["cd", "fire", "start", "end", "add"]
)

# "cd" "fire"  "start"  "end"  "add" "chk"
# a01 2018-11-05 2018-10-10 2018-10-30 10 True    -> 2018-10-10 2018-11-10 : 2018-11-05
# a02 2018-11-15 2018-10-10 2018-10-30 10 False   -> 2018-10-10 2018-11-10 : 2018-11-15
# a03 2018-11-05 2018-10-10 2018-10-30 10 True    -> 2018-10-10 2018-11-10 : 2018-11-05
# a04 2018-11-15 2018-10-10 2018-10-30 10 False   -> 2018-10-10 2018-11-10 : 2018-11-15
# a05 2018-11-05 2018-10-10 2018-10-30 10 True    -> 2018-10-10 2018-11-10 : 2018-11-05


# str -> datetime
df['fire'] = pd.to_datetime(df['fire'])
df['start'] = pd.to_datetime(df['start'])
df['end'] = pd.to_datetime(df['end'])

# betwenn start and end
df_sel = df[(df['end'] >= df['fire']) & (df['start'] < df['fire'])]
print(df_sel)
print('-'*20)

# TODO
# locじゃないとだめかも。

# TODO
# end = end + add