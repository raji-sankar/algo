import sys


def flip_bits(x):
    b = '{0:b}'.format(x).zfill(32)
    c = ''.join(['1' if j=='0' else '0' for j in b])
    return int(c, base=2)


n = int(raw_input().strip())
for i in xrange(n):
    x = int(raw_input().strip())
    print flip_bits(x)