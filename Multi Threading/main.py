# Multi Threading Example Using Python #
from threading import Thread
from time import sleep, time

## Decorator ##
def calc_exe_time(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
        print(f"{func.__name__} took {execution_time:.2f}ms", end="\n\n")
        return result
    return wrapper


## Thread functions with decorator ##
@calc_exe_time
def my_function1():
    # Simulating a long process
    sleep(2)
    print("my_function1  completed a long process.")
    

@calc_exe_time
def my_function2():
    # Simulating a long process
    sleep(6)
    print("my_function2  completed a long process.")
    

## main function ##
@calc_exe_time
def main():
    # Create new threads
    my_thread1 = Thread(target=my_function1)
    my_thread2 = Thread(target=my_function2)

    # Starting the thread
    my_thread1.start()  
    my_thread2.start()

    # Wait for threads to complete
    # (for calculating the complete program execution time)
    my_thread1.join()  
    my_thread2.join()

## Entry point for execution ##
if __name__ == "__main__":
    main()
