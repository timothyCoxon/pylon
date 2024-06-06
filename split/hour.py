import sys
import csv
import re

def split_hour(data):
    if 'time' in data[0]:
        time_idx = data[0].index('time')
        header = data[0] + ['hour']
        output = [header]
        for row in data[1:]:
            time = row[time_idx]
            hour = time.split(':')[0]
            output.append(row + [hour])
    else:
        output = data
    return output

if __name__ == "__main__":
    reader = csv.reader(sys.stdin)
    data = list(reader)
    split_data = split_hour(data)
    writer = csv.writer(sys.stdout)
    writer.writerows(split_data)
