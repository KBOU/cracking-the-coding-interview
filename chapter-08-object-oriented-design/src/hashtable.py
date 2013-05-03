class LinkedList(object):
    def __init__(self, contents=None):
        self.contents = contents
        self.next = None
        self.prev = None
    def destroy(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev



class HashTable(object):
    def __init__(self):
        self.table = {}

    def update(self, key, value):
        l_list = self.__search_table(key)
        l_list = self.__search_list(key, l_list)

        l_list.contents = [key, value]

    def delete(self, key):
        l_list = self.__search_table(key)
        l_list = self.__search_list(key, l_list)
        l_list.destroy()

    def search(self, key):
        l_list = self.__search_table(key)
        l_list = self.__search_list(key, l_list)
        if l_list.contents is None:
            l_list.destroy()
            return None
        else:
            return l_list.contents[1]

    def __hashing(self, key):
        return key[0:1]

    def __search_table(self, key):
        return self.table.get(self.__hashing(key))

    def __search_list(self, key, l_list):
        head = l_list
        while l_list is not None:
            k = l_list.contents[0]
            if k is key:
                break
            l_list = l_list.next
        if l_list is None:
            l_list = LinkedList()
            l_list.prev = head
            if head is not None:
                head.next = l_list
            else:
                self.table[self.__hashing(key)] = l_list

        return l_list

if __name__ == "__main__":
    ht = HashTable()
    ht.update('hgoe', 'fube')
    ht.update('hf', 'bbbb')
    ht.update('fff', 'aaaaa')
