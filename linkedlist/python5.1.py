print("***Railway on route***")
inp = input('Input Station name/Source, Destination, Direction(optional): ').split('/')
station = inp[0].split(",")
destiny = inp[1].split(",")
class Node:
    def __init__(self, value, next=None, previous=None):
        self.value = value
        if next is None:
            self.next = None
        else:
            self.next = next
        if previous is None:
            self.previous = None
        else:
            self.previous = previous
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.for_size = 0 
        self.back_size = 0
    
    def backward(self,start,end):
        self.head.previous = self.tail
        self.tail.next = self.head
        cur= self.head
        res = []
        count = 0
        while cur.value != start:  
            cur = cur.next
        res.append(cur.value)                             
        while cur.previous.value != end:
            res.append(cur.previous.value)
            cur = cur.previous
            count += 1
        res.append(cur.previous.value)
        count += 1
        self.back_size = count
        return "Backward Route: " + "->".join(res) + f",{count}"
        
    def forward(self,start,end):
        self.head.previous = self.tail
        self.tail.next = self.head
        cur= self.head
        count = 0
        res = []
        while cur.value != start:
            cur = cur.next
        res.append(cur.value)

        while cur.next.value != end:
            res.append(cur.next.value)
            cur = cur.next
            count += 1
        res.append(cur.next.value)
        count += 1
        self.for_size = count
        return "Forward Route: " + "->".join(res) + f",{count}"

    def append(self, value):
        node = Node(value)
        if self.head == None:
            self.head = self.tail = node
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = node
            node.previous = t
            self.tail = node
    

    def forward_size (self):
        return self.for_size

    def backward_size (self):
        return self.back_size
    
L = LinkedList()
[L.append(stations) for stations in station]
if  len(destiny) == 3 and destiny[2] == 'F':
    if destiny[0] == destiny[1]:
        print(f"Forward Route: {destiny[0]},{0}")
    else:
        print(L.forward(destiny[0],destiny[1]))
elif len(destiny) == 3 and destiny[2] == 'B':
    if destiny[0] == destiny[1]:
        print(f"Backward Route: {destiny[0]},{0}")
    else:
        print(L.backward(destiny[0],destiny[1]))
else:
    if destiny[0] == destiny[1]:
        print(f"Forward Route: {destiny[0]},{0}")
        print(f"Backward Route: {destiny[0]},{0}")
    else:
        L.forward(destiny[0],destiny[1])
        L.backward(destiny[0],destiny[1])
        if L.forward_size() < L.backward_size():
            print(L.forward(destiny[0],destiny[1]))
        elif L.backward_size() < L.forward_size():
            print(L.backward(destiny[0],destiny[1]))
        else:
            print(L.forward(destiny[0],destiny[1]))
            print(L.backward(destiny[0],destiny[1]))