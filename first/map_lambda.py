import sys

f = [0, 1] + [None]*15

def fibo(n):
    if f[n] is None:
        f[n] = fibo(n-1) + fibo(n-2)
    return f[n]




n = int(raw_input().strip())
g = map(fibo, xrange(n))
h = map(lambda x: x**3, g)
print h

