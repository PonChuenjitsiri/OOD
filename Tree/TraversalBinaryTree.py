import QueueLinklist as queue

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBt = TreeNode("Drinks")
leftChild = TreeNode("HOT")
tea = TreeNode("TEA")
coffee = TreeNode("COFFEE")
rightChild = TreeNode("COLD")
newBt.leftChild = leftChild
newBt.rightChild = rightChild
leftChild.leftChild = tea
leftChild.rightChild = coffee

def preTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preTraversal(rootNode.leftChild)
    preTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    print(rootNode.data)
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    custumerqueue = queue.Queue()
    custumerqueue.enqueue(rootNode)
    rightheight = 0
    while not custumerqueue.isEmpty():
        root = custumerqueue.dequeue()
        print(root.value.data)
        if root.value.leftChild is not None:
            custumerqueue.enqueue(root.value.leftChild)

        
        if root.value.rightChild is not None:
            custumerqueue.enqueue(root.value.rightChild)

def searchBT(rootNode,nodeValue):
    if not rootNode:
        return "NOT EXIX"
    custumerqueue = queue.Queue()
    custumerqueue.enqueue(rootNode)
    while not custumerqueue.isEmpty():
        root = custumerqueue.dequeue()
        if root.value.data == nodeValue:
            return "FOUND"
        
        if root.value.leftChild is not None:
            custumerqueue.enqueue(root.value.leftChild)
        
        if root.value.rightChild is not None:
            custumerqueue.enqueue(root.value.rightChild)
    return "NOT FOUND"

def insertNodeBT(rootNode,newNode):
    if not rootNode:
        return
    custumerqueue = queue.Queue()
    custumerqueue.enqueue(rootNode)
    while rootNode is not None:
        root = custumerqueue.dequeue()
        if root.value.leftChild is not None:
            custumerqueue.enqueue(root.value.leftChild)
        else:
            root.value.leftChild = newNode
            return "sucess"
        if root.value.rightChild is not None:
            custumerqueue.enqueue(root.value.rightChild)
        else:
            root.value.rightChild = newNode
            return "sucess"

newNode = TreeNode("COLA")
inp = input("Enter tree: ").split()
rootNode = TreeNode(inp.pop(0))
# for i in inp:
#     insertNodeBT(rootNode,TreeNode(i))
[insertNodeBT(rootNode,TreeNode(i)) for i in inp]
preTraversal(rootNode)
# print(rootNode.data)