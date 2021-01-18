class UnionFind:
    id = []
    sz = []
    size = 0
    numComponents = 0

    def __init__(self, length):
        if length <= 0:
            raise RuntimeError('Size is not valid')
        self.size = self.numComponents = length
        for i in range(length):
            self.id.append(i)
            self.sz.append(1)

    def find(self, p):
        root = p
        while root != self.id[root]:
            root = self.id[root]
        while p != root:
            next = self.id[p]
            self.id[p] = root
            p = next
        return root

    def unify(self, p, q):
        root1 = self.find(p)
        root2 = self.find(q)
        if root1 == root2:
            return
        if self.sz[root1] < self.sz[root2]:
            self.id[root1] = root2
            self.sz[root2] += self.sz[root1]
        else:
            self.id[root2] = root1
            self.sz[root1] += self.sz[root2]
        self.numComponents -= 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def componentSize(self, p):
        return self.sz[self.find(p)]

    def length(self):
        return self.size

    def components(self):
        return self.numComponents



