'''
Input (stdin)
2
1 2 3 4 5 6 7
Your Output (stdout)
Yes
Expected Output
Yes

Case 6
Input
4
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 16 18 19 20 21 22 23 24 25 26 27 28 29 30 31
Output
No

Case 1
Input
4
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
Output
No
Case 3
Input
2
1 2 2 4 5 6 7
Output
No
'''

class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, d):
        if d <= self.data:
            if not self.left:
                self.left = Node(d)
            else:
                self.left.insert(d)
        else:
            if not self.right:
                self.right = Node(d)
            else:
                self.right.insert(d)

    def find(self, value):
        if value == self.data:
            return True
        elif value < self.data:
            if not self.left:
                return False
            else:
                return self.left.find(value)
        else:
            if not self.right:
                return False
            else:
                return self.right.find(value)

    def print_in_order(self):
        if self.left:
            self.left.print_in_order()
        print self.data
        if self.right:
            self.right.print_in_order()

    def print_pre_order(self):
        print self.data
        if self.left:
            self.left.print_pre_order()
        if self.right:
            self.right.print_pre_order()


def check_bst(root, max=10000, min=0):

    if root.left:
        print 'left'
        if root.left.data < root.data and root.left.data < max:
            max = root.left.data
            return check_bst(root.left, max=max, min=None)
        else:
            return False
    if root.right:
        print 'right'
        min = root.right.data
        if root.right.data > root.data and root.right.data > min:
            return check_bst(root.right, max=max, min=min)
        else:
            return False

    return True

def is_bst(root, max=10000, min = 0):

    if root is not None:
        print root.data, max, min
        if root.data >= max or root.data <= min:
            return False

        return  is_bst(root.left, root.data, min) and is_bst(root.right, max, root.data)

    else:
        return True



def checkBST(root):
    #A tree is a binary search tree if the left element is less than the current node
    # and the right node is greater than the current node
    #traverse the tree in order
    return is_bst(root)

def create_binary_tree(elements, start, end):
    if start > end:
        return None

    mid = (start + end)/2
    node = Node(elements[mid])
    node.left = create_binary_tree(elements, start, mid-1)
    node.right = create_binary_tree(elements, mid+1, end)
    return node

n = int(raw_input().strip())
a = map(int, raw_input().strip().split())
node = create_binary_tree(a, 0, len(a)-1)
node.print_pre_order()
if checkBST(node):
    print 'YES'
else:
    print 'NO'




