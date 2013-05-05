# coding: utf-8
class Stack(object):
    def __init__(self, size):
        self.__stack = [None] * size
        self.__index = -1

    def push(self, elem):
        if self.__index == len(self.__stack) -1:
            raise Exception("stack is full")
        self.__index += 1
        self.__stack[self.__index] = elem

    def pop(self):
        if self.__index < 0:
            raise Exception("stack is empty")
        elem = self.__stack[self.__index]
        self.__index -= 1
        return elem

    def __str__(self):
        return self.__stack.__str__()

class StackSet(object):
    def __init__(self):
        self.__stacks = []
        self.__stack_index = 0
        self.__stacks.append(Stack(10))

    def push(self, elem):
        try:
            self.__stacks[self.__stack_index].push(elem)
        except Exception, msg:
            print msg
            self.__stack_index += 1
            if self.__stack_index >= len(self.__stacks):
                self.__stacks.append(Stack(10))
            self.__stacks[self.__stack_index].push(elem)

    def pop(self):
        try:
            elem = self.__stacks[self.__stack_index].pop()
            return elem
        except Exception, msg:
            print msg
            if self.__stack_index == 0:
                return None
            self.__stack_index -= 1
            if self.__stack_index < len(self.__stacks) - 2:
                self.__stacks.pop()

            elem = self.__stacks[self.__stack_index].pop()
            return  elem

    def pop_at(self, index):
        try:
            if index <= self.__stack_index:
                return self.__stacks[index].pop()
            else:
                return None
        except Exception:
            return None

    def __str__(self):
        string = "["
        for stack in self.__stacks:
            string += stack.__str__() + ", "
        string += "]"
        return string

if __name__ == "__main__":
    import time
    import random

    choice = (True, True, True, False, False)
    stack = StackSet()
    while True:
        if random.choice(choice):
            stack.push(random.randint(0, 10))
        else:
            print "poped", stack.pop()
        print stack
        time.sleep(1)
