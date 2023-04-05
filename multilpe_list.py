"""Create a new list from a two list using the following condition
Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list."""

list1 = input("enter list one:")
list2 = input("enter list two:")
list3=[]

cl1 = list1.split()
cl2 = list2.split()

for i in range(len(cl1)):
    cl1[i] = int(cl1[i])
    if cl1[i] %2 == 0:
        list3.append(cl1[i])

for i in range(len(cl2)):
    cl2[i] = int(cl2[i])
    if cl2[i] %2 != 0:
        list3.append(cl2[i])

print(list3)

