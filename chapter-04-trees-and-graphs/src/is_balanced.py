# coding: utf-8


class Tree(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def check_height(node):
    if node == None:
        return 0

    left = check_height(node.left)
    if left == -1:
        return -1
    right = check_height(node.right)
    if right == -1:
        return -1

    if abs(left - right) > 1:
        return -1
    else:
        return max(left, right) + 1

if __name__ == "__main__":
    root = Tree(1)
    node = Tree(2)
    root.left = node
    node = Tree(3)
    root.right = node
    node = Tree(4)
    root.left.left = node
    node = Tree(5)
    root.left.right = node
    node = Tree(6)
    root.right.left = node
    node = Tree(7)
    root.right.right = node
    print check_height(root)
    node = Tree(8)
    root.right.right.right = node
    node = Tree(9)
    root.right.right.right.right = node
    print check_height(root)

