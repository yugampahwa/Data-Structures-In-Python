class DynamicArray:
    """
    Constructor:-

    """

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.array(self.capacity)

    """
    len function always go to this function so we can improvise the len function
    """

    def __len__(self):
        return self.n

    """
    Accessing data elements and returning error if out of bounds
    """

    def __getitem__(self, item):
        if item not in range(0, self.n):
            return IndexError("Out of bounds!!!")
        return self.A[item]

    """
    Insertion Function
    """

    def insert(self, item, index):
        if 0 > index or index > self.n:
            print('Out of Bound')
            return
        if self.n == self.capacity:
            self.Resize(2 * self.capacity)

        for i in range(self.n - 1, index - 1, -1):
            self.A[i + 1] = self.A[i]
        self.A[index] = item
        self.n += 1

    """
    Append Function
    """

    def append(self, item):
        if self.n == self.capacity:
            self.Resize(2 * self.capacity)
        self.A[self.n] = item
        self.n += 1

    """
    Resize Function
    """

    def Resize(self, cap):
        temp = self.array(cap)
        for i in range(self.n):
            temp[i] = self.A[i]
        self.A = temp
        self.capacity = cap

    """
    Array making function
    """

    def array(self, cap):
        return [None] * cap

    """
    Delete Function
    """

    def delete(self):
        if self.n == 0:
            print('array is empty!!')
            return
        self.A[self.n - 1] = None
        self.n -= 1

    """
    remove Function
    """

    def remove(self, index):
        if self.n == 0:
            print('No element to delete ')
            return
        if 0 > index or index > self.n - 1:
            print("Out of bound")
            return
        if index == self.n - 1:
            self.A[index] = None
            self.n -= 1
            return
        for i in range(index, self.n - 1):
            self.A[i] = self.A[i + 1]
        self.A[self.n - 1] = None
        self.n -= 1

    """
    Clear Function
    """
    def clear(self):
        if self.n == 0:
            return
        for i in range(self.n):
            self.A[i] = None
        self.n = 0

arr=DynamicArray()
arr.append(1)
arr.append(1)
arr.append(1)
arr.append(1)
arr.clear()
print(arr.A)