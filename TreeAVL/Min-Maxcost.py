class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class AVL():
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insertAVL(self.root, data)

    def insertAVL(self, rootNode, data):
        if not rootNode:
            return Node(data)
        if data < rootNode.data:
            rootNode.left = self.insertAVL(rootNode.left, data)
        else:
            rootNode.right = self.insertAVL(rootNode.right, data)
        
        balance = self.getBalance(rootNode)
        if balance > 1 and data < rootNode.left.data: 
            rootNode = self.rightRotation(rootNode)
        elif balance > 1 and data >= rootNode.left.data:
            rootNode.left = self.leftRotation(rootNode.left)
            rootNode = self.rightRotation(rootNode)
        elif balance < -1 and data >= rootNode.right.data: 
            rootNode = self.leftRotation(rootNode)
        elif balance < -1 and data < rootNode.right.data: 
            rootNode.right = self.rightRotation(rootNode.right)
            rootNode = self.leftRotation(rootNode)
        
        return rootNode
    
    def rightRotation(self, root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        return new_root
    
    def leftRotation(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        return new_root
    
    def height(self, root):
        if not root:
            return 0 
        return 1 + max(self.height(root.left), self.height(root.right))

    def findMin(self):
        t = self.root
        while t.left!=None:
            t = t.left
        return t.data
    
    def findMax(self):
        t = self.root
        while t.right!=None:
            t = t.right
        return t.data

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def getBalance(self, rootNode):
        if not rootNode:
            return 0
        return self.height(rootNode.left) - self.height(rootNode.right)

    def getMinValueNode(self,rootNode):
        if rootNode is None or rootNode.left is None:
            return rootNode
        return self.getMinValueNode(rootNode.left)

    def delete(self, data):
        self.root = self.deleteAVL(self.root, data)

    def deleteAVL(self, rootNode, nodeValue):
        if not rootNode:
            return rootNode
        elif nodeValue < rootNode.data:
            rootNode.left = self.deleteAVL(rootNode.left, nodeValue)
        elif nodeValue > rootNode.data:
            rootNode.right = self.deleteAVL(rootNode.right, nodeValue)
        else:
            if rootNode.left is None:
                temp = rootNode.right
                rootNode = None
                return temp 
            elif rootNode.right is None:
                temp = rootNode.left
                rootNode = None
                return temp 
            temp = self.getMinValueNode(rootNode.right)
            rootNode.data = temp.data
            rootNode.right = self.deleteAVL(rootNode.right, temp.data)
        balance = self.getBalance(rootNode)
        if balance > 1 and self.getBalance(rootNode.left) >= 0:
            return self.rightRotation(rootNode)
        if balance < -1 and self.getBalance(rootNode.right) <= 0:
            return self.leftRotation(rootNode)
        if balance > 1 and self.getBalance(rootNode.left) < 0:
            rootNode.left = self.leftRotation(rootNode.left)
            return self.rightRotation(rootNode)
        if balance > 1 and self.getBalance(rootNode.right) < 0:
            rootNode.right = self.leftRotation(rootNode.right)
            return self.leftRotation(rootNode)
        
        
        
        return rootNode

    def Min_Cost(self, node, temp, lst_of_sum): 
        if self.root is None:
            return lst_of_sum
        Min = self.findMin()
        temp.append(Min)
        self.delete(Min)
        if len(temp) >= 2:
            lst_of_sum.append(sum(temp))
            self.insert(sum(temp))
            return self.Min_Cost(node, [], lst_of_sum)
        return self.Min_Cost(node, temp, lst_of_sum)
    
    def Max_Cost(self, node, temp, lst_of_sum): 
        if self.root is None:
            return lst_of_sum
        Min = self.findMax()
        temp.append(Min)
        self.delete(Min)
        if len(temp) >= 2:
            lst_of_sum.append(sum(temp))
            self.insert(sum(temp))
            return self.Max_Cost(node, [], lst_of_sum)
        return self.Max_Cost(node, temp, lst_of_sum)
        

inp = input('Enter Input: ').split("/")
number = [int(i) for i in inp[0].split()]
AVLTree = AVL()

if len(number) <= 1:
    print(f"Min cost: 0")
    print(f"Max cost: 0")
else:
    for i in number:
        AVLTree.insert(i)
    print(f"Min cost: {sum(AVLTree.Min_Cost(AVLTree.root, [], []))}")
    for i in number:
        AVLTree.insert(i)
    print(f"Max cost: {sum(AVLTree.Max_Cost(AVLTree.root, [], []))}")

