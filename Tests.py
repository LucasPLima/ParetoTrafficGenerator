import itertools
import random
from application_gen import paretoGen


def main():
    a, b = paretoGen.paretoCalculate()
    ctr = []
    '''
    print(sum(a))
    c = sum(a)
    d = []
    for i in range(4):
        e = round(sum(a)/5)
        d.append(e)
        c = c-e

    d.append(c)

    print(d)
    '''
    j = len(a)
    a = round(j/5)
    ctr.append(a)
    for i in range(2,5):
        ctr.append(a*i)
    print(ctr)

    if j % 5 == 4 or j % 5 == 3:
        for i in range(len(ctr)):
            ctr[i] = ctr[i]-1

    print(ctr)
    print(ctr[0], ctr[1], ctr[2], ctr[3])

    for i in range(ctr[0]):
        print('a={}\tb ={}\tc={}\td={}\te={}'.format(i, (i + ctr[0]), (i + ctr[1]), (i + ctr[2]), (i + ctr[3])))

    print(j)
    print(j % 5)
if __name__ == '__main__':
    main()