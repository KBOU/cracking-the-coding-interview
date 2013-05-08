# coding: utf-8

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def set_left(self, node):
        self.left = node
        node.parent = self
    def set_right(self, node):
        self.right = node
        node.parent = self

def find_next_node(node):
    # 親要素を遡ってく
    if node.right is None:
        tmp = node
        node_next = tmp.parent
        while node_next is not None and node_next.left is not tmp:
            tmp = node_next
            node_next = tmp.parent
        return node_next

    # 右側サブツリーの左下の要素を探ってく
    node_next = node.right
    while node_next.left is not None:
        node_next = node_next.left

    return node_next

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

    node4.set_left(node2)
    node2.set_left(node1)
    node2.set_right(node3)
    node1.set_left(node0)

    node4.set_right(node6)
    node6.set_left(node5)
    node6.set_right(node7)
    node7.set_right(node8)

    n = find_next_node(node3)
    if n is not None:
        print n.data
