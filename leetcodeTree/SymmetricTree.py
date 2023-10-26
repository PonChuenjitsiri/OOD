class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:
        if root is None :
            return True
        
        return self.mirror(root.left, root.right)
    
    def mirror(self, root1, root2) -> bool:
        if root1 is None and root2 is None:
            return True
        if root1 is not "null" and root2 is not "null":
            if root1.val == root2.val:
                return self.mirror(root1.left, root2.right) and self.mirror(root1.right, root2.left)
        
        return False
    


