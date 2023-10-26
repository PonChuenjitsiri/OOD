class Node:
    def __init__(self, item, next = None):
        self.item = item
        if next is None:
            self.next = None
        else:
            self.next = next

class LinkList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.item) + " "
        while cur.next != None:
            s += str(cur.next.item) + " "
            cur = cur.next
        return s

    def append(self, item):    
        node = Node(item)
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node


def RadixSort():
    pass

inp = input("Enter Input : ").split()
highest = 0
L = LinkList()
lst = [L] * 10
for i in inp:
    if int(i) > int(highest):
        highest = i
for i in range(1,len(highest)+1):
    for num in inp:
        print(num[-i])
        if i > len(num):
            lst[0].append(num)
        else:
            lst[4].append(num)

