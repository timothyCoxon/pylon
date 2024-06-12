# name: name
# purpose: Filter out any row based on name
# complete: No
# task: 
# idea: 
# test: Need Tests
import sys
import csv
import argparse

def filter_name(data, name_file, not_flag):
    with open(name_file, 'r') as file:
        names = [line.strip() for line in file]
    
    output = [data[0]]
    for row in data[1:]:
        chat = row[data[0].index('chat')]
        if any(name in chat for name in names):
            if not not_flag:
                output.append(row)
        else:
            if not_flag:
                output.append(row)
    return output

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Filter messages containing names from a CSV file')
    parser.add_argument('name_file', help='CSV file with names to filter by')
    parser.add_argument('-n', '--not-flag', action='store_true', help='Negate the filter')
    args = parser.parse_args()
    
    reader = csv.reader(sys.stdin)
    data = list(reader)
    filtered_data = filter_name(data, args.name_file, args.not_flag)
    writer = csv.writer(sys.stdout)
    writer.writerows(filtered_data)
