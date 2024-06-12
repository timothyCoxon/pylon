# name: generate_metadata_csv
# purpose: Script to run throught the project to gather the current header data
# complete: No
# task: Need moving to ~/pylon/dev/
# idea: Is this technically needed? isn't it the same as generate_overview.py?
# test: Need Tests
import os
import csv
import pathspec

def load_gitignore_patterns(directory):
    gitignore_path = os.path.join(directory, '.gitignore')
    if not os.path.exists(gitignore_path):
        return None
    with open(gitignore_path, 'r') as file:
        patterns = file.read().splitlines()
    return pathspec.PathSpec.from_lines('gitwildmatch', patterns)

def is_ignored(path, spec):
    if spec is None:
        return False
    return spec.match_file(path)

def extract_metadata_from_python(file_path):
    metadata = {
        'path': file_path,
        'name': '',
        'desc': '',
        'complete': '',
        'tasks': [],
        'ideas': [],
        'tests': []
    }
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('# name:'):
                metadata['name'] = line.split(':', 1)[1].strip()
            elif line.startswith('# purpose:'):
                metadata['desc'] = line.split(':', 1)[1].strip()
            elif line.startswith('# complete:'):
                metadata['complete'] = line.split(':', 1)[1].strip()
            elif line.startswith('# task:'):
                metadata['tasks'].append(line.split(':', 1)[1].strip())
            elif line.startswith('# idea:'):
                metadata['ideas'].append(line.split(':', 1)[1].strip())
            elif line.startswith('# test:'):
                metadata['tests'].append(line.split(':', 1)[1].strip())
    return metadata

def extract_metadata_from_markdown(file_path):
    metadata = {
        'path': file_path,
        'name': '',
        'desc': '',
        'complete': '',
        'tasks': [],
        'ideas': [],
        'tests': []
    }
    with open(file_path, 'r') as file:
        in_front_matter = False
        for line in file:
            if line.strip() == '---':
                in_front_matter = not in_front_matter
                continue
            if in_front_matter:
                if line.startswith('name:'):
                    metadata['name'] = line.split(':', 1)[1].strip()
                elif line.startswith('desc:'):
                    metadata['desc'] = line.split(':', 1)[1].strip()
                elif line.startswith('complete:'):
                    metadata['complete'] = line.split(':', 1)[1].strip()
                elif line.startswith('task:'):
                    metadata['tasks'].append(line.split(':', 1)[1].strip())
                elif line.startswith('idea:'):
                    metadata['ideas'].append(line.split(':', 1)[1].strip())
                elif line.startswith('test:'):
                    metadata['tests'].append(line.split(':', 1)[1].strip())
    return metadata

def generate_csv(directory, output_csv):
    fieldnames = ['path', 'name', 'desc', 'complete', 'tasks', 'ideas', 'tests']
    gitignore_spec = load_gitignore_patterns(directory)
    
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                if is_ignored(file_path, gitignore_spec):
                    continue
                if file.endswith('.py'):
                    metadata = extract_metadata_from_python(file_path)
                elif file.endswith('.md'):
                    metadata = extract_metadata_from_markdown(file_path)
                else:
                    continue
                metadata['tasks'] = '; '.join(metadata['tasks'])
                metadata['ideas'] = '; '.join(metadata['ideas'])
                metadata['tests'] = '; '.join(metadata['tests'])
                writer.writerow(metadata)

if __name__ == "__main__":
    project_directory = '/home/timothy/pylon'  # Replace with your project directory
    output_csv_file = 'metadata_summary.csv'
    generate_csv(project_directory, output_csv_file)
    print(f"Metadata summary has been written to {output_csv_file}")