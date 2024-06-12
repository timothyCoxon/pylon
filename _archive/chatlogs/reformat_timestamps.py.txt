import sys

def reformat_timestamps(lines):
    new_lines = []
    for line in lines:
        parts = line.strip().split(' ', 1)
        if len(parts) > 1 and parts[0].startswith('[') and parts[0].endswith(']'):
            timestamp = parts[0]
            date, time = timestamp[1:-1].split(' ')
            new_timestamp = f"[{date}] ({time})"
            new_line = f"{new_timestamp} {parts[1]}"
            new_lines.append(new_line)
    return new_lines

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    lines = reformat_timestamps(lines)
    for line in lines:
        print(line)