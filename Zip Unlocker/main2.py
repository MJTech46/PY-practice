from zipfile import ZipFile, BadZipFile
from string import ascii_letters, digits
import itertools
from time import time

def unlock_zip(file_name, max_length=8):
    """
    itertools.product generates all possible combinations of characters up to the specified max_length.
    So his method allows trying passwords of varying lengths.
    """
    characters = ascii_letters + digits 
    
    with ZipFile(file_name, 'r') as zip_file:
        for length in range(1, max_length + 1):
            for password_tuple in itertools.product(characters, repeat=length):
                password = ''.join(password_tuple)
                try:
                    print(f"Trying the sequence: {password}")
                    zip_file.extractall(pwd=bytes(password, 'utf-8'))
                    print(f"The password is: {password}")
                    return
                except (RuntimeError, BadZipFile):
                    continue
        print("Password not found within the given length limit.")

# Usage
start_time = time()
unlock_zip("protected.zip")
end_time = time()

execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
print(execution_time)
