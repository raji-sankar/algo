import sys


def funny_string(s):
    rev = s[::-1]
    for j in xrange(1, len(s)):
        if abs(ord(s[j]) - ord(s[j-1])) != abs(ord(rev[j])- ord(rev[j-1])):
            return False
    return True

n = int(raw_input().strip())
for i in range(n):
    s = raw_input().strip()
    print 'Funny' if funny_string(s) else 'Not Funny'