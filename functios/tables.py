import pandas as pd
import numpy as np

tbl = [
        {"cd":"f001","val":None},
        {"cd":"f002","val":100},
        {"cd":"e001","val":None},
        {"cd":"e001","val":200},
        {"cd":"x001","val":None},
        ]
mst1 = [
        {"cd":"f001","val":1},
        {"cd":"e001","val":2}
        ]
mst2 = [
        {"cd":"f001","val":3},
        {"cd":"e001","val":4}
        ]
tbl  = pd.DataFrame(tbl)
mst1 = pd.DataFrame(mst1)
mst2 = pd.DataFrame(mst2)

print(tbl)
print(mst1)
print(mst2)

print("-" * 20)
for i in range (len(tbl)):
    if tbl.loc[i, "val"] == None:
        print('>> ',tbl.loc[i, "val"])
        if tbl.loc[i, "cd"][0] == "f":
            tbl.loc[i, "val"] = mst1[mst1["cd"] == tbl.loc[i, "cd"]]
        elif tbl.loc[i, "cd"][0] == "e":
            tbl.loc[i, "val"] = mst2[mst2["cd"] == tbl.loc[i, "cd"]]
print("-" * 20)
