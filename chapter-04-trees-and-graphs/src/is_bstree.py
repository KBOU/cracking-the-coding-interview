import sys

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_bst(node):
    bst = False
    mx = -sys.maxint
    mn = sys.maxint

    l_bst = True
    l_mx = -sys.maxint
    l_mn = sys.maxint

    r_bst = True
    r_mx = -sys.maxint
    r_mn = sys.maxint

    if node.left is not None:
        (l_bst, l_mx, l_mn) = is_bst(node.left)
    if node.right is not None:
        (r_bst, r_mx, r_mn) = is_bst(node.right)

    if l_bst and r_bst and node.data > l_mx and node.data < r_mn:
        bst = True
        mx = r_mx if r_mx != -sys.maxint else node.data
        mn = l_mn if l_mn != sys.maxint else node.data

    return (bst, mx, mn)

if __name__ == "__main__":
    node0 = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)

    node0.left = node1
    node0.right = node2

    node1.left = node3
    node1.right = node4

    node2.left = node5
    node2.right = node6

    print is_bst(node0)

    node1.left = node0
    node1.right = node2

    node0.left = None
    node0.right = None
    node2.left = None
    node2.right = None

    print is_bst(node1)

    node4.left = node2
    node4.right = node6
    node2.left = node1
    node2.right = node3
    node1.left = node0
    node1.right = None
    node3.left = None
    node3.right = None
    node6.left = node5
    node6.right = node8
    node8.left = node7
    node8.right = node9
    node5.left = None
    node5.right = None
    node7.left = None
    node7.right = None
    node9.left = None
    node9.right = None

    print is_bst(node4)
