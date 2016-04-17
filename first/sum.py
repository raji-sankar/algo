import sys

def sum(ar):
    return reduce(lambda x, y: x+y, ar)

def main():
    n = int(raw_input().strip())
    ar = map(int, raw_input().strip().split(' '))
    print sum(ar)