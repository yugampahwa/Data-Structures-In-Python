class FenwickTree:
    tree = []
    N = 0

    def __init__(self, values):
        if values is None:
            raise ValueError("Values is Null!!!")
        values.insert(0, 0)
        self.N = len(values)
        self.tree = [None] * self.N
        self.tree = values
        for i in range(1, self.N):
            parent = i + self.lsb(i)
            if parent < self.N:
                self.tree[parent] += self.tree[i]

    def lsb(self, value):
        return value & -value

    def prefixSum(self, i):
        sum = 0
        while i != 0:
            sum += self.tree[i]
            i -= self.lsb(i)
        return sum

    def sum(self, left, right):
        if right < left:
            raise ValueError("Right should be greater or equal than left")
        return self.prefixSum(right) - self.prefixSum(left - 1)

    def get(self, i):
        return self.sum(i, i)

    def add(self, i, v):
        while i < self.N:
            self.tree[i] += v
            i += self.lsb(i)

    def set(self, i, v):
        self.add(i, v - self.sum(i, i))
