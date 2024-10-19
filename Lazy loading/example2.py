from time import sleep

class HeavyComputation:
    def __init__(self):
        self._result = None  # The result is initially set to None

    @property
    def result(self):
        if self._result is None:  # Check if the result is already computed
            print("Performing heavy computation...")
            self._result = self._perform_heavy_computation()
        return self._result

    def _perform_heavy_computation(self):
        # Simulate a heavy computation (e.g., a large calculation or data fetch)
        sleep(3)
        return sum(i * i for i in range(1000000))  # A large computation

# Usage example
heavy_computation = HeavyComputation()

# The heavy computation is not performed yet
print("Object created, computation not performed.")

# Access the result for the first time; the computation will now run
print("Result:", heavy_computation.result)

# Access the result again; the heavy computation won't run this time
print("Result again:", heavy_computation.result)
