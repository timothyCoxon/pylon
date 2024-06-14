import sys
import re

def parse_input(input_text):
    # Regular expression to match the header (file path)
    header_pattern = re.compile(r'^# (.+)$')
    # Regular expression to match the script content enclosed in triple backticks
    script_pattern = re.compile(r'```(.*?)```', re.DOTALL)

    header_match = header_pattern.search(input_text)
    script_match = script_pattern.search(input_text)

    if not header_match or not script_match:
        raise ValueError("Input format is incorrect. Ensure you have a header and script content enclosed in triple backticks.")

    file_path = header_match.group(1).strip()
    script_content = script_match.group(1).strip()

    return file_path, script_content

def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"Script has been written to {file_path}")

def main():
    # Read from standard input
    input_text = sys.stdin.read()

    try:
        file_path, script_content = parse_input(input_text)
        write_to_file(file_path, script_content)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()