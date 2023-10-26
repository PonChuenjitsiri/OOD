class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        self.sec = None
class Snode:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Link:
    def __init__(self):
        self.head = None
        self.tail = None
    def next_node(self,data):
        node = Node(data)
        if self.search(data) != None:
            return
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    def search(self,data):
        primary = self.head
        while primary != None:
            if primary.data == data:
                return primary
            primary = primary.next
        return None
    def next_secondary_node(self,n,data):
        node = Snode(data)
        pri_node = self.search(n)
        if pri_node.sec == None:
            pri_node.sec = node
            return
        cur = pri_node.sec
        while cur.next != None:
            cur=cur.next
        cur.next = node
    def show_all(self):
        primary, s = self.head,""
        while primary != None:
            s += str(primary.data) + " : "
            secondary = primary.sec
            while secondary != None:
                s += str(secondary.data) + ","
                secondary = secondary.next
            s += "\n"
            primary = primary.next
        return print(s)

inp = input("input : ").split(",")
l = Link()
for i in inp:
    u = i.split(" ")
    h = u[1].split("-")
    if u[0] == "ADN":
        l.next_node(h[0])
    elif u[0] == "ADSN":
        l.next_secondary_node(h[0],h[1])
l.show_all()