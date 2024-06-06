import sys
import csv
import re

def split_minute(data):
    if 'time' in data[0]:
        time_idx = data[0].index('time')
        header = data[0] + ['minute']
        output = [header]
        for row in data[1:]:
            time = row[time_idx]
            minute = time.split(':')[1]
            output.append(row + [minute])
    else:
        output = data
    return output

if __name__ == "__main__":
    reader = csv.reader(sys.stdin)
    data = list(reader)
    split_data = split_minute(data)
    writer = csv.writer(sys.stdout)
    writer.writerows(split_data)
