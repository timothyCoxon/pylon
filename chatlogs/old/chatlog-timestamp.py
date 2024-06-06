# Open the file containing the timestamps
with open('timestamps.txt', 'r') as file:
    lines = file.readlines()

# Process each line to change the timestamp format
new_lines = []
for line in lines:
    # Splitting the timestamp from the rest of the line if necessary
    parts = line.strip().split(' ')
    timestamp = parts[0]
    # Extracting date and time from the timestamp
    date, time = timestamp[1:-1].split(' ')
    # Reformatting the timestamp
    new_timestamp = f"[{date}] ({time})"
    # Reconstructing the line if there was more content beyond the timestamp
    new_line = ' '.join([new_timestamp] + parts[1:])
    new_lines.append(new_line)

# Write the modified lines back to a new file or overwrite the old one
with open('modified_timestamps.txt', 'w') as file:
    for line in new_lines:
        file.write(line + '\n')