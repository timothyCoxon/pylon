# name: date
# purpose: Filter out any row based on cron style date options
# complete: No
# task: 
# idea: 
# test: Need Tests
import sys
import csv
import argparse

def filter_date(data, start_year, end_year, months, not_flag):
    output = [data[0]]
    for row in data[1:]:
        date = row[data[0].index('date')]
        year, month, _ = map(int, date.split('-'))
        if start_year <= year <= end_year and month in months:
            if not not_flag:
                output.append(row)
        else:
            if not_flag:
                output.append(row)
    return output

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Filter messages by date range from CSV data')
    parser.add_argument('start_year', type=int, help='Start year of the date range')
    parser.add_argument('end_year', type=int, help='End year of the date range')
    parser.add_argument('months', type=str, help='Comma-separated list of months to include')
    parser.add_argument('-n', '--not-flag', action='store_true', help='Negate the filter')
    args = parser.parse_args()
    
    months = list(map(int, args.months.split(',')))
    
    reader = csv.reader(sys.stdin)
    data = list(reader)
    filtered_data = filter_date(data, args.start_year, args.end_year, months, args.not_flag)
    writer = csv.writer(sys.stdout)
    writer.writerows(filtered_data)
