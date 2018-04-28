import sys


def digits(n):
    s = str(n)
    num = 0
    for x in s:
        if not x == '0' and n % int(x) == 0:
            num += 1
    print num



t = int(raw_input().strip())
for i in range(t):
    n = int(raw_input().strip())
    digits(n)
