from typing import *
#from typing import List, Dict, Tuple, Set, Union, Optional, Callable, Any

# Basic Data Types
integer: int = 10
floating_point: float = 3.14
boolean: bool = True
string: str = 'This is a string'

# Collection Types
integer_list: List[int] = [1, 2, 3]
string_to_int_dict: Dict[str, int] = {"key": 1}
tuple_example: Tuple[int, str, float] = (1, "two", 3.0)
integer_set: Set[int] = {1, 2, 3}

# Union (Multiple Types)
union_example: Union[int, str] = 42  # can be an integer or string
union_example_string: Union[int, str] = "Answer" # can be an integer or string

# Union (Multiple Types) using | (Python 3.10+)
say_any_thing: int | str = 123
say_any_thing_string: int | str = "Hello"

# Optional (Can Be None)
optional_integer: Optional[int] = None
optional_integer_value: Optional[int] = 10
optional_integer_alt: int | None = None

# Callable (Functions)
callable_example: Callable[[int, int], int] = lambda a, b: a + b

# Example usage
sum_two_numbers: Callable[[int, int], int] = lambda x, y: x + y
result: int = sum_two_numbers(5, 7)

# Any (Any type)
any_example: Any = "Could be anything"
any_example_int: Any = 100



# Function
def sum_two_integers(a: int, b: int) -> int:
    return a + b

# Passing a callable to a function
def call_with_args(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)
    #Example usage:
    #   print(call_with_args(sum_two_integers, 5, 7))

