def yieldtest():
    for i in range(4):
        yield i

def main():
    print(next(yieldtest()))
    print(next(yieldtest()))

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
    # j = len(a)
    # b = 4
    # a = round(j/b)
    # ctr.append(a)
    # for i in range(2, b):
    #     ctr.append(a*i)
    # print(ctr)
    #
    # # if j % b == b-2 or j % b == b-1:
    # #     for i in range(len(ctr)):
    # #         ctr[i] = ctr[i] - (b-(j % b))
    #
    # print(ctr)
    #
    # for i in range(ctr[0]):
    #     print('a={}\tb={}\tc={}\td={}'.format(i, (i + ctr[0]), (i+ctr[1]), (i+ctr[2])))
    #
    # print(j-1)
    # print(j % b)


if __name__ == '__main__':
    main()