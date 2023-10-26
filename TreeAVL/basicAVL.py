class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()
    
    def __str__(self):
        value = [str(x) for x in self.LinkedList]
        return " ".join(value)
    
    def enqueue(self,value):
        newNode = Node(value)
        if self.LinkedList.head == None:
            self.LinkedList.head = self.LinkedList.tail = newNode
        else:
            self.LinkedList.tail.next = newNode
            self.LinkedList.tail = newNode
    
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False
    
    def dequeue(self):
        if self.isEmpty():
            return "No"
        else:
            tempNode = self.LinkedList.head
            if self.LinkedList.head == self.LinkedList.tail:
                self.LinkedList.head = self.LinkedList.tail = None
            else:
                self.LinkedList.head = self.LinkedList.head.next
        return tempNode

    def peek(self):
        if self.isEmpty():
            return "No"
        else:
            return self.LinkedList.head

class AVLNode():
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

def preTraversal(rootNode, item):
    if not rootNode:
        return 
    item.append(rootNode.data)
    preTraversal(rootNode.leftChild, item)
    preTraversal(rootNode.rightChild, item)
    return item

def inOrderTraversal(rootNode, item):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild, item)
    item.append(rootNode.data)
    inOrderTraversal(rootNode.rightChild, item)
    return item

def postOrderTraversal(rootNode, item):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild, item)
    postOrderTraversal(rootNode.rightChild, item)
    item.append(rootNode.data)
    return item

def levelOrderTraversal(rootNode, item):
    if not rootNode:
        return
    custumerqueue = Queue()
    custumerqueue.enqueue(rootNode)
    while not custumerqueue.isEmpty():
        root = custumerqueue.dequeue()
        item.append(root.value.data)
        if root.value.leftChild is not None:
            custumerqueue.enqueue(root.value.leftChild)
        
        if root.value.rightChild is not None:
            custumerqueue.enqueue(root.value.rightChild)
    return item

# def insertNodeBT(rootNode,newNode):
#     if not rootNode:
#         return
#     custumerqueue = Queue()
#     custumerqueue.enqueue(rootNode)
#     while rootNode is not None:
#         root = custumerqueue.dequeue()
#         if int(newNode.data) < int(root.value.data) :
#             if root.value.leftChild is not None:
#                 custumerqueue.enqueue(root.value.leftChild)
#             else:
#                 root.value.leftChild = newNode
#                 return
#         else:
#             if root.value.rightChild is not None:
#                 custumerqueue.enqueue(root.value.rightChild)
#             else:
#                 root.value.rightChild = newNode
#                 return

def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.rightChild, nodeValue)

def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def rightRotation(disbalancedNode):
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def leftRotation(disbalancedNode):
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newRoot.leftChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def re_balance(balance, nodeValue, rootNode):
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotation(rootNode)
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotation(rootNode.leftChild)
        return rightRotation(rootNode)
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotation(rootNode)
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotation(rootNode.rightChild)
        return leftRotation(rootNode)


def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)
    
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotation(rootNode)
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotation(rootNode.leftChild)
        return rightRotation(rootNode)
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotation(rootNode)
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotation(rootNode.rightChild)
        return leftRotation(rootNode)
    return rootNode

def getMinValueNode(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValueNode(rootNode.leftChild)

def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp 
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp 
        temp = getMinValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    balance = getBalance(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) >= 0:
        return rightRotation(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) <= 0:
        return leftRotation(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) < 0:
        rootNode.leftChild = leftRotation(rootNode.leftChild)
        return rightRotation(rootNode)
    if balance > 1 and getBalance(rootNode.rightChild) < 0:
        rootNode.rightChild = leftRotation(rootNode.rightChild)
        return leftRotation(rootNode)
    
    return rootNode



newAVL = AVLNode(10)
newAVL = insertNode(newAVL, -1)
newAVL = insertNode(newAVL, 11)
deleteNode(newAVL, -1)
Min = (getMinValueNode(newAVL))
print(Min.data)
print(levelOrderTraversal(newAVL,[]))