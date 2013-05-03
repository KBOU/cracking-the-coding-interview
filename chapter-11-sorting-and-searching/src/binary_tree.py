# coding: utf-8

class Node(object):
    def __init__(self, data):
        self.data = data
        self.__left = None
        self.__right = None

    def put(self, node):
        if node.data <= self.data:
            if self.__left is None:
                self.__left = node
            else:
                self.__left.put(node)
        else:
            if self.__right is None:
                self.__right = node
            else:
                self.__right.put(node)

    def get_cnt(self, data, cnt=0):
        if data < self.data:
            if self.__left is not None:
                return self.__left.get_cnt(data, cnt)
            else:
                return cnt
        elif data > self.data:
            if self.__right is not None:
                return self.nodes_left_count() + 1 + self.__right.get_cnt(data, cnt)
            else:
                return cnt+1
        else:
            return cnt+self.nodes_left_count()


    def nodes_left_count(self):
        left = 0
        if self.__left is not None:
            left = self.__left.nodes_count()
        return left
    def nodes_right_count(self):
        left = 0
        if self.__right is not None:
            left = self.__right.nodes_count()
        return left

    def nodes_count(self):
        left = self.nodes_left_count()
        right = self.nodes_right_count()
        return left + right + 1

ROOT = [None]
def track(num):
    if ROOT[0] is None:
        ROOT[0] = Node(num)
    else:
        ROOT[0].put(Node(num))

def get_rank_of_num(num):
    if ROOT[0] is None:
        return 0
    else:
        return ROOT[0].get_cnt(num)


if __name__ == "__main__":
    arr = [5, 1, 4, 3, 2, 8, 5, 1, 1,]
    for elem in arr:
        track(elem)

    print get_rank_of_num(4)
