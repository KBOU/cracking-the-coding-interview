# coding: utf-8

class BSTree(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_node(self, node):
        if node > self:
            self.right = node
        else:
            self.left = node

    def __cmp__(self, other):
        return self.data - other.data

    def __str__(self):
        return "Node(" + str(self.data) + ")"

    def print_tree(self):
        print self
        if self.left is not None:
            print self, "left", 
            self.left.print_tree()
        if self.right is not None:
            print self, "right", 
            self.right.print_tree()


def create_BSTree(sorted_arr, left, right):
    if left > right:
        return None

    mid = (left + right) / 2

    root = BSTree(sorted_arr[mid])

    root.left = create_BSTree(sorted_arr, left, mid - 1)
    root.right = create_BSTree(sorted_arr, mid + 1, right)

    return root


if __name__ == "__main__":
    sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    root = create_BSTree(sorted_arr, 0, 8)
    root.print_tree()
