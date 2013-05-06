class Stack(object):
    def __init__(self):
        self.__stack = []

    def push(self, elem):
        self.__stack.append(elem)
    def pop(self):
        if len(self.__stack) == 0:
            return None
        return self.__stack.pop()

    def size(self):
        return len(self.__stack)

class Queue(object):
    def __init__(self):
        self.__in_stack = Stack()
        self.__out_stack = Stack()

    def push(self, elem):
        while self.__out_stack.size() > 0:
            self.__in_stack.push(self.__out_stack.pop())
        self.__in_stack.push(elem)
    def shift(self):
        while self.__in_stack.size() > 0:
            self.__out_stack.push(self.__in_stack.pop())
        return self.__out_stack.pop()


if __name__ == "__main__":
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    print q.shift()
    print q.shift()
    q.push(4)
    q.push(5)
    print q.shift()
    print q.shift()
    print q.shift()
    print q.shift()
