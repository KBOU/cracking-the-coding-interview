
class Stack(object):
    def __init__(self, partition_size):
        self.__arr = [None] * partition_size * 3
        self.__partition_size = partition_size
        self.__partitions = [partition_size, partition_size * 2, partition_size * 3]
        self.__indices = [0, partition_size, partition_size * 2]

    def push(self, partition_id, elem):
        last_id = self.__indices[partition_id]
        if last_id < self.__partitions[partition_id]:
            self.__arr[last_id] = elem
            self.__indices[partition_id] += 1
        else:
            print "this partition is full"


    def pop(self, partition_id, elem):
        last_id = self.__indices[partition_id]
        if last_id > self.__partitions[partition_id] - self.__partition_size:
            self.__indices[partition_id] -= 1
            return self.__arr[last_id-1]
        else:
            print "this partition is empty"

if __name__ == "__main__":
    stack = Stack(3)
    stack.push(1, 1)
    stack.push(1, 1)
    stack.push(1, 1)
    stack.push(1, 1)
    stack.push(1, 1)
    stack.push(1, 1)
    stack.pop(0, 1)
    stack.pop(0, 1)
    stack.pop(0, 1)
    stack.pop(0, 1)
    stack.pop(0, 1)
