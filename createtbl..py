import pandas as pd

cols=["lcd", "product", "price"]

df = pd.DataFrame(
    [
     {"lcd": "E00", "product": "item1", "price": 100},
     {"lcd": "E01", "product": "item1", "price": ''},
     {"lcd": "E02", "product": "item1", "price": ''},
     {"lcd": "F00", "product": "item1", "price": 300},
     {"lcd": "F01", "product": "item1", "price": ''},
     {"lcd": "F02", "product": "item1", "price": ''}
     ],
    columns=cols
)

print(df)