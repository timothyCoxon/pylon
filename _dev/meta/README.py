# name: README
# purpose: For the generation of certain aspects of the README.md file in the root directory
# complete: No
# task: [x] Need moving to ~/[pylon]/pylon/_dev/
# idea: 
# test: Need Tests

import os
import csv

def gather_metadata(project_dir):
    metadata = {
        'tasks': [],
        'ideas': [],
        'tests': []
    }
    
    for root, _, files in os.walk(project_dir):
        for file in files:
            if file.endswith('.py') or file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        if line.startswith('# task:'):
                            metadata['tasks'].append((file_path, line.split(':', 1)[1].strip()))
                        elif line.startswith('# idea:'):
                            metadata['ideas'].append((file_path, line.split(':', 1)[1].strip()))
                        elif line.startswith('# test:'):
                            metadata['tests'].append((file_path, line.split(':', 1)[1].strip()))
                        elif line.startswith('# test result:'):
                            metadata['tests'].append((file_path, line.split(':', 1)[1].strip()))
    return metadata

def generate_readme(metadata, readme_path):
    with open(readme_path, 'w') as readme:
        readme.write("# Project Overview\n\n")
        
        readme.write("## Tasks\n\n")
        readme.write("| File | Task | Status |\n")
        readme.write("|------|------|--------|\n")
        for file_path, task in metadata['tasks']:
            readme.write(f"| [{os.path.relpath(file_path)}]({os.path.relpath(file_path)}) | {task} | Pending |\n")
        
        readme.write("\n## Ideas\n\n")
        readme.write("| File | Idea | Status |\n")
        readme.write("|------|------|--------|\n")
        for file_path, idea in metadata['ideas']:
            readme.write(f"| [{os.path.relpath(file_path)}]({os.path.relpath(file_path)}) | {idea} | Pending |\n")
        
        readme.write("\n## Tests\n\n")
        readme.write("| File | Test | Result |\n")
        readme.write("|------|------|--------|\n")
        for file_path, test in metadata['tests']:
            readme.write(f"| [{os.path.relpath(file_path)}]({os.path.relpath(file_path)}) | {test} | Pending |\n")

if __name__ == "__main__":
    project_directory = '/home/timothy/pylon'  # Replace with your project directory
    readme_path = os.path.join(project_directory, 'README.md')
    metadata = gather_metadata(project_directory)
    generate_readme(metadata, readme_path)
    print(f"README.md has been updated with tasks, ideas, and tests.")