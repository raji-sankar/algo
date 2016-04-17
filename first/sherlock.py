import sys

def main():

    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        if n < 3:
            return -1
        elif n % 3 == 0:
            print '5'*n
        elif n % 3 == 2:
            print '5'* (((n/3) -1)*3) + '3' *5
        elif n % 3 == 1 and n > 10:
            print '5' * (((n-10)/3)*3) + '3' * 10
        elif n % 5 == 3:
            print '555' + ('3' * (n/5) * 5)
        elif n % 5 == 0:
            print '3'*n
        else:
            print -1




