import pandas as pd
import csv
import json

class Getqb:

    def __init__(self):
        pass

    def read_from_json(self):
        df = pd.read_json('input/sample.json')
        # s = '{"col1":{"row1":1,"row2":2,"row3":3},"col2":{"row1":"a","row2":"x","row3":"\u3042"}}'
        # df = pd.read_json(s)
        print(df)

    def export_to_csv_format(self):
        header = ["Player",
                  "Hash",
                  "Pos",
                  "HT",
                  "WT",
                  "Age",
                  "Exp",
                  "College"]
        with open('output/output001.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(header)
            csvwriter.writerow(['Mason Crosby', 2, 'K', '6-1', '207', 34, 12, 'Colorado'])

    def write_to_csv(self):
        # df = pd.DataFrame([
        #     ["0001", "John", "Engineer"],
        #     ["0002", "Lily", "Sales"]],
        #     columns=['id', 'name', 'job'])
        df = pd.read_json('input/sample2.json')

        # CSV ファイル (employee.csv) として出力
        df.to_csv("output/output.csv", index=False)

getqb = Getqb()
# getqb.read_from_json()
getqb.write_to_csv()

# if __name__ == '__main__':
#     read_to_json()

