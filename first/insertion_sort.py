import sys

def insertion_sort_step(ar):
    new_elment = ar[-1]
    for i in xrange(len(ar)):
        j = ((i+1) * - 1) - 1
        if (abs(j) <= len(ar)) and new_elment < ar[j]:
            ar[j +1] = ar[j]
            # print ' '.join(map(str,ar))
        else:
            ar[j+1] = new_elment
            # print ' '.join(map(str,ar))
            break


def insertion_sort(ar):
    # break up the array into parts and run insertion_sort on smaller array
    smaller_arry = ar[:1]
    for k in xrange(1, len(ar)):
        smaller_arry.append(ar[k])
        insertion_sort_step(smaller_arry)
        print ' '.join(map(str,smaller_arry + ar[k+1:]))



n = raw_input().strip()
ar = map(int, raw_input().strip().split())
insertion_sort(ar)