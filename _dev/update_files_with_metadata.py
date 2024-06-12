import csv
import os

def update_python_file(file_path, metadata):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    lines = []
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove existing metadata comments
    lines = [line for line in lines if not line.startswith('# name:') and not line.startswith('# purpose:') and not line.startswith('# complete:') and not line.startswith('# task:') and not line.startswith('# idea:') and not line.startswith('# test:')]

    # Add new metadata comments
    lines.insert(0, f"# test: {metadata['tests']}\n")
    lines.insert(0, f"# idea: {metadata['ideas']}\n")
    lines.insert(0, f"# task: {metadata['tasks']}\n")
    lines.insert(0, f"# complete: {metadata['complete']}\n")
    lines.insert(0, f"# purpose: {metadata['desc']}\n")
    lines.insert(0, f"# name: {metadata['name']}\n")

    with open(file_path, 'w') as file:
        file.writelines(lines)

def update_markdown_file(file_path, metadata):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    lines = []
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove existing front matter
    if lines[0].strip() == '---':
        end_index = 1
        while end_index < len(lines) and lines[end_index].strip() != '---':
            end_index += 1
        lines = lines[end_index + 1:]

    # Add new front matter
    front_matter = [
        '---\n',
        f'name: {metadata["name"]}\n',
        f'desc: {metadata["desc"]}\n',
        f'complete: {metadata["complete"]}\n',
        f'tasks: {metadata["tasks"]}\n',
        f'ideas: {metadata["ideas"]}\n',
        f'tests: {metadata["tests"]}\n',
        '---\n'
    ]
    lines = front_matter + lines

    with open(file_path, 'w') as file:
        file.writelines(lines)

def update_files_from_csv(csv_path):
    with open(csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            file_path = row['path']
            metadata = {
                'name': row['name'],
                'desc': row['desc'],
                'complete': row['complete'],
                'tasks': row['tasks'],
                'ideas': row['ideas'],
                'tests': row['tests']
            }
            if file_path.endswith('.py'):
                update_python_file(file_path, metadata)
            elif file_path.endswith('.md'):
                update_markdown_file(file_path, metadata)

if __name__ == "__main__":
    csv_path = 'Pylon-Sorting.csv'  # Replace with the path to your CSV file
    update_files_from_csv(csv_path)
    print(f"Files have been updated with metadata from {csv_path}")