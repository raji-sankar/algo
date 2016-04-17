import sys


def tree(n):
    if n == 0:
        return 1

    if n % 2 == 1:
        return 2 * tree(n-1)
    else:
        return tree(n-1) + 1


def main():
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        print tree(n)

