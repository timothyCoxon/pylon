# name: url
# purpose: Extract all URL found
# complete: No
# task: 
# idea: 
# test: Need Tests
import sys
import csv
import re

def extract_url(data):
    url_pattern = re.compile(r'https?://[^\s]+')
    output = [data[0] + ['url']]
    for row in data[1:]:
        chat = row[data[0].index('chat')]
        urls = url_pattern.findall(chat)
        if urls:
            for url in urls:
                output.append(row + [url])
    return output

if __name__ == "__main__":
    reader = csv.reader(sys.stdin)
    data = list(reader)
    url_data = extract_url(data)
    writer = csv.writer(sys.stdout)
    writer.writerows(url_data)
