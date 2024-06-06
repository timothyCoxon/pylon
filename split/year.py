import sys
import csv
import re

def split_year(data):
    if 'date' in data[0]:
        date_idx = data[0].index('date')
        header = data[0] + ['year']
        output = [header]
        for row in data[1:]:
            date = row[date_idx]
            year = date.split('-')[0]
            output.append(row + [year])
    else:
        output = data
    return output

if __name__ == "__main__":
    reader = csv.reader(sys.stdin)
    data = list(reader)
    split_data = split_year(data)
    writer = csv.writer(sys.stdout)
    writer.writerows(split_data)
