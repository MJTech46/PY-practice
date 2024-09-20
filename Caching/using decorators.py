from functools import lru_cache
from time import sleep

@lru_cache(maxsize=100)
def factorial(n: int) -> int:
    sleep(0.5) # simulating an expensive computation 
    if n==0:
        return 1
    return n*factorial(n-1)


print("computing the output:", factorial(10)) # slower
print("fetching from cache:", factorial(10))  # faster

# printing the cache information
print({factorial.cache_info()})
