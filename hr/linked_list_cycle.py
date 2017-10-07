class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList(object):

    def __init__(self, head):
        self.head = head

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while(current.next):
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

def has_cycle(head):
    visited = []
    current = head
    while current.next:
        visited.append(current)
        if current.next in visited:
            return True
        current = current.next

    return False

