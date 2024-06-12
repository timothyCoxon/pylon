# name: generate_overview
# purpose: Script to generate a csv containing all header comment and frontmatter
# complete: No
# task: Need moving to ~/pylon/dev/
# idea: 
# test: Need Tests

import os
import csv
import pathspec

def load_gitignore(directory):
    gitignore_path = os.path.join(directory, '.gitignore')
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as file:
            patterns = file.read().splitlines()
        return pathspec.PathSpec.from_lines('gitwildmatch', patterns)
    return None

def extract_metadata(file_path):
    metadata = {
        'parent': os.path.dirname(file_path),
        'file/folder name': os.path.basename(file_path),
        'purpose': '',
        'tasks': '',
        'tests': '',
        'ideas': '',
        'complete': ''
    }
    if file_path.endswith('.py') or file_path.endswith('.md'):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith('#') or line.startswith('---'):
                    key_value = line.strip('#- \n').split(':', 1)
                    if len(key_value) == 2:
                        key, value = key_value
                        key = key.strip().lower()
                        value = value.strip()
                        if key in metadata:
                            metadata[key] = value
    return metadata

def generate_csv(directory):
    gitignore = load_gitignore(directory)
    csv_file = os.path.join(directory, 'project_overview.csv')
    with open(csv_file, 'w', newline='') as csvfile:
        fieldnames = ['parent', 'file/folder name', 'purpose', 'tasks', 'tests', 'ideas', 'complete']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                if gitignore and gitignore.match_file(file_path):
                    continue
                metadata = extract_metadata(file_path)
                writer.writerow(metadata)

if __name__ == "__main__":
    generate_csv('/home/timothy/pylon')