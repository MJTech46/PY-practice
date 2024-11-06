from enum import Enum

class Shape(Enum):
    CIRCLE = 1
    SQUARE = 2
    TRIANGLE = 3

    def describe(self):
        return f"This is a {self.name.lower()}."

# Usage
shape = Shape.CIRCLE
print(shape.describe())  # Output: This is a circle.
