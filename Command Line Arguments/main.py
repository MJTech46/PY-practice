# Command Line Arguments in Python
import sys

# Provide arguments at the execution 
# EG:- 
#   Input:-  python main.py one 2 III 
#   Output:- ['main.py', 'one', '2', 'III']
print(sys.argv)

print(type(sys.argv[0]))
