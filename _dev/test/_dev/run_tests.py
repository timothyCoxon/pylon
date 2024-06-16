import os
import subprocess

def run_tests_and_update_headers(project_dir, tests_dir):
    for root, _, files in os.walk(tests_dir):
        for file in files:
            if file.endswith('_test.py'):
                test_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(test_file_path, tests_dir)
                target_file_path = os.path.join(project_dir, relative_path.replace('_test.py', '.py'))
                
                if os.path.exists(target_file_path):
                    result = subprocess.run(['python', test_file_path], capture_output=True, text=True)
                    test_result = result.stdout.strip()
                    
                    update_test_result_in_header(target_file_path, test_result)

def update_test_result_in_header(file_path, test_result):
    lines = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Remove existing test result comments
    lines = [line for line in lines if not line.startswith('# test result:')]
    
    # Add new test result comment
    lines.insert(0, f"# test result: {test_result}\n")
    
    with open(file_path, 'w') as file:
        file.writelines(lines)

if __name__ == "__main__":
    project_directory = '/home/timothy/pylon'  # Replace with your project directory
    tests_directory = '/home/timothy/pylon/_dev/tests'  # Replace with your tests directory
    run_tests_and_update_headers(project_directory, tests_directory)
    print("Tests have been run and results updated in headers.")