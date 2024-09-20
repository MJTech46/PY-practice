from time import sleep
from typing import Dict

cache: Dict[int, int] = {}

def factorial(n: int) -> int:
    # caching logic
    if n in cache:
        return cache[n]
    else:
        # business logic
        sleep(0.5) # simulating an expensive computation 
        if n==0:
            return 1
        result: int = n*factorial(n-1)
        cache[n] = result # saving the computed data to cache
        return result

print("computing the output:", factorial(10)) # slower
print("fetching from cache:", factorial(10))  # faster

# printing the cache dictionary
print(f"{cache=}")
