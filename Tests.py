import itertools
import random
from application_gen import paretoGen


def main():
    a, b = paretoGen.paretoCalculate()
    print(sum(a))
    c = sum(a)
    d = []
    for i in range(4):
        e = round(sum(a)/5)
        d.append(e)
        c = c-e

    d.append(c)

    print(d)

if __name__ == '__main__':
    main()