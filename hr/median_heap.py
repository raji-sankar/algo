class Heap(object):

    def __init__(self):
        self.items = []

    def insert(self, k):
        self.items.append(k)
        child_index = len(self.items) -  1
        parent_index = self.get_parent_index(child_index)
        if not self.is_child(child_index, parent_index):
            self.bubble_up(child_index, parent_index)

    def get_parent_index(self, child_index):
        return ((child_index +1)/2) -1


    def bubble_up(self, child_index, parent_index):
        if not self.is_child(child_index, parent_index):
            child = self.items[child_index]
            self.items[child_index] = self.items[parent_index]
            self.items[parent_index] = child
            self.bubble_up(parent_index, self.get_parent_index(parent_index))

        return


    def is_child(self, child_index, parent_index):
        return self.items[parent_index] <= self.items[child_index]


    def peek(self):
        return ','.join(str(x) for x in self.items)

    def remove(self):
        root = self.items[0]
        self.items[0] = self.items.pop()
        self.bubble_down(0)
        return root

    def get_smaller_child(self, parent_index):
        max_index = len(self.items) - 1
        child_indices = []
        child_1 = (parent_index +1)*2 -1
        child_2 = (parent_index +1)*2
        for child in (child_1, child_2):
            if child <= max_index:
                child_indices.append(child)

        if child_indices:
            return min(child_indices, key=lambda x: self.items[x])
        else:
            return None


    def bubble_down(self, parent_index):
        child_index = self.get_smaller_child(parent_index)
        if child_index:
            if not self.is_child(child_index, parent_index):
                child = self.items[child_index]
                self.items[child_index] = self.items[parent_index]
                self.items[parent_index] = child
                self.bubble_down(child_index)

        return

#  4 13 8 4 9 12 11 4 9 7

a = map(int, raw_input().strip().split())
heap = Heap()
for x in a:
    heap.insert(x)
    print heap.peek()


for i in range(len(a)-1):
    y = heap.remove()
    print y
    print heap.peek()

