# name: names
# purpose: Extract all the names from the data
# complete: No
# task: Need Display Name and Username Versions
# idea: 
# test: Need Tests
import sys
import re
from init.config import update_seen_names

def extract_names(lines):
    name_pattern = re.compile(r'\[(\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2})\] (.*?):')
    name_map = {}
    for line in lines:
        match = name_pattern.match(line)
        if match:
            timestamp = match.group(1)
            name = match.group(2)
            if '(' in name:
                display_name, user_name = name.split('(')
                display_name = display_name.strip()
                user_name = user_name.strip(')').strip()
                if '.' in user_name:
                    first_name, last_name = user_name.split('.')
                else:
                    first_name = user_name
                    last_name = "Resident"
            else:
                display_name = name
                first_name = name
                last_name = "Resident"
            name_map[name] = (display_name, first_name, last_name)
    return name_map

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    names = extract_names(lines)
    for name, (display_name, first_name, last_name) in names.items():
        name_match = re.match(r'\[(\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2})\] (.*?):', name)
        if name_match:
            name = name_match.group(2)
            update_seen_names(name)
        print(f"{display_name},{first_name},{last_name}")