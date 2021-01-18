class Heap:
    heap = []
    heapSize = 0

    def add(self, element):
        self.heap.append(element)
        self.swim(self.heapSize)
        self.heapSize += 1

    def addArray(self, elementArr):
        self.heap = elementArr
        self.heapSize = len(elementArr)
        for i in range(max(0, int((self.heapSize - 1) / 2)), -1, -1):
            self.sink(i)

    def sink(self, element):
        while True:
            left = element * 2 + 1
            right = element * 2 + 2
            smallest = left
            if right < self.heapSize and self.less(right, left):
                smallest = right
            if left >= self.heapSize or self.less(element, smallest):
                break
            self.swap(element, smallest)
            element = smallest

    def swim(self, element):
        parent = int((element - 1) / 2)
        while element > 0 and self.less(element, parent):
            self.swap(parent, element)
            element = parent
            parent = int((element - 1) / 2)

    def less(self, i, j):
        if self.heap[j] > self.heap[i]:
            return True
        else:
            return False

    def swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def isEmpty(self):
        return self.heapSize == 0

    def clear(self):
        self.heap = []
        self.heapSize = 0

    def size(self):
        return self.heapSize

    def peek(self):
        if self.isEmpty():
            return None
        return self.heap[0]

    def poll(self):
        return self.removeAt(0)

    def removeAt(self, index):
        if self.isEmpty():
            return None
        self.heapSize -= 1
        data = self.heap[index]
        self.swap(index, self.heapSize)
        self.heap[self.heapSize] = None
        if index == self.heapSize:
            return data
        element = self.heap[index]
        self.sink(index)
        if self.heap[index] is element:
            self.swim(index)
        return data

    def remove(self, element):
        for i in range(self.heapSize):
            if element is self.heap[i]:
                self.removeAt(i)
                return True
        return False

    def printHeap(self):
        print(self.heap)
