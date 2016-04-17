import sys

def main():
    n = int(raw_input().strip())
    arr = map(int,raw_input().strip().split(' '))
    p = reduce(lambda x, y: x+ (y > 0), arr, 0)
    z = reduce(lambda x, y: x+ (y == 0), arr, 0)
    m = reduce(lambda x, y: x+ (y < 0), arr, 0)
    print '{:f}'.format(p/float(n))
    print '{:f}'.format(m/float(n))
    print '{:f}'.format(z/float(n))

