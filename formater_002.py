import pandas as pd
import numpy as np

import csv
import json

class Getqb(object):

    def __init__(self,file_name):
        self.file_name = file_name

    def get_header(self):
        df = pd.read_json(self.file_name)
        print(df)
        return df[0]

    def write_to_csv(self):
        df = pd.read_json(self.file_name)
        # CSV ファイルとして出力
        # indexを出力対象から外したい場合はindex = Falseを指定。
        df.to_csv("output/output.csv", index=False)
        return self.file_name

