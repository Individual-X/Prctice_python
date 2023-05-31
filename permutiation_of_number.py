from itertools import permutations
list1 = [item for item in input().split()]
print(list1)
allcombinations = permutations(list1)
sum  = 0
for item in allcombinations:
    print(''.join(item))
    