# This file is used to simulate a CLI app usage
# Usage: python print-range.py 0 10
import sys
import time

# starting index from CLA
start_int: int = int(sys.argv[1])

# ending index from CLA
end_int: int = int(sys.argv[2])

for i in range(start_int, end_int+1):
    print(i)
    # simulating a long task
    time.sleep(1)
