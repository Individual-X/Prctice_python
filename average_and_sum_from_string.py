"""Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters."""
str  = input()
number = 0
sum = 0
for item in str:
    if item.isdigit():
        sum += int(item)
        number+=1
        
print(sum)
print(sum/number)