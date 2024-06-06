import sys
import csv
import re
from init.config import config, update_seen_names

def extract_view_dist(data):
    view_dist_pattern = re.compile(r'\b(view distance is now)\b')
    output = [data[0] + ['view_distance']]
    for row in data[1:]:
        chat = row[data[0].index('chat')]
        if view_dist_pattern.search(chat):
            name_match = re.match(r'\[(\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2})\] (.*?):', chat)
            if name_match:
                name = name_match.group(2)
                config.update_seen_names(name)
            output.append(row + [chat])
    return output

if __name__ == "__main__":
    reader = csv.reader(sys.stdin)
    data = list(reader)
    view_dist_data = extract_view_dist(data)
    writer = csv.writer(sys.stdout)
    writer.writerows(view_dist_data)
