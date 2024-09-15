from os import read

print("Enter a string: ", end="")
# Reads up to 100 bytes from stdin
input_byte: bytes = read(0, 100)
# Conversion form 'bytes' to 'str'
string: str = input_byte.decode(encoding="utf-8")

print("You entered: \n\t", string)
