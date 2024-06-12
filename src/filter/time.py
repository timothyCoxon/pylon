# name: time
# purpose: Filter out any row based on cron style time options
# complete: No
# task: 
# idea: 
# test: Need Tests
import sys
import csv
import argparse

def filter_time(data, start_time, end_time, not_flag):
    output = [data[0]]
    for row in data[1:]:
        time = row[data[0].index('time')]
        if start_time <= time <= end_time:
            if not not_flag:
                output.append(row)
        else:
            if not_flag:
                output.append(row)
    return output

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Filter messages by time range from CSV data')
    parser.add_argument('start_time', help='Start time of the range (HH:MM:SS)')
    parser.add_argument('end_time', help='End time of the range (HH:MM:SS)')
    parser.add_argument('-n', '--not', action='store_true', help='Negate the filter')
    args = parser.parse_args()
    
    reader = csv.reader(sys.stdin)
    data = list(reader)
    filtered_data = filter_time(data, args.start_time, args.end_time, args.not_flag)
    writer = csv.writer(sys.stdout)
    writer.writerows(filtered_data)
