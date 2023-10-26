class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

def insert(rootNode,newNode):
    if not rootNode:
        return
    custumerqueue = []
    custumerqueue.append(rootNode)
    while rootNode is not None:
        root = custumerqueue.pop(0)
        if root.left is not None:
            custumerqueue.append(root.left)
        else:
            root.left = newNode
            return
        
        if root.right is not None:
            custumerqueue.append(root.right)
        else:
            root.right = newNode
            return
        
res = []
def pathFinder(rootNode, path, pathLen):
    if not rootNode:
        return
    if len(path) > pathLen:
        path[pathLen] = rootNode.data
    else:
        path.append(rootNode.data)
    pathLen += 1
    if rootNode.left is None and rootNode.right is None:
        res.append(path[0:pathLen].copy())
    else:
        pathFinder(rootNode.left, path, pathLen)
        pathFinder(rootNode.right, path, pathLen)

inp = [int(i) for i in input('Enter tree: ').split()]
rootNode = Node(inp.pop(0))
[insert(rootNode,Node(i)) for i in inp]
pathFinder(rootNode, [], 0)
maxPath = max(res, key=sum)
print(f"Maximum path: {maxPath}")



    