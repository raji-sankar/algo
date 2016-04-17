import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    a = raw_input().strip()
    b = raw_input().strip()

    c= False

    j = set(a)
    k = set(b)
    if j.intersection(k):
        c = True

    if c:
        print 'YES'
    else:
        print 'NO'



