def subset(n,k):
    print 'n = %d and k = %d' %(n, k)
    if k == 0 or n == k:
        return 1
    else:
        return subset(n-1, k-1) + subset(n-1, k)

counter = 0


def subsets(s, n, k, a=None):
    global counter
    counter += 1
    print 'counter %d' %(counter)
    print 'n = %d and k = %d' %(n, k)
    print s
    if a:
        print a
    if k == 0:
        print 'returning S + a = ' + str(a) if a else ''
        return a if a else []
    if n == k:
        print 'returning s + a'
        return s + a if a else s
    '''
    if a is None:
        a = []
    a.append(s[-1])

    return [subsets(s[:-1], n-1, k-1, a) , subsets(s[:-1], n-1, k)]'''
    return subsets(s[:-1], n-1, k-1, a=[s[-1]]+a if a else [s[-1]]) , subsets(s[:-1], n-1, k, a=a)


def subset_sum(s, c, a=None):
    if a is None:
        pass

def is_a_solution(current_step, set_upper_bound):
    return current_step == set_upper_bound

def process_solution(partial_sol, current_step):
    print '{' + ''.join([str(x) for x in range(current_step + 1)  if partial_sol[x]]) + '}'


def construct_candidates(candidates):
    candidates[0] = True
    candidates[1] = False
    return candidates



finished = False
def backtrack(partial_sol, current_step, set_upper_bound):
    num_candidates = 2
    candidates = range(num_candidates)

    if is_a_solution(current_step, set_upper_bound):
        process_solution(partial_sol, current_step)
    else:
        current_step += 1
        candidates = construct_candidates(candidates)
        for x in range(num_candidates):
            partial_sol[x] = candidates[x]
            backtrack(partial_sol, current_step, set_upper_bound)





def main():
    #print(subset(4,2))
    # print subsets([1, 2, 3, 4], 4, 2)

    set_upper_bound = 3
    partial_sol = range(set_upper_bound + 1)
    backtrack(partial_sol, 0, set_upper_bound)
