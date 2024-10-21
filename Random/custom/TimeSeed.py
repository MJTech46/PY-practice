import time

def custom_random(minimum, maximum):
    # Get the current time in seconds
    current_time = time.time()
    # Convert the time to a string and reverse it
    reversed_time_str = str(current_time)[::-1]
    # Take the first few digits and convert back to float
    random_fraction = float(reversed_time_str[:6]) / 1e6
    # Scale the random fraction to the desired range
    return minimum + random_fraction * (maximum - minimum)

# Example usage
min_val = 1
max_val = 100
print(custom_random(min_val, max_val))
