import sys
import csv
import re
from init.config import config, update_seen_names

def extract_on_region(data):
    on_region_pattern = re.compile(r'\b(entered the region|left the region)\b')
    output = [data[0] + ['region_status']]
    for row in data[1:]:
        chat = row[data[0].index('chat')]
        if on_region_pattern.search(chat):
            name_match = re.match(r'\[(\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2})\] (.*?):', chat)
            if name_match:
                name = name_match.group(2)
                config.update_seen_names(name)
            output.append(row + [chat])
    return output

if __name__ == "__main__":
    reader = csv.reader(sys.stdin)
    data = list(reader)
    on_region_data = extract_on_region(data)
    writer = csv.writer(sys.stdout)
    writer.writerows(on_region_data)
