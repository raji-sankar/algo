import sys

def bubble_sort(ar):
    num_sorts = 0
    for i in range(len(ar)):
        for j in range(len(ar) -1):
            if ar[j] > ar[j+1]:
                num_sorts += 1
                ar[j], ar[j+1] = ar[j+1], ar[j]
        if num_sorts == 0:
            break
    print 'Array is sorted in {0} swaps.'.format(num_sorts)
    print 'First Element: {0}'.format(ar[0])
    print 'Last Element: {0}'.format(ar[-1])


n = int(raw_input().strip())
ar = map(int, raw_input().strip().split())
bubble_sort(ar)