import sys

def prepare_timestamps(parsed_lines):
    new_lines = []
    for line in parsed_lines:
        date, time, text = line.split(' ', 2)
        if date and time:
            formatted_date = date.replace('/', '-')
            new_line = f"([[_3._Time\\{formatted_date}\\{date}.md]] {time}) {text}"
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    return new_lines

if __name__ == "__main__":
    parsed_lines = sys.stdin.readlines()
    prepared_lines = prepare_timestamps(parsed_lines)
    for line in prepared_lines:
        print(line)