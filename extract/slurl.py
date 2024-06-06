import sys
import csv
import re

def extract_slurl(data):
    slurl_pattern = re.compile(r'http://maps.secondlife.com/secondlife/[^\s]+')
    output = [data[0] + ['slurl']]
    for row in data[1:]:
        chat = row[data[0].index('chat')]
        slurls = slurl_pattern.findall(chat)
        if slurls:
            for slurl in slurls:
                output.append(row + [slurl])
    return output

if __name__ == "__main__":
    reader = csv.reader(sys.stdin)
    data = list(reader)
    slurl_data = extract_slurl(data)
    writer = csv.writer(sys.stdout)
    writer.writerows(slurl_data)
