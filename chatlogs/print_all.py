import sys

def print_all(lines):
    for line in lines:
        print(line)

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    print_all(lines)