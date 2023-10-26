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
        self.Size = 0 

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        #Code Here
        self.Size += 1
        p = Node(item)
        if self.head == None:
            self.head = self.tail = p
        else:
            t = self.head
            while t.next != None:
                t = t.next   
            t.next = p
            p.previous = t 
            self.tail = p   

    def addHead(self, item):
        #Code Here
        self.Size += 1
        p = Node(item)
        t = self.head
        if self.head == None:
            self.head = p
            self.tail = p
        else:
            p.next = t
            t.previous = p
            self.head = p
        
    def insert(self, pos, item):
        #Code Here
        invers = self.Size + pos
        p = Node(item)
        t = self.head
        if self.head == None:
            self.head = self.tail = p
        elif invers > 0 and invers < self.Size:
            for i in range(invers-1):
                t = t.next 
            temp = t.next
            t.next = p
            p.previous = t
            p.next = temp
            temp.previous = p
        elif pos <= 0:
            p.next = t
            t.previous = p
            self.head = p
        elif pos >= self.Size:
            while t.next != None:
                t = t.next
            t.next = p
            p.previous = t
            self.tail = p
        else:  
            for i in range(pos -1):
                t = t.next
            temp = t.next
            t.next = p
            p.previous = t
            p.next = temp
            temp.previous = p
            
        self.Size += 1

    def search(self, item):
        #Code Here
        current = self.head
        while current != None:
            if current.value == item:
                return "Found"
            current = current.next
        return "Not Found"

    def index(self, item):
        #Code Here
        current = self.head
        index = 0
        if current.value == item:
                return 0
        else:
            while current != None:
                if current.value == item:
                    return index   
                current = current.next
                index += 1
        return -1

    def size(self):
        #Code Here
        return self.Size

    def pop(self, pos):
        #Code Here
        current = self.head
        current_tail = self.tail
        if pos < 0 or pos > self.Size-1 or self.Size == 0:
                return "Out of Range"
        else:
                if pos == 0:
                    self.head = None
                    self.tail = None
                    self.Size -= 1
                    return "Success"
                for i in range(0,self.Size):
                    if i == pos and current != None:
                        current.next = current.next.next
                        current_tail.previous = current_tail.previous.previous
                        self.Size -= 1
                        return "Success"
                    current = current.next
                    current_tail = current_tail.previous
        
L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())