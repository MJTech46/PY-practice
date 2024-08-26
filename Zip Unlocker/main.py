from zipfile import ZipFile, BadZipFile
from string import ascii_letters, digits

def zip_unlock_1d(file_name):
    """
    this can be only used for password of length one
    """
    total_str = digits + ascii_letters
    current_password_index = 0

    with ZipFile(file_name, 'r') as protected_file:
            while(True):
                try:
                    protected_file.extractall(pwd=bytes(total_str[current_password_index], encoding='utf-8'))
                    break
                except RuntimeError as e:
                    #print("Wrong password!")
                    current_password_index += 1
            print("The password is: "+total_str[current_password_index])

# usage
zip_unlock_1d("protected.zip")
