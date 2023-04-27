#Count all letters, digits, and special symbols from a given string
str = input()
print("Original string:", str)
alpha = 0
chr = 0
digit = 0

for item in str:
    if item.isalpha():
        alpha += 1
    elif item.isdigit():
        digit += 1
    else:
        chr += 1

print("Alphabet:", alpha , "Digit:", digit , "Char:", chr)