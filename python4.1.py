inp = input("Enter Input : ")
lst = [st for st in inp.split(",")]

class Queue:
    def __init__(self,List = None):
        if List == None:
            self.items = []
        else:
            self.items = List
    
    def enQueue(self, value):
        self.items.append(value)
    
    def deQueue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def index(self,value):
        return self.items.index(value)
    
    def size(self):
        return len(self.items)
    
    def get(self):
        lst = [str(st) for st in self.items] 
        return lst
    
queue = Queue()
for st in lst:
    if st.split()[0] == "E":
        num = int(st.split()[1])
        queue.enQueue(num)
        print("Add {num} index is {index}".format(num = num, index = queue.index(num)))
    
    elif st.split()[0] == "D":
        if queue.isEmpty():
            print(-1)
        else:
            print("Pop {num} size in queue is {size}".format(num = queue.deQueue() , size = queue.size()))

if not queue.isEmpty():
    print("Number in Queue is :  {queue}".format(queue = queue.get()))

else:
    print("Empty")
    
