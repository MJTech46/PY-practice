from fileinput import input as f_input, FileInput

print("Enter a string: ", end="")
# creating a file obj using fileinput.input() function
file_obj: FileInput[str] = f_input()
# collecting the input string from the file obj
string: str = file_obj.readline()

print("You entered: \n\t", string)

''' Expected output '''
# Enter a string: IS this code working...?
# You entered: 
#          IS this code working...?
