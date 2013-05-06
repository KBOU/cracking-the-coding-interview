# coding: utf-8

class LinkedNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def setnext(self, elem):
        tmp = self
        while tmp.next is not None:
            tmp = tmp.next
        tmp.next = elem
        elem.prev = tmp

    def __str__(self):
        tmp = self
        string = "[" 
        while tmp is not None:
            string += tmp.data.__str__() + ","
            tmp = tmp.next
        string += "]" 
        return string

class Animal(object):
    def talk(self):
        pass

class Cat(Animal):
    cat_id = 0
    def __init__(self):
        Cat.cat_id += 1
        self.cat_id = Cat.cat_id
    def talk(self):
        print "にゃー"
    def __str__(self):
        return "Cat(" + str(self.cat_id) + ")"
class Dog(Animal):
    dog_id = 0
    def __init__(self):
        Dog.dog_id += 1
        self.dog_id = Dog.dog_id
    def talk(self):
        print "わん"
    def __str__(self):
        return "Dog(" + str(self.dog_id) + ")"


class AnimalShelter(object):
    def __init__(self):
        self.__queue = None

    def enqueue(self, animal):
        if self.__queue is None:
            self.__queue = LinkedNode(animal)
        else:
            elem = LinkedNode(animal)
            self.__queue.setnext(elem)

    def dequeue_any(self):
        head = self.__queue
        if head is None:
            return None

        nxt = head.next
        if nxt is not None:
            nxt.prev = None
        head.next = None
        self.__queue = nxt
        head.data.talk()
        return head.data

    def dequeue_dog(self):
        head = self.__queue
        while head is not None:
            if isinstance(head.data, Dog):
                break
            head = head.next
        if head is not None:
            self.__finalize_list(head)
            head.data.talk()
            return head.data
        else:
            return None
    def dequeue_cat(self):
        head = self.__queue
        while head is not None:
            if isinstance(head.data, Cat):
                break
            head = head.next
        if head is not None:
            self.__finalize_list(head)
            head.data.talk()
            return head.data
        else:
            return None

    def __finalize_list(self, head):
        nxt = head.next
        prv = head.prev
        if nxt is not None:
            nxt.prev = prv
        if prv is not None:
            prv.next = nxt

        head.next = None
        head.prev = None
        if head == self.__queue:
            self.__queue = nxt

    def __str__(self):
        return self.__queue.__str__()


if __name__ == "__main__":
    import time
    import random
    shelter = AnimalShelter()

    while True:
        rand = random.randint(0, 100)
        if rand < 67:
            if rand < 34:
                shelter.enqueue(Cat())
            else:
                shelter.enqueue(Dog())
        else:
            if rand < 78:
                shelter.dequeue_dog()
            elif rand < 89:
                shelter.dequeue_cat()
            else:
                shelter.dequeue_any()
        print shelter
        time.sleep(1)
