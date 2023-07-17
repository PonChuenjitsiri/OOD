inp = input("Enter Input: ")
lst = [st for st in inp.split(",")]

class Stack:
    def __init__(self, lst=None):
        if lst is None:
            self.items = []
        else:
            self.items = lst
    
    def push(self, value):
        self.items.append(value)
    
    def pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []
    
    def peek(self):
        return self.items[-1]
    
    def get(self):
        return self.items

tree_stack = Stack()


for st in lst:
    if st.split()[0] == "A":
        height = int(st.split()[1])
        tree_stack.push(height)
    
    elif st.split()[0] == "S":
        temp = []
        while not tree_stack.isEmpty():
            if tree_stack.peek() % 2 == 0:
                temp.append(tree_stack.pop() - 1)
            else:
                temp.append(tree_stack.pop() + 2)
        
        while temp != []:
            tree_stack.push(temp.pop())
    
    elif st.split()[0] == "B":
        seen_stack = Stack()
        tem = []
        while not tree_stack.isEmpty():
            tem.append(tree_stack.pop())
        
        while tem != []:
            add = tem.pop()
            if not seen_stack.isEmpty():
                while not seen_stack.isEmpty() and add > seen_stack.peek():
                    seen_stack.pop()
                seen_stack.push(add)
                tree_stack.push(add)
            else:
                seen_stack.push(add)       
        print(seen_stack.size())