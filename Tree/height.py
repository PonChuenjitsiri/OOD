class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

def insertNodeBT(rootNode,newNode):
    if not rootNode:
        return
    custumerqueue = []
    custumerqueue.append(rootNode)
    while rootNode is not None:
        root = custumerqueue.pop(0)
        if int(newNode.data) < int(root.data):
            if root.left is not None:
                custumerqueue.append(root.left)
            else:
                root.left = newNode
                return
        else:
            if root.right is not None:
                custumerqueue.append(root.right)
            else:
                root.right = newNode
                return

def height(root):
    if root is None:  
        return 0 
    leftAns = height(root.left)
    rightAns = height(root.right)
    return max(int(leftAns), int(rightAns)) + 1

inp = [int(i) for i in input('Enter Input : ').split()]
rootNode = Node(inp.pop(0))
[insertNodeBT(rootNode,Node(i)) for i in inp]
print(f"Height of this tree is : {height(rootNode) - 1}")
