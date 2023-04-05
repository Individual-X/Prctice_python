"""Write a Program to extract each digit from an integer in the reverse order."""
#testcase: If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

inp = int(input("Enter the number for extract:"))

while inp>0:
    number = inp % 10
    inp = inp // 10
    print(number, end =" ")
