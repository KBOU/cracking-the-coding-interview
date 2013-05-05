class Stack(object):
    def __init__(self, size):
        self.__index = 0
        self.__stack = [None] * size

    def push(self, elem):
        self.__stack[self.__index] = elem
        self.__index += 1

    def pop(self):
        elem = self.__stack[self.__index-1]
        self.__index -= 1
        return elem

    def peek(self):
        return self.__stack[self.__index-1]

class StackWithMin(Stack):
    def __init__(self, size):
        super(StackWithMin, self).__init__(size)
        self.__min_stack = Stack(size)

    def push(self, elem):
        super(StackWithMin, self).push(elem)
        minval = self.__min_stack.peek()
        if minval is None or elem <= minval:
            self.__min_stack.push(elem)

    def pop(self):
        elem = super(StackWithMin, self).pop()
        minval = self.__min_stack.peek()
        if elem == minval:
            self.__min_stack.pop()
        return elem

    def min(self):
        return self.__min_stack.peek()

if __name__ == "__main__":
    stack = StackWithMin(20)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print stack.pop(), stack.min()
    print stack.pop(), stack.min()
    print stack.pop(), stack.min()
    print stack.pop(), stack.min()
    print stack.pop(), stack.min()
    print stack.pop(), stack.min()
    print stack.pop(), stack.min()
    print stack.pop(), stack.min()
    print stack.pop(), stack.min()
    print stack.pop(), stack.min()
    print stack.pop(), stack.min()
