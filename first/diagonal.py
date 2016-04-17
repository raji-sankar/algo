import sys

def main():
    n = int(raw_input().strip())
    a = []
    for a_i in xrange(n):
       a_temp = map(int,raw_input().strip().split(' '))
       a.append(a_temp)

    b = [a[i][i] for i in range(n)]
    s1 = reduce(lambda x, y: x+y, b)
    c = [a[i][n-1-i] for i in range(n)]
    s2 = reduce(lambda x, y: x+y, c)
    d = abs(s1 - s2)
    print d