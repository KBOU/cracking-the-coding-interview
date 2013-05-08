class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def add_tail(self, node):
        if self.head is None:
            self.head = LinkedList.LinkedNode(node)
            self.tail = self.head
        else:
            self.tail.next = LinkedList.LinkedNode(node)
            self.tail = self.tail.next

    def __str__(self):
        string = "["
        n = self.head
        while n is not None:
            string += n.__str__() + ", "
            n = n.next
        string += "]"
        return string

    class LinkedNode(object):
        def __init__(self, node):
            self.node = node
            self.next = None

        def __str__(self):
            return "LinkedNode(" + str(self.node.data) + ")"

SKEWERS = []

def depth_search(root, level=0):
    if len(SKEWERS) <= level:
        skewer = LinkedList()
        SKEWERS.append(skewer)
    else:
        skewer = SKEWERS[level]

    skewer.add_tail(root)

    for child in root.children:
        depth_search(child, level + 1)

if __name__ == "__main__":
    root = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    root.children.append(node1)
    root.children.append(node2)
    node2.children.append(node3)
    node1.children.append(node4)
    node2.children.append(node5)

    depth_search(root)
    for skewer in SKEWERS:
        print skewer
