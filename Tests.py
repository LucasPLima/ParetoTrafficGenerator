import itertools

myList = [0,1,2]
myList2 = [0,1]
allCombinations = []
allCombinations2 = []
for theSize in range(1, len(myList)+1):
    for combination in itertools.combinations(myList, theSize):
        allCombinations.append(combination)

for theSize in range(1, len(myList2)+1):
    for combination in itertools.combinations(myList2, theSize):
        allCombinations2.append(combination)

print(allCombinations)
print(allCombinations2)

