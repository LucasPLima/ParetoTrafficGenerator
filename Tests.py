import itertools
import random

def func_test(*args):
    print("Length ={}".format(len(args)))
    print(args[0][2])


def main():
    myList = [0]
    myList2 = [0,4,5,2]
    lst = []
    func_test(myList2)
    allCombinations = []
    allCombinations2 = []
    for theSize in range(1, len(myList)+1):
        for combination in itertools.combinations(myList, theSize):
            allCombinations.append(combination)

    for theSize in range(1, len(myList2)+1):
        for combination in itertools.combinations(myList2, theSize):
            allCombinations2.append(combination)

    myList2_cp = myList2[1:]
    #print(random.choice(allCombinations))
    #print(allCombinations2)
    print(myList2_cp)

if __name__ == '__main__':
    main()