class AVL:
    root = None
    nodeCount = 0

    class Node:
        def __init__(self, value):
            self.value = value
            self.bf = None
            self.height = 0
            self.left = None
            self.right = None

    def height(self):
        if self.root is None:
            return 0
        return self.root.height

    def size(self):
        return self.nodeCount

    def isEmpty(self):
        return self.size() == 0

    def contains(self, node, value):
        if node is None:
            return False
        if node.value > value:
            return self.contains(node.left, value)
        if node.value < value:
            return self.contains(node.right, value)
        return True

    def insert(self, value):
        if value is None:
            return False
        if self.contains(self.root, value) is False:
            self.root = self.insertValue(self.root, value)
            self.nodeCount += 1
            return True
        return False

    def insertValue(self, node, value):
        if node is None:
            node = self.Node(value)
            return node
        if node.value > value:
            node.left = self.insertValue(node.left, value)
        else:
            node.right = self.insertValue(node.right, value)
        self.update(node)
        return self.balance(node)

    def update(self, node):
        leftNodeHeight = -1 if node.left is None else node.left.height
        rightNodeHeight = -1 if node.right is None else node.right.height
        node.height = 1 + max(leftNodeHeight, rightNodeHeight)
        node.bf = rightNodeHeight - leftNodeHeight

    def balance(self, node):
        if node.bf == -2:
            if node.left.bf <= 0:
                return self.leftLeftCase(node)
            else:
                return self.leftRightCase(node)
        elif node.bf == 2:
            if node.right.bf >= 0:
                return self.rightRightCase(node)
            else:
                return self.rightLeftCase(node)
        return node

    def leftLeftCase(self, node):
        return self.rightRotation(node)

    def leftRightCase(self, node):
        node.left = self.leftRotation(node.left)
        return self.leftLeftCase(node)

    def rightRightCase(self, node):
        return self.leftRotation(node)

    def rightLeftCase(self, node):
        node.right = self.rightRotation(node.right)
        return self.rightRightCase(node)

    def leftRotation(self, node):
        newParent = node.right
        node.right = newParent.left
        newParent.left = node
        self.update(node)
        self.update(newParent)
        return newParent

    def rightRotation(self, node):
        newParent = node.left
        node.left = newParent.right
        newParent.right = node
        self.update(node)
        self.update(newParent)
        return newParent

    def remove(self, node, elem):
        if node is None or elem is None:
            return False
        if node.value > elem:
            node.left = self.remove(node.left, elem)
        elif node.value < elem:
            node.right = self.remove(node.right, elem)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                if node.left.height > node.right.height:
                    value = self.findMax(node.left)
                    node.value = value
                    node.left = self.remove(node.left, value)
                else:
                    value = self.findMin(node.right)
                    node.value = value
                    node.right = self.remove(node.right, value)
        self.update(node)
        return self.balance(node)

    def findMin(self, node):
        while node.left is not None:
            node = node.left
        return node.value

    def findMax(self, node):
        while node.right is not None:
            node = node.right
        return node.value
