class BinarySearchTree:
    nodeCount = 0
    root = None

    class Node:
        def __init__(self, right=None, left=None, data=None):
            self.right = right
            self.left = left
            self.data = data

    def isEmpty(self):
        return self.nodeCount == 0

    def size(self):
        return self.nodeCount

    def add(self, node, element):
        if self.contain(node, element):
            return
        if node is None:
            if self.root is None:
                self.root = self.Node(data=element)
                self.nodeCount += 1
            else:
                new_node = self.Node(data=element)
                self.nodeCount += 1
                return new_node
        elif node.data < element:
            node.right = self.add(node.right, element)
        else:
            node.left = self.add(node.left, element)
        return node

    def contain(self, node, element):
        if node is None:
            return False
        if node.data < element:
            return self.contain(node.right, element)
        elif node.data > element:
            return self.contain(node.left, element)
        else:
            return True

    def callRemove(self, node, element):
        if self.contain(node, element):
            self.nodeCount -= 1
            self.remove(node, element)

        else:
            print("Element is not present in binary search tree")

    def remove(self, node, element):
        if node is None:
            return None

        if node.data > element:
            node.left = self.remove(node.left, element)
        elif node.data < element:
            node.right = self.remove(node.right, element)
        else:
            if node.left is None:
                tmp = node.right
                node.data = None
                node = None
                return tmp
            elif node.right is None:
                tmp = node.left
                node.data = None
                node = None
                return tmp
            else:
                tmp = self.findMin(node.right)
                node.data = tmp.data
                node.right = self.remove(node.right, tmp.data)
        return node

    def findMin(self, node):
        while node.left is not None:
            node = node.left
        return node

    def height(self, node):
        if node is None:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1

    def preorder(self, node):
        if node is None:
            return
        print(node.data, ",")
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data, ",")
        self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data, ",")

    def levelorder(self, node):
        h = self.height(node)
        for i in range(1, h + 1):
            self.printLevel(node, i)

    def printLevel(self, node, level):
        if node is None:
            return
        if level == 1:
            print(node.data, ",")
        else:
            self.printLevel(node.left, level - 1)
            self.printLevel(node.right, level - 1)
