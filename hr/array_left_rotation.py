'''
Sample Input
5 4
1 2 3 4 5
Sample Output
5 1 2 3 4
'''


def array_left_rotation(a, n, k):
    return a[k:] + a[0:k]


n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str, answer))