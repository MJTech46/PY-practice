# static method using function

class Math:
    def add(arg1, arg2):
        # Method code here
        return arg1 + arg2

    static_method = staticmethod(add)

# Calling the static method
result = Math.static_method(5, 10)
print(result)  # Output: 15

