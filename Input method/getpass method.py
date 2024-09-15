from getpass import getpass, getuser

# printing the current username
print("Your user name:", getuser(), end="\n\n")

# there will be no 'echo' feedback
string: str = getpass("Enter a sensitive string: ")
print("You entered: \n\t", string)

''' Expected output '''
# Your user name: mjtech
#
# Enter a sensitive string: ***************
# You entered:
#          IS this code working...?

