"""
Example Usage: 
python try-seq.py [path: str] [length: int] [starting_index: int|None = None] [ending_index: int|None = None] 
"""
from zipfile import ZipFile, BadZipFile
from string import ascii_letters, digits
import sys
import itertools

## CLA collection part ##

# path for the file
try:
    file_name: str = sys.argv[1]
# for no input error
except IndexError:
    print("Please provide at least 2 Command Line Argument [path: str] [length: int]")
    exit()

# length for 'itertools.product'
try:
    length: int = int(sys.argv[2])
# for int conversion error
except ValueError:
    print("Please provide integer values")
    exit()
# for no input error
except IndexError:
    print("Please provide the 2nd Argument")
    exit()

# starting sequence
try:
    start_index: int|None = int(sys.argv[3])
# for int conversion error
except ValueError:
    print("Please provide integer values")
    exit()
# for no input error
except IndexError:
    start_index: int|None = None

# end sequence
try:
    end_index: str|None = sys.argv[3]
# for int conversion error
except ValueError:
    print("Please provide integer values")
    exit()
# for no input error
except IndexError:
    end_index: str|None = None

## working part ##

# creating the required characters
characters = ascii_letters + digits

with ZipFile(file_name, 'r') as file:
    # generating itertools.product obj using the CLA length
    cartesian_product : list[any] = list(itertools.product(characters, repeat=length))

    # using the required part if any
    cartesian_product = cartesian_product[start_index:end_index]

    #looping through each password
    for password_tuple in cartesian_product:
        password = ''.join(password_tuple)
        try:
            print(f"Trying the sequence: {password}")
            file.extractall(pwd=bytes(password, 'utf-8'))
            print(f"The password is: {password}")
            # exit with code 0 means ok
            exit(0)
        except (RuntimeError, BadZipFile):
            continue
    #providing a nonzero for representing not success
    exit(1)

