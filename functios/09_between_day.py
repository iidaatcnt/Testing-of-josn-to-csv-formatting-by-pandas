import pandas as pd
import datetime

df = pd.DataFrame(
    [
        {"cd": "a01", "fire": "2018-11-05", "start": "2018-11-01", "end": "2018-11-30", "add": 10},
        {"cd": "a02", "fire": "2018-11-15", "start": "2018-11-01", "end": "2018-11-30", "add": 10},
        {"cd": "a03", "fire": "2018-11-25", "start": "2018-11-01", "end": "2018-11-30", "add": 10},
        {"cd": "a04", "fire": "2018-12-05", "start": "2018-11-01", "end": "2018-11-30", "add": 10},
        {"cd": "a05", "fire": "2018-12-15", "start": "2018-11-01", "end": "2018-11-30", "add": 10}
    ], columns=["cd", "fire", "start", "end", "add"]
)

# 1. pd日付型にする  str -> datetime
df['fire'] = pd.to_datetime(df['fire'])
df['start'] = pd.to_datetime(df['start'])
df['end'] = pd.to_datetime(df['end'])
# df['res'] = False
print("--1--\n",df)
# --- output
#     cd       fire      start        end  add
# 0  a01 2018-11-05 2018-11-01 2018-11-30   10
# 1  a02 2018-11-15 2018-11-01 2018-11-30   10
# 2  a03 2018-11-25 2018-11-01 2018-11-30   10
# 3  a04 2018-12-05 2018-11-01 2018-11-30   10
# 4  a05 2018-12-15 2018-11-01 2018-11-30   10

# 2. end = end + add
# ここで行数は減らない、add列は不要になる
# TODO: end = end + addが出来てない。
#
# print(datetime.timedelta(days=df["add"]))
#     cd       fire      start        end
# 1  a02 2018-11-15 2018-11-01 2018-12-10
# 0  a01 2018-11-05 2018-11-01 2018-12-10
# 2  a03 2018-11-25 2018-11-01 2018-12-10
# 3  a04 2018-12-05 2018-11-01 2018-12-10
# 4  a05 2018-12-15 2018-11-01 2018-12-10

# 3. betwenn start and end
# 範囲ないの行だけ返すことできます。
# 必要なものだけ抽出するので判定値用の列は増やさないで良いです。
df_sel = df[(df['start'] <= df['fire']) & (df['end'] >= df['fire'])]
print("--3--\n",df_sel)
#  output
#     cd       fire      start        end
# 0  a01 2018-11-05 2018-11-01 2018-11-30
# 1  a02 2018-11-15 2018-11-01 2018-11-30
# 2  a03 2018-11-25 2018-11-01 2018-11-30
# 3  a04 2018-12-05 2018-11-01 2018-11-30


# df.locで処理をしようとしてますが悩み中
# import pandas.tseries.offsets as offsets
# # Try using .loc[row_indexer,col_indexer] = value instead
# df_sel['fire'] = df_sel.loc[df_sel['fire'] + offsets.Day(10)]
# print("--4--\n",df_sel)

