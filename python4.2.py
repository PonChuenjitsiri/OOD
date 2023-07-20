inp = input("Enter people : ")
class Queue:
    def __init__(self,List = None):
        if List == None:
            self.items = []
        else:
            self.items = List
    
    def enQueue(self,value):
        self.items.append(value)

    def deQueue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

    def isFull(self):
        return len(self.items) > 4

    def __str__(self):
        return self.items

minute = 0
count_ch1 = 0
count_ch2 = 0
main = Queue()
cashier1 = Queue()
cashier2 = Queue()
[main.enQueue(st) for st in inp]
while not main.isEmpty():
    minute += 1
    if not cashier1.isFull():
        cashier1.enQueue(main.deQueue())
        print(minute,main.items,cashier1.items,end=" ")
        print(cashier2.items)
        count_ch1 += 1
        
        if count_ch1 == 3:
            cashier1.deQueue()
            count_ch1 = 0
        if not cashier2.isEmpty():
            count_ch2 += 1
            if count_ch2 == 2:
                cashier2.deQueue()
                count_ch2 = 0
    else:
        cashier2.enQueue(main.deQueue())
        print(minute,main.items,cashier1.items,end=" ")
        print(cashier2.items)
        count_ch2 += 1
        count_ch1 += 1
        if count_ch2 == 2:
            cashier2.deQueue()
            count_ch2 = 0
        if count_ch1 == 3:
            cashier1.deQueue()
            count_ch1 = 0