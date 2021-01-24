class HashTable:
    size = 0
    capacity = 0
    hashTable = None

    def __init__(self):
        self.initial()

    def initial(self):
        self.capacity = int(input("Enter capacity for hash table"))
        self.hashTable = [[] for _ in range(self.capacity)]

    def initial1(self, capacity):
        self.hashTable = [[] for _ in range(self.capacity)]

    def Size(self):
        return self.size

    def isEmpty(self):
        return self.Size() == 0

    def normaliseIndex(self, keyHash):
        keyHash = abs(hash(keyHash)) % self.capacity
        return keyHash

    def clean(self):
        self.hashTable.clear()
        output = input("Type yes to make new hash table and Type no for hash table with existing capacity ")
        if output.lower() == "yes":
            self.initial()
        else:
            print("Hash table is cleared and formed with previous capacity ")
            self.initial1(self.capacity)

    def insert(self, value):
        if value is None:
            raise RuntimeError("Value is Null")
        if self.hasValue(value):
            print("Value is already there")
            return
        key = self.normaliseIndex(hash(value))
        self.hashTable[key].append(value)
        self.size += 1
        print("Successfully Inserted")

    def hasValue(self, value):
        if value is None:
            raise RuntimeError("Value is None")
        key = self.normaliseIndex(hash(value))
        for i in self.hashTable[key]:
            if i is value:
                return True
        return False

    def remove(self, value):
        if value is None:
            raise RuntimeError("Value is none")
        if self.hasValue(value):
            key = self.normaliseIndex(hash(value))
            self.hashTable[key].remove(value)
            self.size -= 1
        else:
            print("Value is not present in hash table")

    def printHashMap(self):
        for i, j in enumerate(self.hashTable):
            print(i, end="->")
            for q in j:
                print(q, end="->")
            print()
