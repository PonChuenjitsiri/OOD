class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class AVL():
    def __init__(self):
        self.root = None
    
    def insert(self, new_data):
        self.root = self._insert(self.root, new_data)
        return self.root
    
    def height(self,root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left),self.height(root.right))
    
    def get_balance(self,root):
        if root is None:
            return 0
        return self.height(root.left) - self.height(root.right)

    def right_rotation(self,root):
        new_node = root.left
        root.left = new_node.right
        new_node.right = root
        return new_node
    
    def left_rotation(self,root):
        new_node = root.right
        root.right = new_node.left
        new_node.left = root
        return new_node

    def _insert(self, root, new_data):
        if root is None:
            return Node(new_data)
        if new_data < root.data:
            root.left = self._insert(root.left, new_data)
        else:
            root.right = self._insert(root.right, new_data)
        balance = self.get_balance(root)
        if balance > 1 and new_data < root.left.data:
            root = self.right_rotation(root)
        elif balance > 1 and new_data >= root.left.data:
            root.left = self.left_rotation(root.left)
            root = self.right_rotation(root)
        elif balance < -1 and new_data >= root.right.data:
            root = self.left_rotation(root)
        elif balance < -1 and new_data < root.right.data:
            root.right = self.right_rotation(root.right)
            root = self.left_rotation(root)
        return root

    def printTree(self, root, level = 0):
        if root != None:
            self.printTree(root.right, level + 1)
            print("     " * level, root.data)
            self.printTree(root.left, level + 1)
    
    def levelTraversal(self, root):
        if root is None:
            return
        queue = []
        queue.append(root)
        while queue != []:
            temp = queue.pop(0)
            print(temp.data)
            if temp.left is not None:
                queue.append(temp.left)
            if temp.right is not None:
                queue.append(temp.right)
    
inp = input("Enter input : ").split()
Tree = AVL()
for i in inp:
    Tree.insert(i)

Tree.printTree(Tree.root)
Tree.levelTraversal(Tree.root)


        