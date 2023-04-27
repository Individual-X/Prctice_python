"""Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result."""

#decalare two input string
str1= input()
str2 = input()
result = ''
#reverse the second string to avoid complex loop
str2 = str2[::-1]
length = len(str1) if len(str1) > len(str2) else len(str2)

for i in range(length):
    if i < len(str1):
        result = result + str1[i]
    if i <  len(str2):
        result = result + str2[i]

print(result)