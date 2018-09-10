import pandas as pd
import csv
import json

class Getqb(object):

    def __init__(self,file_name):
        self.file_name = file_name

    def read_from_json(self):
        df = pd.read_json('input/sample.json')
        print(df)

    def write_to_csv(self):
        df = pd.read_json('input/greenbay_players.json')

        # CSV ファイル (employee.csv) として出力
        df.to_csv("output/output.csv", index=False)

        return self.file_name


