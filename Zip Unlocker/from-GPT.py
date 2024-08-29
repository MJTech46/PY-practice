from zipfile import ZipFile, BadZipFile
from string import ascii_letters, digits
from threading import Thread
from time import time
import itertools

def unlock_zip(file_name: str, sequence: itertools.product):
    with ZipFile(file_name, 'r') as file:
        for password_tuple in sequence:
            password = ''.join(password_tuple)
            try:
                print(f"Trying the sequence: {password}")
                file.extractall(pwd=bytes(password, 'utf-8'))
                print(f"The password is: {password}")
                return
            except (RuntimeError, BadZipFile):
                continue

def generate_thread(file_name: str, sequence: itertools.product):
    thread = Thread(target=unlock_zip, args=(file_name, sequence))
    thread.start()
    return thread

def main(file_name: str, max_length: int):
    characters = ascii_letters + digits

    threads = []
    for length in range(1, max_length + 1):
        sequence = itertools.product(characters, repeat=length)
        thread = generate_thread(file_name, sequence)
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start_time = time()
    main("protected.zip", 3)
    end_time = time()

    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    print(execution_time)
