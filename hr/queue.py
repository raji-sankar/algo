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


class Queue(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def peek(self):
        return self.head.data


    def enqueue(self, data):
        node = Node(data)
        if self.tail:
            self.tail.nxt = node
        self.tail = node

        if self.head is None:
            self.head = node

    def dequeue(self):
        ret = self.head.data
        self.head = self.head.nxt
        if self.head is None:
            self.tail = None
        return ret


