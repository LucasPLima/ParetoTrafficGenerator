import itertools
import random

myList = [0]
myList2 = list(range(0,2))
lst = []

allCombinations = []
allCombinations2 = []
for theSize in range(1, len(myList)+1):
    for combination in itertools.combinations(myList, theSize):
        allCombinations.append(combination)

for theSize in range(1, len(myList2)+1):
    for combination in itertools.combinations(myList2, theSize):
        allCombinations2.append(combination)

print(random.choice(allCombinations))
print(allCombinations2)

