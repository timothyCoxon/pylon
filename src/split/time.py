# name: time
# purpose: Split out the time value of the timestamp to it's own row
# complete: No
# task: 
# idea: 
# test: Need Tests
import sys
import csv
import re
from init.config import config

def split_time(data):
    date_format = config.get_constant('date_format')
    time_format = config.get_constant('time_format')
    # Check if the 'chat' column exists
    if 'chat' in data[0]:
        chat_idx = data[0].index('chat')
        header = data[0] + ['date', 'time']
        output = [header]

        for row in data[1:]:
            chat = row[chat_idx]
            match = re.match(rf'\(\[\[.*?\]\] ({time_format})\) (.*)', chat)
            if match:
                time = match.group(1)
                new_chat = match.group(2)
                date = re.search(r'\d{4}-\d{2}-\d{2}', chat).group(0)
                output.append(row + [date, time])
            else:
                output.append(row + ['', ''])
    else:
        output = data
    return output

if __name__ == "__main__":
    reader = csv.reader(sys.stdin)
    data = list(reader)
    split_data = split_time(data)
    writer = csv.writer(sys.stdout)
    writer.writerows(split_data)
