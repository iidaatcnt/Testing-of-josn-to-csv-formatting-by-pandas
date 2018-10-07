import pandas as pd

# factory_tblを作成
records = [
    {"cd": "E001", "val": 100},
    {"cd": "E001", "val": ''},
    {"cd": "E001", "val": None},
    {"cd": "E002", "val": 100},
    {"cd": "E002", "val": ''},
    {"cd": "E002", "val": None},
    {"cd": "F001", "val": 100},
    {"cd": "F001", "val": ''},
    {"cd": "F001", "val": None},
    {"cd": "F002", "val": 100},
    {"cd": "F002", "val": ''},
    {"cd": "F002", "val": None}
]
cols = ["cd", "val"]


def create_tbl(records, cols):
    tbl = pd.DataFrame(records, columns=cols)
    tbl = tbl.replace({'': None})
    return tbl


tbl = create_tbl(records, cols)

print(tbl)
