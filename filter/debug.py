import sys
import csv
import argparse
from init.config import config

def filter_debug(data, not_flag):
    debug_prefix = config.get_constant('debug_prefix')
    output = [data[0]]
    for row in data[1:]:
        chat = row[data[0].index('chat')]
        if not_flag:
            if not chat.startswith(debug_prefix):
                output.append(row)
        else:
            if chat.startswith(debug_prefix):
                output.append(row)
    return output

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Filter debug messages from CSV data')
    parser.add_argument('-n', '--not-flag', action='store_true', help='Negate the filter')
    args = parser.parse_args()
    
    reader = csv.reader(sys.stdin)
    data = list(reader)
    filtered_data = filter_debug(data, args.not_flag)
    writer = csv.writer(sys.stdout)
    writer.writerows(filtered_data)
