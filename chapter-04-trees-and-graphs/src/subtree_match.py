# coding: utf-8

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def __str__(self):
        return "Node(" + str(self.value) + ")"


def match_completely(node1, node2):
    if node1.left is None and node2.left is not None:
        return False
    elif node1.left is not None and node2.left is None:
        return False

    if node1.right is None and node2.right is not None:
        return False
    elif node1.right is not None and node2.right is None:
        return False

    if (node1.left is None and node2.left is None) or node1.left.value == node2.left.value:
        if (node1.right is None and node2.right is None) or node1.right.value == node2.right.value:

            if node1.left is None and node2.left is None:
                left_match = True
            else:
                left_match = match_completely(node1.left, node2.left)
            if node1.right is None and node2.right is None:
                right_match = True
            else:
                right_match = match_completely(node1.right, node2.right)
            if left_match and right_match:
                return True
    return False

def match_subtree(node1, node2):
    if node1 is None or node2 is None:
        return False
    if node1.value == node2.value:
        if match_completely(node1, node2):
            return True

    left_match = match_subtree(node1.left, node2)
    if left_match:
        return True

    right_match = match_subtree(node1.right, node2)
    if right_match:
        return True

    return False


if __name__ == "__main__":
    node1_1 = Node(1)
    node1_2 = Node(2)
    node1_3 = Node(3)
    node1_4 = Node(4)
    node1_5 = Node(5)

    node1_1.left = node1_2
    node1_1.right = node1_3
    node1_2.left = node1_4
    node1_2.right = node1_5

    node2_2 = Node(1)
    node2_4 = Node(2)
    node2_5 = Node(3)

    node2_2.left = node2_4
    node2_2.right = node2_5

    print match_subtree(node1_1, node2_2)
