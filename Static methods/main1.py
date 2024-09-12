# static method using decorator

class Math:
    @staticmethod
    def add(arg1, arg2):
        # Method code here
        return arg1 + arg2

# Calling the static method
result = Math.add(5, 10)
print(result)  # Output: 15
