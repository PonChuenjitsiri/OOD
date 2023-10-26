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
        self.printTree(self.root)
        print("--------------------------------------------------")

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

def closest(lst, K):
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

inp = input('Enter Input : ').split("/")
number = [int(i) for i in inp[0].split()]
closest_goal = int(inp[1])

T = BST()
print(f" {number[0]}")
print("--------------------------------------------------")
for i in number:
    T.insert(i)
print(f"Closest value of {closest_goal} : {closest(number, closest_goal)}")
