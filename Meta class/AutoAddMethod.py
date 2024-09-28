def new_method(self):
    print("This is a dynamically added method :)")

class AddMethodMeta(type):
    def __new__(cls, name, bases, dct):
        dct['dynamic_method'] = new_method
        return super().__new__(cls, name, bases, dct)
    

   
class MyClass(metaclass=AddMethodMeta):
    pass

class NewExample(metaclass=AddMethodMeta):
    pass


obj1: MyClass = MyClass()
obj2: MyClass = MyClass()

obj1.dynamic_method()  # "This is a dynamically added method"
obj2.dynamic_method()  # "This is a dynamically added method"
