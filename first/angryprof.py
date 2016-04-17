def main():
    t = int(raw_input().strip())
    for c in xrange(t):
        n,k = raw_input().strip().split(' ')
        n,k = [int(n),int(k)]
        a = map(int,raw_input().strip().split(' '))
        p = reduce(lambda x, y: x+ (y >= 0), a, 0)
        if p < k:
            print 'NO'
        else:
            print 'YES'


