def fib(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

f = [0, 1] + [None]*100

def fib1(n):
    print 'getting fib1 of %d' %(n)
    if f[n] is None:
        f[n] = fib1(n-1) + fib1(n-2)
    return f[n]


def main():
    print('123')
    print(fib1(8))

