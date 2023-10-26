class Node:
    def __init__(self, data, id):
        self.data = data
        self.left = None
        self.right = None
        self.id = id
    
    def __str__(self):
        return str(self.data)

class Tree():
    def __init__(self):
        self.root = None
        self.count = 1
    
    def insert(self,data):
        self.root = self.insertTree(self.root,data)
        self.count += 1
    
    def insertTree(self,root,data):
        if not root:
            return Node(data, self.count)
        if data < root.data:
            root.data, data = data, root.data

        if not root.left:
            root.left = self.insertTree(root.left,data)
        elif not root.right:
            root.right = self.insertTree(root.right,data)  
        else:
            root.left = self.insertTree(root.left,data)

        return root      
    
    def heapify(self):
        self.root = self.heapifyTree(self.root)
    
    def heapifyTree(self,root):
        if not root:
            return root
        
        small, left, right = root, root.left, root.right

        if left and (left.data < small.data or (left.data == small.data and left.id < small.id)):
            small = left
        
        if right and (right.data < small.data or (right.data == small.data and right.id < small.id)):
            small = right
        
        if small != root:
            root.data, small.data = small.data, root.data
            root.id, small.id = small.id, root.id
            self.heapifyTree(small)

        return root

    def add_root(self,data):
        if self.root is None:
            return
        self.root.data += data

    def printOutput(self, customer, day):
        print(f"Customer {customer} Booking Van {self.root.id} | {day} day(s)")

inp = input('Enter Input : ').split("/")
BusNum = int(inp[0])
days = [int(i) for i in inp[1].split()]
T = Tree()
for i in range(BusNum):
    T.insert(1)
customer = 1
for day in days:
    T.add_root(day)
    T.printOutput(customer, day)
    customer += 1
    T.heapify()

    