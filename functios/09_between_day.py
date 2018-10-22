import pandas as pd
import datetime

df = pd.DataFrame(
    [
        {"cd": "a01", "fire": "2018-11-05", "start": "2018-11-01", "end": "2018-11-10", "add": 10},
        {"cd": "a02", "fire": "2018-11-15", "start": "2018-11-01", "end": "2018-11-10", "add": 10},
        {"cd": "a03", "fire": "2018-11-25", "start": "2018-11-01", "end": "2018-11-10", "add": 10},
        {"cd": "a04", "fire": "2018-12-05", "start": "2018-11-01", "end": "2018-11-10", "add": 10},
        {"cd": "a05", "fire": "2018-12-15", "start": "2018-11-01", "end": "2018-11-10", "add": 10}
    ], columns=["cd", "fire", "start", "end", "add"]
)

# "cd" "fire"  "start"  "end"  "add" "chk"
# a01 2018-11-05 2018-11-01 2018-11-10 10 True   -> 2018-11-05 : 2018-11-01 2018-11-20
# a02 2018-11-15 2018-11-01 2018-11-10 10 True   -> 2018-11-15 : 2018-11-01 2018-11-20
# a03 2018-11-25 2018-11-01 2018-11-10 10 False  -> 2018-11-25 : 2018-11-01 2018-11-20
# a04 2018-12-05 2018-11-01 2018-11-10 10 False  -> 2018-12-05 : 2018-11-01 2018-11-20
# a05 2018-12-15 2018-11-01 2018-11-10 10 False  -> 2018-12-15 : 2018-11-01 2018-11-20


# str -> datetime
df['fire'] = pd.to_datetime(df['fire'])
df['start'] = pd.to_datetime(df['start'])
df['end'] = pd.to_datetime(df['end'])
# df['res'] = False

# betwenn start and end
df_sel = df[(df['start'] <= df['fire']) & (df['end'] >= df['fire'])]
print(df_sel)

# TODO
# end = end + add