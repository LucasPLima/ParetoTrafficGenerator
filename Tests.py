import itertools
import random
from application_gen import paretoGen


def main():
    a, b = paretoGen.paretoCalculate()

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
    a = round(j/4)-1
    b = 2*a
    c = 3*a
    d = 4*a

    print(j)
    print(a,b,c,d)

    for i in range(a):
        print('a={}\tb ={}\tc={}\td={}'.format(i, (i+a+1), (i+b+1), (i+c+1)))


if __name__ == '__main__':
    main()