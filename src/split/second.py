# name: second
# purpose: Split out the seond value of the timestamp to it's own row
# complete: No
# task: 
# idea: 
# test: Need Tests
import sys
import csv
import re

def split_second(data):
    if 'time' in data[0]:
        time_idx = data[0].index('time')
        header = data[0] + ['second']
        output = [header]
        for row in data[1:]:
            time = row[time_idx]
            second = time.split(':')[2]
            output.append(row + [second])
    else:
        output = data
    return output

if __name__ == "__main__":
    reader = csv.reader(sys.stdin)
    data = list(reader)
    split_data = split_second(data)
    writer = csv.writer(sys.stdout)
    writer.writerows(split_data)
