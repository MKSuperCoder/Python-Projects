import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special
        
    password = ""
    meets_condition = False
    has_numbers = False
    has_special = False
    
    while not meets_condition or len(password) < min_length:
        new_char = random.choice(characters)
        password += new_char
        
        if new_char in digits:
            has_numbers = True
        elif new_char in special:
            has_special = True
        
        meets_condition = True
        
        if numbers:
            meets_condition = has_numbers
        if special_characters:
            meets_condition = meets_condition and has_special
    return password
    
while True:
    get_password = input("Do you want to generate a pasasword? (Y/N) ").upper()
    if get_password == "N":
        break
    pwd_length = int(input("How long do you want your password to be? "))
    has_numbers = input("Do you want to include a number in your password? (Y/N) ").upper() == "Y"
    has_special_characters = input("Do you want to include special characters? (Y/N)" ).upper() == "Y"
    password = generate_password(pwd_length, has_numbers, has_special_characters)
    print(password)
      
    