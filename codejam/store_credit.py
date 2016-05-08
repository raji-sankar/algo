import sys


# Skeina backtracking
# bool finished = FALSE; /* found all solutions yet? */
# backtrack(int a[], int k, data input)
# {
#   int c[MAXCANDIDATES]; /* candidates for next position */
#   int ncandidates; /* next position candidate count */
#   int i; /* counter */
#   if (is_a_solution(a,k,input))
#       process_solution(a,k,input);
#   else {
#       k = k+1;
#       construct_candidates(a,k,input,c,&ncandidates);
#       for (i=0; i<ncandidates; i++) {
#           a[k] = c[i];
#           make_move(a,k,input);
#           backtrack(a,k,input);
#           unmake_move(a,k,input);
#           if (finished) return; /* terminate early */
#       }
#   }
# }
# is_a_solution(int a[], int k, int n)
# {
#     return (k == n); /* is k == n? */
# }

# construct_candidates(int a[], int k, int n, int c[], int *ncandidates)
# {
#     c[0] = TRUE;
#     c[1] = FALSE;
#     *ncandidates = 2;
# }
# process_solution(int a[], int k)
# {
#     int i; /* counter */
#     printf("{");
#     for (i=1; i<=k; i++)
#         if (a[i] == TRUE) printf(" %d",i);
#             printf(" }\n");
# }

finished = False
def backtrack(case, a, k, input, credit):

    if finished:
        return
    if is_a_solution(case, a, k, input, credit):
        process_solution(case, a, k, input)
        return
    else:
        if k < len(input):
            k += 1
            candidates = construct_candidates(a, k, input, credit)
            for m in candidates:
                a[k-1] = m
                backtrack(case, a, k, input, credit)
        else:
            return



def is_a_solution(case, a, k, input, credit):
    sum = 0
    for j in range(k):
        if a[j]:
            sum += input[j]
    if sum == credit:
        return True
    else:
        return False

def process_solution(case, a, k, input):
    print "Solution"
    print "Case #" + str(case) + ': ' +' '.join(map(str,[x+1 for x, v in enumerate(a) if x]))
    finished = True

def construct_candidates(a, k, input, credit):
    x = sum(map(int, a))
    if  k < len(a) and input[k] < credit and x < 2:
        return (True, False)
    else:
        return (False,)

def calculate( input, credit, case) :
    a = [False] * len(input)
    k = 0
    case += 1
    backtrack(case, a, k, input, credit)

def brute_force(input, credit, case):
    b = len(input)
    for j in range(b):
        for m in range(j+1, b):
            if (input[j] + input[m]) == credit:
                print 'Case #' + str(case +1) + ': ' + str(j+1) + ' ' + str(m+1)
                return

def recursive_sol(input, credit, case):
    # if is_a_solution()
    pass


n = int(raw_input().strip())
for x in range(n):
    c = int(raw_input().strip())
    i = int(raw_input().strip())
    p = map(int, raw_input().strip().split())
    assert(i == len(p))
    brute_force(p, c, x)
    # calculate(p, c, x)
