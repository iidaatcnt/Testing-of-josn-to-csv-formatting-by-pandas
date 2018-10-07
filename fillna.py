import pandas as pd

# factory_tblを作成


def create_tbl(records, cols):
    tbl = pd.DataFrame(records, columns=cols)
    tbl = tbl.replace({'': None})
    return tbl


# int + str  :object
records = [
     {"lcd": "E00", "product": "item1", "price": 100},
     {"lcd": "E01", "product": "item1", "price": ''},
     {"lcd": "E02", "product": "item1", "price": ''},
     {"lcd": "F00", "product": "item1", "price": 300},
     {"lcd": "F01", "product": "item1", "price": ''},
     {"lcd": "F02", "product": "item1", "price": ''}
     ]
cols = ["lcd", "product", "price"]
tbl = create_tbl(records, cols)
print(tbl)

# int + str  :object
records = [
     {"lcd": "E00", "product": "item1", "price": ''},
     {"lcd": "E01", "product": "item1", "price": ''},
     {"lcd": "E02", "product": "item1", "price": ''},
     {"lcd": "F00", "product": "item1", "price": ''},
     {"lcd": "F01", "product": "item1", "price": ''},
     {"lcd": "F02", "product": "item1", "price": ''}
     ]
cols = ["lcd", "product", "price"]
tbl = create_tbl(records, cols)
print(tbl)

# int + str  :object
records = [
     {"lcd": "E00", "product": "item1", "price": None},
     {"lcd": "E01", "product": "item1", "price": None},
     {"lcd": "E02", "product": "item1", "price": None},
     {"lcd": "F00", "product": "item1", "price": None},
     {"lcd": "F01", "product": "item1", "price": None},
     {"lcd": "F02", "product": "item1", "price": None}
     ]
cols = ["lcd", "product", "price"]
tbl = create_tbl(records, cols)
print(tbl)
