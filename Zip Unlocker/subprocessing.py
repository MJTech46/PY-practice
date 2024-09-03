'''
import subprocess

file_path: str = "protected.zip"

max_subprocess: int = 3

subprocess_array: list[int] = []

def make_subprocess(current_count: int):
    cmd_str: str = f"python try-seq.py protected.zip {current_count}"
    subprocess_id: int = subprocess.call(cmd_str, shell=True)
    print(f"{subprocess_id}")

make_subprocess(1)
make_subprocess(2)
make_subprocess(3)
'''


import subprocess

file_path: str = "protected.zip"
max_subprocess: int = 3
subprocess_array: list[subprocess.Popen] = []

def make_subprocess(current_count: int):
    cmd_str: str = f"python try-seq.py {file_path} {current_count}"
    process = subprocess.Popen(cmd_str, shell=True)
    subprocess_array.append(process)
    print(f"Subprocess {current_count} PID: {process.pid}")

for i in range(1, max_subprocess + 1):
    make_subprocess(i)

# Wait for all subprocesses to complete
for process in subprocess_array:
    process.wait()

print("All subprocesses have completed.")

print("All subprocesses' PIDs:", subprocess_array)
