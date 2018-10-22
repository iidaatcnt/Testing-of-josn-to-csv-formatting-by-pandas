import pandas as pd
import datetime

df = pd.DataFrame(
    [
        {"cd": "a01", "fire": "2018-10-05", "start": "2018-10-10", "end": "2018-10-30", "add": 10},
        {"cd": "a02", "fire": "2018-10-15", "start": "2018-10-10", "end": "2018-10-30", "add": 20},
        {"cd": "a03", "fire": "2018-10-05", "start": "2018-10-10", "end": "2018-10-30", "add": 10},
        {"cd": "a04", "fire": "2018-10-15", "start": "2018-10-10", "end": "2018-10-30", "add": 20},
        {"cd": "a05", "fire": "2018-10-05", "start": "2018-10-10", "end": "2018-10-30", "add": 10}
    ], columns=["cd", "fire", "start", "end", "add"]
)

# pd.to_datetime(df['start'], format='%Y年%m月%d日')
df['fire'] = pd.to_datetime(df['fire'])
df['start'] = pd.to_datetime(df['start'])
df['end'] = pd.to_datetime(df['end'])

# df['result'] = df['end'] + df['add']
df_sel = df[(df['end'] >= df['fire']) & (df['start'] < df['fire'])]

# df_sel = df[(df['date_time'] >= START_TIME) & [(df['date_time'] < END_TIME)]

print(df_sel)

