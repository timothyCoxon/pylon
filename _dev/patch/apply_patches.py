# name: apply_patches
# purpose: Script to apply patches to the project
# complete: No
# task: [x] Need moving to ~/[pylon]/pylon/_dev/
# idea: 
# test: Need Tests

import os

def apply_patch(file_path, changes):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for change in changes:
        line_num, new_content = change
        if 0 <= line_num < len(lines):
            lines[line_num] = new_content + '\n'

    with open(file_path, 'w') as file:
        file.writelines(lines)

def read_patch_file(patch_file):
    patches = {}
    with open(patch_file, 'r') as file:
        lines = file.readlines()
        current_file = None
        for line in lines:
            if line.startswith('file:'):
                current_file = line.strip().split(':', 1)[1].strip()
                patches[current_file] = []
            elif line.startswith('change:'):
                if current_file:
                    line_num, new_content = line.strip().split(':', 1)[1].split(',', 1)
                    patches[current_file].append((int(line_num), new_content.strip()))
    return patches

def apply_patches(patch_file):
    patches = read_patch_file(patch_file)
    for file_path, changes in patches.items():
        if os.path.exists(file_path):
            apply_patch(file_path, changes)
        else:
            print(f"File {file_path} does not exist.")

if __name__ == "__main__":
    patch_file = 'patches.txt'
    apply_patches(patch_file)