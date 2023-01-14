def getPi(cnt = 10000):
    pi = 0
    for n in range(0, cnt + 1):
        pi = pi + ((-1) ** n * 4 / (2 * n + 1))
        if n == 0:
            print('%20s' % ('초기값 : '), pi)
        else :
            print('%20s' % (str(n) + ' 번째 : '), pi)
getPi(100000)