# name: setup_project
# purpose: Seems be the file that generates the patch files to update the project
# complete: No
# task: [x] Need moving to ~/[pylon]/pylon/_dev/
# idea: 
# test: Need Tests

import os
import csv
import subprocess

# Template for Python script headers
python_header_template = """# name: {name}
"""

# Template for Markdown front matter
markdown_front_matter_template = """---
name: {name}
purpose: {purpose}
task: {task1}
task: {task2}
test: {test}
task: {task3}
idea: {idea}
complete: {complete}
---
"""

# Default metadata values
default_metadata = {
    'name': 'example script',
    'purpose': 'to show the layout of a standard header',
    'task1': 'to include this in all python scripts',
    'task2': 'to make markdown files for each folder with similar info to this included as front matter.',
    'test': 'None as yet',
    'task3': 'Make Tests!',
    'idea': 'Make other things based on this like a project task list or test suite.',
    'complete': 'no'
}

def git_commit(directory, message):
    subprocess.run(['git', 'add', '.'], cwd=directory)
    subprocess.run(['git', 'commit', '-m', message], cwd=directory)

def prepend_metadata(file_path, metadata, log_file):
    with open(file_path, 'r') as original_file:
        original_content = original_file.read()
    if metadata.strip() not in original_content:
        with open(file_path, 'w') as modified_file:
            modified_file.write(metadata + '\n' + original_content)
        log_file.write(f"Patched: {file_path}\n")

def generate_patch_file(directory, log_file):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith('.py'):
                header = python_header_template.format(**default_metadata)
                prepend_metadata(file_path, header, log_file)
            elif file.endswith('.md'):
                front_matter = markdown_front_matter_template.format(**default_metadata)
                prepend_metadata(file_path, front_matter, log_file)

def generate_markdown_files(directory, log_file):
    for root, dirs, _ in os.walk(directory):
        for dir in dirs:
            md_file_path = os.path.join(root, dir, f'{dir}.md')
            with open(md_file_path, 'w') as md_file:
                md_file.write(markdown_front_matter_template.format(**default_metadata))
            log_file.write(f"Created: {md_file_path}\n")

def generate_rules_csv(directory):
    rules_csv_path = os.path.join(directory, 'rules.csv')
    rules = [
        ['Rule', 'Description'],
        ['Directory Structure', 'Organize files by action type and context.'],
        ['Metadata', 'Include metadata headers in Python scripts and front matter in Markdown files.'],
        ['Patch System', 'Use a patch file to apply changes across multiple files.']
    ]
    with open(rules_csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rules)

if __name__ == "__main__":
    project_directory = '/home/timothy/pylon'
    
    # Revert changes made by the previous script
    subprocess.run(['git', 'checkout', '--', '.'], cwd=project_directory)
    
    # Commit the current state before making changes
    git_commit(project_directory, "Backup before applying metadata patch")

    # Open log file
    log_file_path = os.path.join(project_directory, 'patch.log')
    with open(log_file_path, 'w') as log_file:
        generate_patch_file(project_directory, log_file)
        generate_markdown_files(project_directory, log_file)
        generate_rules_csv(project_directory)

    # Commit the changes after applying the patch
    git_commit(project_directory, "Applied metadata patch")