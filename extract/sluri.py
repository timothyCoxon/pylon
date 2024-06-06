import sys
import csv
import re

def extract_sluri(data):
    sluri_pattern = re.compile(r'secondlife://[^\s]+')
    output = [data[0] + ['sluri']]
    for row in data[1:]:
        chat = row[data[0].index('chat')]
        sluris = sluri_pattern.findall(chat)
        if sluris:
            for sluri in sluris:
                output.append(row + [sluri])
    return output

if __name__ == "__main__":
    reader = csv.reader(sys.stdin)
    data = list(reader)
    sluri_data = extract_sluri(data)
    writer = csv.writer(sys.stdout)
    writer.writerows(sluri_data)
