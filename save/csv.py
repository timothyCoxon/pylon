import sys
import csv
import argparse
from pathlib import Path
from init.config import config

def save_csv(data, filepath, mode):
    with open(filepath, mode, newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Save CSV data')
    parser.add_argument('mode', choices=['overwrite', 'append', 'update'], help='Mode to save the data')
    parser.add_argument('filepath', type=str, help='Filepath to save the data')
    args = parser.parse_args()
    
    reader = csv.reader(sys.stdin)
    data = list(reader)

    if args.mode == 'overwrite':
        save_csv(data, args.filepath, 'w')
    elif args.mode == 'append':
        save_csv(data, args.filepath, 'a')
    elif args.mode == 'update':
        existing_data = []
        if Path(args.filepath).exists():
            with open(args.filepath, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                existing_data = list(reader)
        updated_data = {tuple(row) for row in existing_data}.union({tuple(row) for row in data})
        save_csv([list(row) for row in updated_data], args.filepath, 'w')
