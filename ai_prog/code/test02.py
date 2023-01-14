'''
    파이 값을 구하는 방법중에 Leibniz 수열을 이용하는 방법이 있다.
    위 식을 이용하여 파이 값을 구하는 코드를 작성하시오.
'''

def getPi(cnt = 10000):
    pi = 0
    for n in range(0, cnt + 1):
        pi = pi + ((-1) ** n * 4 / (2 * n + 1))
        if n == 0:
            print('%20s' % ('초기값 : '), pi)
        else :
            print('%20s' % (str(n) + ' 번째 : '), pi)
getPi(100000)
