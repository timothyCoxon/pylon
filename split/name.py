import sys
import csv
import re

def split_names(data):
    # Check if the 'chat' column exists
    if 'chat' in data[0]:
        # Get the index of the 'chat' column
        chat_idx = data[0].index('chat')
        header = data[0] + ['name']
        output = [header]

        name_pattern = re.compile(r'^(.*?):')
        for row in data[1:]:
            chat = row[chat_idx]
            match = name_pattern.match(chat)
            if match:
                name = match.group(1)
                new_chat = chat[len(name)+2:]  # +2 to remove ': '
                new_row = row + [name]
                new_row[chat_idx] = new_chat
                output.append(new_row)
            else:
                output.append(row + [''])
    else:
        # If 'chat' column doesn't exist, just pass through the data
        output = data
    return output

if __name__ == "__main__":
    reader = csv.reader(sys.stdin)
    data = list(reader)
    split_data = split_names(data)
    writer = csv.writer(sys.stdout)
    writer.writerows(split_data)