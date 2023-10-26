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
    
    def left_rotation(self, root):
        new_node = root.right
        root.data = new_node.left
        new_node.left = root
        return new_node
    
    def right_rotation(self, root):
        new_node = root.left
        root.data = new_node.right
        new_node.right = root
        return new_node

    def height(self,root):
        if root is None:
            return 0
        return 1 + max(root.left.data, root.right.data)

    

    def insert(self, new_data):
        self.root = self._insert(self.root, new_data)
        return self.root

    def _insert(self, root, new_data):
        if root is None:
            return Node(new_data)
        else:
            if new_data < self.root.data:
                self._insert(root.left, new_data)
            else:
                self._insert(root.right, new_data)
        balance = self.get_balance(root)
        if balance > 1 and new_data < self.root.left:
            root = self.right_rotation(root)
        if balance > 1 and new_data >= self.root.left:
            root.left = self.left_rotation(root)
            root = self.right_rotation(root)
        if balance < -1 and new_data > self.root.right:
            root = self.left_rotation(root)
        if balance < -1 and new_data <= self.root.right:
            root.right = self.right_rotation(root)
            root = self.left_rotation(root)
        
        return root

        
    
   


    
