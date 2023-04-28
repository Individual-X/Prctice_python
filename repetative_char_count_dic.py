str1 = input()

outdic = dict()

for char in str1:
    count  = str1.count(char)
    outdic [char] = count
print(outdic)