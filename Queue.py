class Queue:
    head = None
    tail = None
    size = 0

    class Node:
        def __init__(self, prev=None, next=None, data=None):
            self.prev = prev
            self.next = next
            self.data = data

    def enqueue(self, new_data):
        if self.head is None:
            self.head = self.tail = self.Node(data=new_data)
            self.size += 1
        else:
            node = self.Node(data=new_data)
            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node
            self.size += 1

    def length(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            raise RuntimeError("Empty Queue")
        print("Peek element:", self.head.data)

    def dequeue(self):
        if self.head is None:
            raise RuntimeError("Empty Queue")
        data = self.head.data
        if self.size == 1:
            self.head = self.tail = None
            print("Popped element:", data)
            self.size -= 1
        else:
            new_node = self.head.next
            self.head.prev = self.head.next = None
            self.head = None
            self.head = new_node
            self.head.prev = None
            print("popped element:", data)
            self.size -= 1

    def printQueue(self):
        if self.isEmpty():
            raise RuntimeError("Empty Queue")
        trav = self.head
        data = "["
        while trav is not None:
            data = data + str(trav.data) + ","
            trav = trav.next
        data = data + "]"
        print(data)
