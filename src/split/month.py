# name: month
# purpose: Split out the month value of the timestamp to it's own row
# complete: No
# task: 
# idea: 
# test: Need Tests
import sys
import csv
import re

def split_month(data):
    if 'date' in data[0]:
        date_idx = data[0].index('date')
        header = data[0] + ['month']
        output = [header]
        for row in data[1:]:
            date = row[date_idx]
            month = date.split('-')[1]
            output.append(row + [month])
    else:
        output = data
    return output

if __name__ == "__main__":
    reader = csv.reader(sys.stdin)
    data = list(reader)
    split_data = split_month(data)
    writer = csv.writer(sys.stdout)
    writer.writerows(split_data)
