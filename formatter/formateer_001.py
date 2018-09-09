import csv
# import time
import json
# import string

def write_csv_format():
      header = ["MLS",
              "Location",
              "Price",
              "Bedrooms",
              "Bathrooms",
              "Size",
              "Price/SQ.Ft",
              "Status"]
    # Get output as csv file
    # with open('out.csv', 'w') as file_out:
    #     wrt = csv.writer(file_out)
    #     wrt.writerow(header)

def write_to_file():
    with open('test.txt', 'w') as f:
        f.write('hello world\n')
        print('What', 'a', 'funy', 'day', '!', file=f)

def export_to_csv_format():
    header = ["Player",
              "Hash",
              "Pos",
              "HT",
              "WT",
              "Age",
              "Exp",
              "College"]
    with open('output001.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)
        csvwriter.writerow(['Mason Crosby', 2, 'K', '6-1', '207', 34, 12, 'Colorado'])

if __name__ == '__main__':
    export_to_csv_format()

