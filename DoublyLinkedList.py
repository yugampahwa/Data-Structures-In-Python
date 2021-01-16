class DoublyLinkedList:
    head = None
    tail = None
    size = 0

    class Node:
        def __init__(self, data=None, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

    def clear(self):
        if self.isEmpty():
            print("Its already empty")
        else:
            trav = self.head
            while trav is not None:
                new = trav.next
                trav.next = trav.prev = None
                trav.data = None
                trav = new
            self.head = self.tail = None
            self.size = 0

    def length(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def add(self, new_data):
        if self.isEmpty():
            self.head = self.tail = self.Node(data=new_data)
        else:
            self.tail.next = self.Node(new_data, self.tail, None)
            self.tail = self.tail.next
        self.size += 1

    def addFirst(self, new_data):
        if self.isEmpty():
            self.head = self.tail = self.Node(data=new_data)
        else:
            self.head.prev = self.Node(new_data, None, self.head)
            self.head = self.head.prev
        self.size += 1

    def peekFirst(self):
        if self.isEmpty():
            raise RuntimeError("Empty List")
        return self.head.data

    def peekLast(self):
        if self.isEmpty():
            raise RuntimeError("Empty List")
        return self.tail.data

    def removeFirst(self):
        if self.isEmpty():
            raise RuntimeError("Empty List")
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.isEmpty():
            self.tail = None
        else:
            self.head.prev = None
        return data

    def removeLast(self):
        if self.isEmpty():
            raise RuntimeError("Empty List")
        data = self.tail.data
        self.tail = self.tail.prev
        self.size -= 1
        if self.isEmpty():
            self.head = None
        else:
            self.tail.next = None
        return data

    def remove(self, obj):
        if obj.prev is None:
            return self.removeFirst()
        if obj.next is None:
            return self.removeLast()
        obj.next.prev = obj.prev
        obj.prev.next = obj.next
        data = obj.data
        obj.prev = obj.next = None
        obj.data = None
        obj = None
        self.size -= 1
        return data

    def removeAt(self, index):
        if index < 0 or index > self.size:
            raise RuntimeError("Index is out of bounds!!!")
        if index < self.size / 2:
            trav = self.head
            i = 0
            while i is not index:
                trav = trav.next
                i += 1
        else:
            trav = self.tail
            i = self.size - 1
            while i is not index:
                trav = trav.prev
                i -= 1
        return self.remove(trav)

    def isRemove(self, obj):
        trav = self.head
        while trav is not None:
            if trav.data is obj:
                self.remove(trav)
                return True
            trav = trav.next

        return False

    def indexOf(self, obj):
        index = 0
        trav = self.head
        while trav is not None:
            if trav.data is obj:
                return index
            index += 1
            trav = trav.next
        return -1

    def contain(self, obj):
        return self.indexOf(obj) != -1

    def printDLL(self):
        data = "["
        trav = self.head
        while trav is not None:
            data = data + str(trav.data) + ","
            trav = trav.next
        data = data + "]"
        print(data)
