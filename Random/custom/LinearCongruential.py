import time

class LinearCongruentialGenerator:
    def __init__(self, seed):
        self.modulus = 2**32
        self.a = 1664525
        self.c = 1013904223
        self.seed = seed

    def random(self):
        self.seed = (self.a * self.seed + self.c) % self.modulus
        return self.seed / self.modulus

# Example usage
lcg = LinearCongruentialGenerator(seed=int(time.time()))
print(lcg.random())
