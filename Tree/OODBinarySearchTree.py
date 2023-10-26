class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        if (self.root == None):
            self.root = node
            return
        prev = None
        temp = self.root
        while (temp != None):
            if (temp.data > data):
                prev = temp
                temp = temp.left
            elif(temp.data < data):
                prev = temp
                temp = temp.right
        if (prev.data > data):
            prev.left = node
        else:
            prev.right = node

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


inp = [int(i) for i in input('Enter Input : ').split()]
T = BST()
for i in inp:
    T.insert(i)
T.printTree(T.root)