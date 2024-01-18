import os
import random
import string
from colorama import *

def generate_random_string(length=8):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

def ultimate_renamer():
    current_dir = os.getcwd()

    for filename in os.listdir(current_dir):
        if os.path.isfile(os.path.join(current_dir, filename)) and filename != os.path.basename(__file__):
            file_name, file_extension = os.path.splitext(filename)
            new_name = generate_random_string()
            new_filename = new_name + file_extension
            os.rename(os.path.join(current_dir, filename), os.path.join(current_dir, new_filename))
            print(f'{Fore.WHITE}[{Fore.GREEN}OK{Fore.WHITE}]: Renamed {Fore.YELLOW}{filename}{Fore.WHITE} to {Fore.YELLOW}{new_filename}{Fore.WHITE}')
            
if __name__ == "__main__":
    ultimate_renamer()

os.system("pause>nul")