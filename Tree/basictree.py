class TreeNode:
    def __init__(self,data, children = []):
        self.data = data
        self.children = children
    
    def __str__(self, level=0):
        res = ' ' * level + str(self.data) + '\n'
        for child in self.children:
            res += child.__str__(level + 1)
        return res
    
    def addChild(self, TreeNode):
        self.children.append(TreeNode)

tree = TreeNode("Drinks",[])
cold = TreeNode("Cold",[])
hot = TreeNode("Hot",[])
tree.addChild(cold)
tree.addChild(hot)
tea = TreeNode("Tea",[])
coke = TreeNode("Coke",[])
cold.addChild(coke)
cold.addChild(tea)
print(tree)