def find_max_l(n):
    max =  0
    for i in n:
        print 'i=%d, max=%d' %(i, max)
        if i > max:
            max = i

    return max

def main():
    n = [24, 10, 78, 1, 22, 27]
    print find_max_l(n)