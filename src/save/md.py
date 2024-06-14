import sys

def save_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"Content has been saved to {file_path}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python save_md.py <output_file_path>")
        sys.exit(1)

    output_file_path = sys.argv[1]

    # Read content from standard input
    content = sys.stdin.read()

    # Save content to the specified file
    save_to_file(output_file_path, content)

if __name__ == "__main__":
    main()