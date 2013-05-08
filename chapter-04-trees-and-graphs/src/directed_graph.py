class Queue(object):
    def __init__(self):
        self.__queue = []

    def enqueue(self, elem):
        self.__queue.append(elem)

    def dequeue(self):
        return self.__queue.pop(0)

    def is_empty(self):
        return len(self.__queue) == 0

class Node(object):
    def __init__(self, data):
        self.data = data
        self.tos = []
        self.visited = False

    def __str__(self):
        return "Node(" + str(self.data) + ")"

def is_route(nodes, a, b):
    q = Queue()
    q.enqueue(a)
    found = False

    for n in nodes:
        n.visited = False

    while not q.is_empty():
        node = q.dequeue()
        print node
        if node.visited:
            continue
        node.visited = True

        if b is node:
            found = True
            break
        for to in node.tos:
            q.enqueue(to)
    return found


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)
    nodes = (node1, node2, node3, node4, node5, node6, node7, node8, node9)

    node1.tos.append(node2)
    node1.tos.append(node3)
    node2.tos.append(node5)
    node3.tos.append(node8)
    node4.tos.append(node5)
    node9.tos.append(node7)
    print is_route(nodes, node1, node9)
    node5.tos.append(node9)
    print is_route(nodes, node1, node2)
