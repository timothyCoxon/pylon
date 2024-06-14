import sys
import os

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def concat_files(file_paths):
    result = []
    for file_path in file_paths:
        file_content = read_file(file_path)
        header = f"\n\n\n---\n\n> # Start of {file_path}\n\n---\n\n\n"
        footer = f"\n\n\n---\n\n> ## End of {file_path}\n\n---\n\n\n"
        result.append(header + file_content + footer)
    return ''.join(result)

def main():
    # Read file paths from standard input
    input_text = sys.stdin.read().strip()
    file_paths = input_text.splitlines()

    # Concatenate files
    concatenated_content = concat_files(file_paths)

    # Output the result to standard output
    print(concatenated_content)

if __name__ == "__main__":
    main()