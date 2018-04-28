class Heap(object):

    def __init__(self, is_min=True):
        self.items = []
        self.is_min = is_min

    def insert(self, k):
        self.items.append(k)
        child_index = len(self.items) -  1
        parent_index = self.get_parent_index(child_index)
        if not self.is_child(child_index, parent_index):
            self.bubble_up(child_index, parent_index)

    def get_parent_index(self, child_index):
        return ((child_index +1)/2) -1 if child_index > 1 else 0


    def bubble_up(self, child_index, parent_index):
        if not self.is_child(child_index, parent_index):
            child = self.items[child_index]
            self.items[child_index] = self.items[parent_index]
            self.items[parent_index] = child
            self.bubble_up(parent_index, self.get_parent_index(parent_index))

        return


    def is_child(self, child_index, parent_index):
        if self.is_min:
            return self.items[parent_index] <= self.items[child_index]
        else:
            return self.items[parent_index] >= self.items[child_index]


    def peek(self):
        return ','.join(str(x) for x in self.items)

    def remove(self):
        root = self.items[0]
        self.items[0] = self.items.pop()
        self.bubble_down(0)
        return root

    def get_child_candidate(self, parent_index):
        max_index = len(self.items) - 1
        child_indices = []
        child_1 = (parent_index +1)*2 -1
        child_2 = (parent_index +1)*2
        for child in (child_1, child_2):
            if child <= max_index:
                child_indices.append(child)

        if child_indices:
            if self.is_min:
                return min(child_indices, key=lambda x: self.items[x])
            else:
                return max(child_indices, key=lambda x: self.items[x])
        else:
            return None


    def bubble_down(self, parent_index):
        child_index = self.get_child_candidate(parent_index)
        if child_index:
            if not self.is_child(child_index, parent_index):
                child = self.items[child_index]
                self.items[child_index] = self.items[parent_index]
                self.items[parent_index] = child
                self.bubble_down(child_index)

        return

    def extract_min(self):
        self.remove()

    def extract_max(self):
        pass

class MedianHeap(object):

    def __init__(self):
        self.low_heap = Heap(is_min=False)
        self.high_heap = Heap()

    def insert(self, k):

        if len(self.low_heap.items) == 0 or k <= self.low_heap.items[0]:
            self.low_heap.insert(k)
        else:
            self.high_heap.insert(k)
        self.balance_heaps()

    def median(self):
        if len(self.high_heap.items) > 0:
            if len(self.high_heap.items) == len(self.low_heap.items):
                return (self.low_heap.items[0] + self.high_heap.items[0])/2.0
            if len(self.high_heap.items) > len(self.low_heap.items):
                return self.high_heap.items[0]
            else:
                return self.low_heap.items[0]

        else:
            return self.low_heap.items[0]

    def balance_heaps(self):
        if len(self.low_heap.items) - len(self.high_heap.items) > 1:
            self.high_heap.insert(self.low_heap.remove())
        elif len(self.high_heap.items) - len(self.low_heap.items) > 1:
            self.low_heap.insert(self.high_heap.remove())

#  4 13 8 4 9 12 11 4 9 7

# a = map(int, raw_input().strip().split())
# heap = Heap(is_min=False)
# for x in a:
#     heap.insert(x)
#     print heap.peek()
#
#
# for i in range(len(a)-1):
#     y = heap.remove()
#     print y
#     print heap.peek()

n = int(raw_input().strip())
a = []
a_i = 0
for a_i in xrange(n):
    a_t = int(raw_input().strip())
    a.append(a_t)

median_heap = MedianHeap()
for x in a:
    median_heap.insert(x)
    print "{0:0.1f}".format(median_heap.median())


