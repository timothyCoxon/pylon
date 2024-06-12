import sys
import subprocess

# List of scripts to run in order
scripts = ["script1.py", "script2.py", "script3.py"]

def run_scripts(input_file):
    # Temporary variable to hold the current state of the text
    current_text = None
    
    with open(input_file, 'r') as file:
        current_text = file.read()
    
    for script in scripts:
        # Using subprocess to call each script with the current text as input
        process = subprocess.Popen(['python', script], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate(input=current_text)
        
        if process.returncode != 0:
            print(f"Error running {script}: {error}")
            sys.exit(1)
        
        # Update current_text with the output from the script
        current_text = output
    
    return current_text

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python central_control.py <chatlog_file>")
        sys.exit(1)
    
    chatlog_file = sys.argv[1]
    final_text = run_scripts(chatlog_file)
    print("Final modified text:", final_text)