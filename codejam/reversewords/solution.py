import sys

def reverse_words(s):
    return reversed(s.split())

n = int(raw_input().strip())
for i in xrange(n):
    s = raw_input().strip()
    print 'Case #' + str(i+1) + ": " + ' '.join(reverse_words(s))