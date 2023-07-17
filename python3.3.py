class Stack:

    def __init__(self,List = None):
        if List == None:
            self.items = []
        else:
            self.items = List
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
inp = input('Enter Infix : ')
op_paren = False
S = Stack()

print('Postfix : ', end='')

### Enter Your Code Here ###

for char in inp:
    if char.isalpha():
        print(char, end='')
    # elif char == '(':
    #     S.push(char)
    # elif char == ')':
    #     while not S.isEmpty() and S.peek() != "(":
    #         print(S.pop(), end='')
    #     if not S.isEmpty() and S.peek() == "(":
    #         S.pop()

    else:    
        if not S.isEmpty() and S.peek() == '^':
            while not S.isEmpty() and S.peek() != "(" and S.peek() != ")":
                    print(S.pop(), end='')
            op_paren = False
        else:
            if not S.isEmpty():
                if S.peek() == "*" or S.peek() == '/':
                    while not S.isEmpty() and S.peek() != "(" and S.peek() != ")":
                        print(S.pop(), end='')
                    op_paren = False
                elif not S.isEmpty() and S.peek() == "(":
                    op_paren = True
                if op_paren:
                    while not S.isEmpty() and S.peek() != "(" and S.peek() != ")":
                        print(S.pop(), end='')

                    if not S.isEmpty() and (S.peek() == ')' or S.peek() != "("):
                        S.pop()
                        op_paren = False  
        
        S.push(char)
while not S.isEmpty():
        if S.peek() == '(' or S.peek() == ")":
            S.pop()
        else:
            print(S.pop(), end='')

print()