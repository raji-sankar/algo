'''
Sample Input
10
1 42
2
1 14
3
1 28
3
1 60
1 78
2
2
Sample Output
14
14
'''

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

    def peek(self):
        return self.top.data


class MyQueue(object):
    def __init__(self):
        self.first = Stack()
        self.second = Stack()
        self.in_order = False

    def peek(self):
        if self.in_order:
            return self.second.peek()
        else:
            while not self.first.is_empty():
                self.second.push(self.first.pop())
            data = self.second.peek()
            self.in_order = True
            return data


    def pop(self):
        if self.in_order:
            return self.second.pop()
        else:
            while not self.first.is_empty():
                self.second.push(self.first.pop())
            data = self.second.pop()
            self.in_order = True
            return data

    def put(self, value):
        if not self.in_order:
            self.first.push(value)
        else:
            while not self.second.is_empty():
                self.first.push(self.second.pop())
            self.first.push(value)
            self.in_order = False


queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())

    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()