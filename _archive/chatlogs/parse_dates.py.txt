import sys
import re
from datetime import datetime

def parse_dates(lines):
    new_lines = []
    date_pattern = re.compile(r'\[(\d{4}/\d{2}/\d{2}) (\d{2}:\d{2}:\d{2})\]')
    for line in lines:
        match = date_pattern.match(line)
        if match:
            date = match.group(1)
            time = match.group(2)
            new_lines.append((date, time, line.strip()))
        else:
            new_lines.append((None, None, line.strip()))
    return new_lines

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    parsed_lines = parse_dates(lines)
    for date, time, line in parsed_lines:
        print(f"{date} {time} {line}")