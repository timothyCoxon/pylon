import unittest
import os
import shutil
from pylon._dev.meta.update_files_with_metadata import update_python_file, update_markdown_file, update_files_from_csv

class TestUpdateFilesWithMetadata(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a temporary directory for test files
        cls.test_dir = '/home/timothy/pylon/_dev/tests/test_files'
        os.makedirs(cls.test_dir, exist_ok=True)

        # Create sample Python and Markdown files
        cls.python_file_path = os.path.join(cls.test_dir, 'sample.py')
        cls.markdown_file_path = os.path.join(cls.test_dir, 'sample.md')

        with open(cls.python_file_path, 'w') as f:
            f.write("print('Hello, World!')\n")

        with open(cls.markdown_file_path, 'w') as f:
            f.write("# Sample Markdown\n")

    @classmethod
    def tearDownClass(cls):
        # Remove the temporary directory after tests
        shutil.rmtree(cls.test_dir)

    def test_update_python_file(self):
        metadata = {
            'name': 'Sample Python File',
            'purpose': 'A sample Python file for testing.',
            'complete': 'yes',
            'task': 'task1, task2',
            'idea': 'idea1, idea2',
            'test': 'test1, test2'
        }
        update_python_file(self.python_file_path, metadata)

        with open(self.python_file_path, 'r') as f:
            content = f.read()

        self.assertIn("# name: Sample Python File\n", content)
        self.assertIn("# purpose: A sample Python file for testing.\n", content)
        self.assertIn("# complete: yes\n", content)
        self.assertIn("# task: task1, task2\n", content)
        self.assertIn("# idea: idea1, idea2\n", content)
        self.assertIn("# test: test1, test2\n", content)

    def test_update_markdown_file(self):
        metadata = {
            'name': 'Sample Markdown File',
            'purpose': 'A sample Markdown file for testing.',
            'complete': 'yes',
            'task': 'task1, task2',
            'idea': 'idea1, idea2',
            'test': 'test1, test2'
        }
        update_markdown_file(self.markdown_file_path, metadata)

        with open(self.markdown_file_path, 'r') as f:
            content = f.read()

        self.assertIn("name: Sample Markdown File\n", content)
        self.assertIn("purpose: A sample Markdown file for testing.\n", content)
        self.assertIn("complete: yes\n", content)
        self.assertIn("task: task1, task2\n", content)
        self.assertIn("idea: idea1, idea2\n", content)
        self.assertIn("test: test1, test2\n", content)

    def test_update_files_from_csv(self):
        # Create a sample CSV file with correct headers matching the CSV content provided earlier
        csv_path = os.path.join(self.test_test_dir, 'sample.csv')
        with open(csv_path, 'w') as f:
            f.write("path,name,desc,complete,tasks,ideas,tests\n")  # use 'desc' instead of 'purpose'
            # Note that we also need to update 'tasks' to 'task', 'ideas' to 'idea', and 'tests' to 'test'
            f.write(f"{self.python_file_path},Sample Python File,A sample Python file for testing.,yes,task1, task2,idea1, idea2,test1, test2\n")
            f.write(f"{self.markdown_file_path},Sample Markdown File,A sample Markdown file for testing.,yes,task1, task2,idea1, idea2,test1, test2\n")

        update_files_from_csv(csv_path)

        with open(self.python_file_path, 'r') as f:
            python_content = f.read()

        with open(self.markdown_file_path, 'r') as f:
            markdown_content = f.read()

        self.assertIn("# name: Sample Python File\n", python_content)
        self.assertIn("# purpose: A sample Python file for testing.\n", python_content)
        self.assertIn("# complete: yes\n", python_content)
        self.assertIn("# task: task1, task2\n", python_content)
        self.assertIn("# idea: idea1, idea2\n", python_content)
        self.assertIn("# test: test1, test2\n", python_content)

        self.assertIn("name: Sample Markdown File\n", markdown_content)
        self.assertIn("purpose: A sample Markdown file for testing.\n", markdown_content)
        self.assertIn("complete: yes\n", markdown_content)
        self.assertIn("task: task1, task2\n", markdown_content)
        self.assertIn("idea: idea1, idea2\n", markdown_content)
        self.assertIn("test: test1, test2\n", markdown_content)

if __name__ == '__main__':
    unittest.main()