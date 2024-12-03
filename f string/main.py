from datetime import datetime

# Basic f-string usage
name = "Rabin"
age = 20
intro = f"My name is {name} and I am {age} years old."
print(intro)
# Output: My name is Rabin and I am 20 years old.

# Using expressions inside f-strings
a, b = 7, 3
calculation = f"Sum of {a} and {b} is {a + b}, and their product is {a * b}."
print(calculation)
# Output: Sum of 7 and 3 is 10, and their product is 21.

# Using type conversions
value = 42
debug = f"Value in repr format: {value!r}, and in string format: {value!s}."
print(debug)
# Output: Value in repr format: 42, and in string format: 42.

# Formatting numbers
pi = 3.14159
formatted_pi = f"Pi up to 2 decimal places: {pi:.2f}"
large_number = 1234567890
formatted_large_number = f"Number with commas: {large_number:,}"
print(formatted_pi)
# Output: Pi up to 2 decimal places: 3.14
print(formatted_large_number)
# Output: Number with commas: 1,234,567,890

# Formatting dates
now = datetime.now()
formatted_date = f"Today's date is {now:%Y-%m-%d %H:%M:%S}."
print(formatted_date)
# Example Output: Today's date is 2024-12-03 10:30:00.

# Multiline f-string
address = "123 Python Lane"
city = "Codeville"
country = "Programistan"
profile = f"""
Name: {name}
Age: {age}
Address: {address}, {city}, {country}
"""
print(profile)
# Output:
# Name: Rabin
# Age: 20
# Address: 123 Python Lane, Codeville, Programistan

# Nesting expressions
radius = 5
nested = f"A circle with radius {radius} has an area of {3.14159 * (radius ** 2):.2f}."
print(nested)
# Output: A circle with radius 5 has an area of 78.54.
