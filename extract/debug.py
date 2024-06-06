import sys
import csv
from init.config import config

def extract_debug(data):
    debug_prefix = config.get_constant('debug_prefix')
    output = [data[0]]
    for row in data[1:]:
        chat = row[data[0].index('chat')]
        if chat.startswith(debug_prefix):
            output.append(row)
    return output

if __name__ == "__main__":
    reader = csv.reader(sys.stdin)
    data = list(reader)
    debug_data = extract_debug(data)
    writer = csv.writer(sys.stdout)
    writer.writerows(debug_data)
