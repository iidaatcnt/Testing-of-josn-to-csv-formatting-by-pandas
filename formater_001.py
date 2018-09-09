import pandas as pd
import csv
# import json

class Getqb:

    def __init__(self):
        pass

    def read_from_json(self):
        df = pd.read_json('input/sample.json')
        print(df)

    def write_to_csv(self):
        df = pd.read_json('input/greenbay_players.json')

        # CSV ファイル (employee.csv) として出力
        df.to_csv("output/output.csv", index=False)

getqb = Getqb()
getqb.write_to_csv()

# if __name__ == '__main__':
#     write_to_csv()

