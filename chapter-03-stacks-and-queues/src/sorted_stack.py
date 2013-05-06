class Stack(object):
    def __init__(self):
        self.__stack = []
    def push(self, elem):
        self.__stack.append(elem)
    def pop(self):
        if len(self.__stack) == 0:
            return None
        return self.__stack.pop()
    def peek(self):
        if len(self.__stack) == 0:
            return None
        return self.__stack[len(self.__stack)-1]

    def __str__(self):
        return self.__stack.__str__()

class SortedStack(object):
    def __init__(self):
        self.__stack = Stack()
        self.__buffer = Stack()

    def push(self, elem):
        self.__pop_to_elem_less_than(elem)
        self.__stack.push(elem)
        self.__reset_stack()

    def pop(self):
        return self.__stack.pop()

    def __pop_to_elem_less_than(self, elem):
        while self.__stack.peek is not None and elem < self.__stack.peek():
            self.__buffer.push(self.__stack.pop())

    def __reset_stack(self):
        elem = self.__buffer.pop()
        while elem is not None:
            self.__stack.push(elem)
            elem = self.__buffer.pop()

    def __str__(self):
        return self.__stack.__str__()

if __name__ == "__main__":
    stack = SortedStack()
    stack.push(3)
    stack.push(4)
    stack.push(2)
    print stack

    stack.push(5)
    stack.push(3)
    print stack

    stack.pop()
    stack.pop()
    stack.pop()
    print stack

    stack.push(1)
    stack.push(5)
    print stack
