import math


class HashTable:

    def __init__(self, capacity, loadFactor):
        if capacity <= 0 or math.isnan(capacity) or math.isinf(capacity):
            raise ValueError("Correct your capacity")
        if loadFactor <= 0 or math.isnan(loadFactor) or math.isinf(loadFactor):
            raise ValueError("Correct your loadFactor")
        self.loadFactor = loadFactor
        self.capacity = self.adjustCapacity(capacity)
        self.threshold = self.capacity * self.loadFactor
        self.keys = [None for i in range(self.capacity)]
        self.values = [None for i in range(self.capacity)]
        self.usedBuckets = 0
        self.keyCount = 0

    def adjustCapacity(self, capacity):
        while self.gcd(19, capacity) != 1:
            capacity += 1
        return capacity

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def insert(self, key, val):
        if key is None:
            raise ValueError("Key is None")
        if self.usedBuckets >= self.threshold:
            self.resizeTable()
        offset = self.normalizeIndex(hash(key))
        j = -1
        x = 0
        node = offset
        while True:
            if self.keys[node] == "T":
                j = node
                x = x + 1
                node = self.normalizeIndex(offset + self.probe(x))
            elif self.keys[node] is not None:
                if self.keys[node] is key:
                    oldValue = self.values[node]
                    if j == -1:
                        self.values[node] = val
                    else:
                        self.keys[node] = "T"
                        self.values[node] = None
                        self.keys[j] = key
                        self.values[j] = val
                    return "Updated value  " + str(oldValue) + " to " + str(val)
                x = x + 1
                node = self.normalizeIndex(offset + self.probe(x))
            else:
                if j == -1:
                    self.usedBuckets += 1
                    self.keyCount += 1
                    self.keys[node] = key
                    self.values[node] = val
                else:
                    self.keyCount += 1
                    self.keys[j] = key
                    self.values[j] = val
                return "Inserted Successfully"

    def probe(self, x):
        return 19 * x

    def normalizeIndex(self, keyHash):
        return abs(int(keyHash)) % self.capacity

    def resizeTable(self):
        capacity = 2 * self.capacity + 1
        self.capacity = self.adjustCapacity(capacity)
        self.threshold = self.capacity * self.loadFactor
        newKeys = [None for i in range(self.capacity)]
        newValues = [None for i in range(self.capacity)]
        temp = self.keys
        self.keys = newKeys
        newKeys = temp
        temp = self.values
        self.values = newValues
        newValues = temp
        self.keyCount = self.usedBuckets = 0
        for i in range(len(newKeys)):
            if newKeys[i] is not None and newKeys[i] != "T":
                self.insert(newKeys[i], newValues[i])
            newKeys[i] = None
            newValues[i] = None

    def remove(self, key):
        if key is None:
            raise ValueError("key is Null!!!")
        offset = self.normalizeIndex(hash(key))
        node = offset
        x = 0
        while True:
            if self.keys[node] == "T":
                x += 1
                node = self.normalizeIndex(offset + self.probe(x))
            elif self.keys[node] is None:
                return "Not Found"
            else:
                if self.keys[node] is key:
                    self.keyCount -= 1
                    oldValue = self.values[node]
                    self.keys[node] = "T"
                    self.values[node] = None
                    return "Removed" + str(oldValue)
                else:
                    x += 1
                    node = self.normalizeIndex(offset + self.probe(x))

    def get(self, key):
        if key is None:
            raise ValueError("key is Null")
        offset = self.normalizeIndex(hash(key))
        node = offset
        j = -1
        x = 0
        while True:
            if self.keys[node] == "T":
                if j == -1:
                    j = node
                x += 1
                node = self.normalizeIndex(offset + self.probe(x))
            elif self.keys[node] is not None:
                if self.keys[node] is key:
                    if j != -1:
                        self.keys[j] = self.keys[node]
                        self.values[j] = self.values[node]
                        self.keys[node] = "T"
                        self.values[node] = None
                        return self.values[j]
                    else:
                        return self.values[node]
                x += 1
                node = self.normalizeIndex(offset + self.probe(x))
            else:
                return "Key Not Found!!!"

    def hasKey(self, key):
        if key is None:
            raise ValueError("key is Null!!!")
        offset = self.normalizeIndex(hash(key))
        node = offset
        j = -1
        x = 0
        while True:
            if self.keys[node] == "T":
                if j == -1:
                    j = node
                x += 1
                node = self.normalizeIndex(offset + self.probe(x))
            elif self.keys[node] is not None:
                if self.keys[node] is key:
                    if j != -1:
                        self.keys[j] = self.keys[node]
                        self.values[j] = self.values[node]
                        self.keys[node] = "T"
                        self.values[node] = None
                    return True
                x += 1
                node = self.normalizeIndex(offset + self.probe(x))
            else:
                return False

    def clear(self):
        for i in range(self.capacity):
            self.keys[i] = None
            self.values[i] = None
        self.keyCount = 0
        self.usedBuckets = 0

    def Size(self):
        return self.keyCount

    def getCapacity(self):
        return self.capacity

    def isEmpty(self):
        return self.keyCount == 0

    def Keys(self):
        hashableKeys = []
        for i in range(self.capacity):
            if self.keys[i] is not None and self.keys != "T":
                hashableKeys.append(self.keys[i])
        return hashableKeys

    def Values(self):
        ValueList = []
        for i in range(self.capacity):
            if self.values[i] is not None and self.values[i] != "T":
                ValueList.append(self.values[i])
        return ValueList

    def printHashTable(self):
        print("{", end=" ")
        for i in range(self.capacity):
            if self.keys[i] is not None and self.keys[i] != "T":
                print(self.keys[i], " => ", self.values[i], end=" , ")
        print("}")
