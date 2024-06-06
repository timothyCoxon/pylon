import sys
import csv
import re
from init.config import config, update_seen_names

def read_chatlog(lines):
    header = ['chat']
    output = [header]
    name_pattern = re.compile(r'\[(\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2})\] (.*?):')
    for line in lines:
        output.append([line.strip()])
        match = name_pattern.match(line.strip())
        if match:
            name = match.group(2)
            config.update_seen_names(name)
    return output

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    chatlog = read_chatlog(lines)
    writer = csv.writer(sys.stdout)
    writer.writerows(chatlog)
