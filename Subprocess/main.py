# This is the main file which will create subprocess
import subprocess

def basic() -> None:
    #creating a command for the CMD
    cmd_str: str = f"python print-range.py {0} {10}"

    # calling the subprocess
    process: str = subprocess.Popen(cmd_str, shell=True)
    print("The subprocess's PID:",process.pid)

    # connection the subprocesses to the main process
    exit_code: str = process.wait()
    print("The subprocess's exit code:",exit_code)

basic()

