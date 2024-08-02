import re
# Detect if your passwords are strong enough


def isStrongPassword(password):
    if len(password) < 16:  # checks length  of password 
        return False
    if not re.search(r'[A-Z]', password) or not  re.search(r'[a-z]', password):# checks upper and lower case letters
        return False
    if not re.search(r'\d', password):#check for numbers
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]',password):#checks for special characters
        return False
    return True

Password_list = ['Password123','Password12345*!?','Weak','password','dşlasfadskflislkfia']

for i in Password_list:
    if isStrongPassword(i):
        print(f'{i} is a strong password')