# name: term
# purpose: Filter out any row based on term
# complete: No
# task: 
# idea: 
# test: Need Tests
import sys
import csv
import argparse

def filter_term(data, term, not_flag):
    output = [data[0]]
    for row in data[1:]:
        chat = row[data[0].index('chat')]
        if not_flag:
            if term not in chat:
                output.append(row)
        else:
            if term in chat:
                output.append(row)
    return output

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Filter messages containing a term from CSV data')
    parser.add_argument('term', help='Term to filter by')
    parser.add_argument('-n', '--not-flag', action='store_true', help='Negate the filter')
    args = parser.parse_args()
    
    reader = csv.reader(sys.stdin)
    data = list(reader)
    filtered_data = filter_term(data, args.term, args.not_flag)
    writer = csv.writer(sys.stdout)
    writer.writerows(filtered_data)
