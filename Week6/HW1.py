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

    def find_cycle(self):
        if self._rootNode == None:
            return
        slowptr = self._rootNode
        fastptr = self._rootNode
        while fastptr != None:
            slowptr = slowptr.nextNode
            fastptr = slowptr.nextNode.nextNode
            if fastptr == None:
                print("Cycle Yoktur..")
                return
            if fastptr.nextNode == slowptr or fastptr != None:
                print("Cycle Vardır..")
                return

    def do_cycle(self):
        rtnode = self._rootNode
        counter = 0
        while rtnode != None:
            prevNode = rtnode
            rtnode = rtnode.nextNode
            counter = counter + 1
        rnd = random.randint(0, counter)
        rtnode = self._rootNode
        for i in range(0, rnd):
            rtnode = rtnode.nextNode
        prevNode.nextNode = rtnode


if __name__ == "__main__":
    x = LinkedList()
    x.insert(5)
    x.insert(10)
    x.insert(15)
    x.insert(20)
    x.insert(25)
    x.insert(30)
    x.insert(35)
    x.do_cycle()
    x.find_cycle()
