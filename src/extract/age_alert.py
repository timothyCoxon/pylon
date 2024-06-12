# name: age_alert
# purpose: Extract all instances of age_alert messages
# complete: No
# task: 
# idea: 
# test: Need Tests
import sys
import csv
import re
from init.config import config, update_seen_names

# [07:42:08] bota16 triggered the age alert. Age: 0 day(s

def extract_age_alert(data):
    age_alert_pattern = re.compile(r'\b(triggered the age alert.)\b')
    output = [data[0] + ['age_alert']]
    for row in data[1:]:
        chat = row[data[0].index('chat')]
        if age_alert_pattern.search(chat):
            name_match = re.match(r'\[(\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2})\] (.*?):', chat)
            if name_match:
                name = name_match.group(2)
                config.update_seen_names(name)
            output.append(row + [chat])
    return output

if __name__ == "__main__":
    reader = csv.reader(sys.stdin)
    data = list(reader)
    age_alert_data = extract_age_alert(data)
    writer = csv.writer(sys.stdout)
    writer.writerows(age_alert_data)
