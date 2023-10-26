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

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

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
    custumerqueue = []
    custumerqueue.append(rootNode)
    while custumerqueue != []:
        root = custumerqueue.pop(0)
        item.append(root.data)
        if root.leftChild is not None:
            custumerqueue.append(root.leftChild)
        
        if root.rightChild is not None:
            custumerqueue.append(root.rightChild)
    return item

def insertNodeBT(rootNode,newNode):
    if not rootNode:
        return
    custumerqueue = Queue()
    custumerqueue.enqueue(rootNode)
    while rootNode is not None:
        root = custumerqueue.dequeue()
        if int(newNode.data) < int(root.value.data) :
            if root.value.leftChild is not None:
                custumerqueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return
        else:
            if root.value.rightChild is not None:
                custumerqueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return

        
inp = input("Enter Input : ").split()
rootNode = TreeNode(inp.pop(0))
[insertNodeBT(rootNode,TreeNode(i)) for i in inp]
print("Preorder : " + " ".join(preTraversal(rootNode, [])))
print("Inorder : " + " ".join(inOrderTraversal(rootNode, [])))
print("Postorder : " + " ".join(postOrderTraversal(rootNode, [])))
print("Breadth : " + " ".join(levelOrderTraversal(rootNode, [])))


