import random


class Node:
    def __init__(self, data):
        self._data = data
        self._nextNode = None

    @property
    def data(self):
        return self._data

    @property
    def nextNode(self):
        return self._nextNode

    @nextNode.setter
    def nextNode(self, value):
        self._nextNode = value


class LinkedList:
    def __init__(self):
        self._rootNode = None

    def insert(self, data):
        tmp = Node(data)
        if self._rootNode == None:
            self._rootNode = tmp
            return
        v = self._rootNode
        while v.nextNode != None:
            v = v.nextNode
        v.nextNode = tmp

    def dump(self):
        if self._rootNode == None:
            return
        v = self._rootNode
        while v != None:
            print(v.data)
            v = v.nextNode

    def delete(self, data):
        if self._rootNode == None:
            return
        if self._rootNode.data == data:
            self._rootNode = self._rootNode.nextNode
            return
        v1 = self._rootNode
        v2 = v1.nextNode
        while v2 != None:
            if v2.data == data:
                v1.nextNode = v2.nextNode
                return
            v1 = v2
            v2 = v2.nextNode

    def find_mid(self):
        if self._rootNode == None:
            print("LinkedList boştur.")
            return
        slowptr = self._rootNode
        fastptr = self._rootNode
        while fastptr != None:
            if fastptr.nextNode == None:
                print("Linkedlist Ortadaki Eleman : {0}".format(slowptr.data))
                return
            slowptr = slowptr.nextNode
            fastptr = fastptr.nextNode.nextNode
        print("Linkedlist Ortadaki Eleman : {0}".format(slowptr.data))


if __name__ == "__main__":
    print("--" * 10)
    a = LinkedList()
    a.insert(5)
    a.insert(10)
    a.insert(15)
    a.insert(20)
    a.insert(25)
    a.insert(30)
    a.insert(35)
    a.dump()
    print("--" * 10)
    a.find_mid()
    print("--" * 10)
    b = LinkedList()
    x = random.randint(1, 100)
    print("Oluşturulan random linkedlist", x, "Elemanlıdır.")
    for i in range(x):
        b.insert(random.randint(1, 100))
    b.dump()
    print("--" * 10)
    b.find_mid()
    print("--" * 10)
