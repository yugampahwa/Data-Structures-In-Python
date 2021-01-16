class Stack:
    stack = []

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return self.size() == 0

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        if self.isEmpty():
            raise RuntimeError('Empty Stack!!!')
        data = self.stack[len(self.stack) - 1]
        self.stack = self.stack[:len(self.stack) - 1]
        print("Dropped :", data)

    def peek(self):
        if self.isEmpty():
            raise RuntimeError("Empty Stack!!!")
        data = self.stack[len(self.stack) - 1]
        print("peek element:",data)

    def printStack(self):
        for x in self.stack:
            print(x)
