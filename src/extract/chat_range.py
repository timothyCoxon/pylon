# name: chat_range
# purpose: Extract all instances of  chat range messages
# complete: No
# task: 
# idea: 
# test: Need Tests
import sys
import csv
import re
from init.config import config, update_seen_names

def extract_chat_range(data):
    chat_range_pattern = re.compile(r'\b(entered chat range|left chat range)\b')
    output = [data[0] + ['chat_range']]
    for row in data[1:]:
        chat = row[data[0].index('chat')]
        if chat_range_pattern.search(chat):
            name_match = re.match(r'\[(\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2})\] (.*?):', chat)
            if name_match:
                name = name_match.group(2)
                config.update_seen_names(name)
            output.append(row + [chat])
    return output

if __name__ == "__main__":
    reader = csv.reader(sys.stdin)
    data = list(reader)
    chat_range_data = extract_chat_range(data)
    writer = csv.writer(sys.stdout)
    writer.writerows(chat_range_data)
