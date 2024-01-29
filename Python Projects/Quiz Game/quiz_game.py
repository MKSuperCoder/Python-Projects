print("Welcome to my quiz!")



while True:
    playing = input("Do you want to play my game? (Y/N) ").upper()
    if playing == "N":
        quit()
    elif playing == "Y":
        break
    else:
        print("Please type 'Y' or 'N' ")
      
print("Okay! Let's play: ")
score = 0 

answer = input("What does CPU stands for?\n").lower()
if answer == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")
    
answer = input("What does GPU stands for?\n").lower()
if answer == "graphics processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")
    
answer = input("What does RAM stands for?\n").lower()
if answer == "random access memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does PSU stands for?\n").lower()
if answer == "power supply":
    print("Correct")
    score += 1
else:
    print("Incorrect")
    
answer = input("What does HTML stands for?\n").lower()
if answer == "hypertext markup language":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print(f"You got {score} questions correct")
print(f"You got {score/5 * 100}%. ")