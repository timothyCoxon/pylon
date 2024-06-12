# name: unique
# purpose: Remove all but one of rows that are the same, if headers are given only work by those columns.
# complete: No
# task: 
# idea: 
# test: Need Tests
import sys
import csv
import argparse

def unique(data, headers=None):
    if headers:
        # Get the indices of the specified headers
        header_indices = [data[0].index(header) for header in headers]
        seen = set()
        unique_data = [data[0]]  # Keep the header
        for row in data[1:]:
            row_key = tuple(row[index] for index in header_indices)
            if row_key not in seen:
                seen.add(row_key)
                unique_data.append(row)
    else:
        seen = set()
        unique_data = [data[0]]  # Keep the header
        for row in data[1:]:
            row_tuple = tuple(row)
            if row_tuple not in seen:
                seen.add(row_tuple)
                unique_data.append(row)
    return unique_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Remove duplicate rows from CSV data')
    parser.add_argument('headers', nargs='*', help='List of headers to determine uniqueness (optional)')
    args = parser.parse_args()
    
    reader = csv.reader(sys.stdin)
    data = list(reader)
    
    if args.headers:
        unique_data = unique(data, args.headers)
    else:
        unique_data = unique(data)
    
    writer = csv.writer(sys.stdout)
    writer.writerows(unique_data)
