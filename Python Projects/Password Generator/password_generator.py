import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letters
    
    if numbers:
        characters += letters
    
    if special_characters:
        characters += special
        
    password = ""
    meets_criteria = False
    has_number = False
    has_special = False
    
    while not meets_criteria and len(password) < min_length:
        new_char = random.choice(characters)
        password += new_char 
        
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
            
        meets_criteria = True
        if numbers and not has_number:
            meets_criteria = False
        if special_characters and not has_special:
            meets_criteria = False 
    return password

while True:
    min_length = int(input("Enter the mininum length of the password: "))
    has_number = input("Do you want to have numbers? (Y/N) ").upper() == "Y"
    has_special = input ("Do you want to have special characters? (Y/N) ").upper() == "Y"
    password = generate_password(min_length, has_number, has_special)
    print(f"The generated password is {password}")
    continue_or_not = input("Do you want to generate another password? (Y/N) ").upper() 
    if continue_or_not == "N":
        break