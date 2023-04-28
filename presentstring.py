'''Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter.'''
str1 = input()
str2 = input()

flag  = True
for item in str1:
    if item in str2:
        continue
    else:
        flag = False

print(flag)