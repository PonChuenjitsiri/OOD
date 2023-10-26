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

    def checkpos(self, node):
        if not self.root:
            return
        queue = []
        queue.append(self.root)
        while len(queue):
            root = queue.pop(0)
            if root.data == node:
                if root == self.root:
                    return print("Root")
                elif root.left is not None or root.right is not None:
                    return print("Inner")
                elif root.right is None and root.left is None:
                    return print("Leaf")
                
            if root.left is not None:
                queue.append(root.left)
            
            if root.right is not None:
                queue.append(root.right)
        return print("Not exist")

inp = [int(i) for i in input('Enter Input : ').split()]
T = BST()
for i in range(1, len(inp)):
    root = T.insert(inp[i])
root = T
T.printTree(root.root)
T.checkpos(inp[0])