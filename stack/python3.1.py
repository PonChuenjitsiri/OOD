dict = {
    "(" : ")",
    "{" : "}",
    "[" : "]"
}

class Stack:
    def __init__(self,List = None):
        if List == None:
            self.items = []
        else:
            self.items = List
    
    def parenMatch(self,paren):
        count = 0
        for char in paren:
            if char in dict.keys():
                self.items.append(char)
                
            else:
                if len(self.items) != 0:   
                    if dict[self.items[-1]] != char:
                        count += 1
                    else:
                        self.items.pop()
                        status = "Perfect ! ! !"
                else:
                    count += 1
        if len(self.items) != 0 :
            count += len(self.items)
        if count == 0 and len(self.items) == 0:
            return print(count) ,print(status)
        else:
            return print(count)

s = Stack()
input = input("Enter Input : ")
s.parenMatch(input)