'''
Sample Input

3
{[()]}
{[(])}
{{[[(())]]}}
Sample Output

YES
NO
YES
'''

OPEN = ('{', '(', '[')
CLOSE = ('}', ')', ']')
PAIRS = (('{', '}'), ('(', ')'), ('[', ']'))

def is_matched(expression):
    s = Stack()


    for x in expression:
        if x in OPEN:
            s.push(x)
        elif x in CLOSE:
            if s.is_empty():
                return False
            y = s.pop()
            if (y, x) not in PAIRS:
                return False
        else:
            return False

    if not s.is_empty():
        return False

    return True


class Node(object):
    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt = nxt

class Stack(object):
    def __init__(self):
        self.top = None


    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_item = Node(data)
        new_item.nxt = self.top
        self.top = new_item

    def pop(self):
        old_top = self.top
        self.top = self.top.nxt
        return old_top.data


t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"