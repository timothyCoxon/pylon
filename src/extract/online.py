# name: online
# purpose: Extrance all instances of online status messages
# complete: No
# task: 
# idea: 
# test: Need Tests
import sys
import csv
import re
from init.config import config, update_seen_names

def extract_online(data):
    online_pattern = re.compile(r'\b(is online|is offline)\b')
    output = [data[0] + ['status']]
    for row in data[1:]:
        chat = row[data[0].index('chat')]
        if online_pattern.search(chat):
            name_match = re.match(r'\[(\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2})\] (.*?):', chat)
            if name_match:
                name = name_match.group(2)
                config.update_seen_names(name)
            output.append(row + [chat])
    return output

if __name__ == "__main__":
    reader = csv.reader(sys.stdin)
    data = list(reader)
    online_data = extract_online(data)
    writer = csv.writer(sys.stdout)
    writer.writerows(online_data)
