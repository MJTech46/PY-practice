# Define a metaclass
class PrintMyName(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class: {name}")
        return super().__new__(cls, name, bases, dct)

# Define a class using the metaclass
class TestClass(metaclass=PrintMyName):
    pass

class NewExample(metaclass=PrintMyName):
    pass

# When TestClass is defined, the metaclass will be triggered
# Output: Creating class TestClass

obj1: TestClass = TestClass()
obj2: NewExample = NewExample()
