# Please provide Command Line Arguments (CLA)
# EG:- python Add.py 1 2 3 4

import sys

sum = 0
# The 0st argument will always be the name of the pgm itself
for i in sys.argv[1:]:
    sum+=int(i)

print("Sum:", sum)