input = input("Enter a word or sentence you want to turn into an acronym: ")

text = input.split()

acronym = ""

for i in text:
    acronym += i[0].upper()
    
print(acronym)