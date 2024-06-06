import sys
import csv
import re

def split_day(data):
    if 'date' in data[0]:
        date_idx = data[0].index('date')
        header = data[0] + ['day']
        output = [header]
        for row in data[1:]:
            date = row[date_idx]
            day = date.split('-')[2]
            output.append(row + [day])
    else:
        output = data
    return output

if __name__ == "__main__":
    reader = csv.reader(sys.stdin)
    data = list(reader)
    split_data = split_day(data)
    writer = csv.writer(sys.stdout)
    writer.writerows(split_data)
