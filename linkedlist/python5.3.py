class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None
class Link:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, item):
        #Code Here
        p = Node(item)
        if not self.head :
            self.head = self.tail = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p
            self.tail = p

    def __str__(self):
        cur = self.head
        s = []
        while cur != None:
            s.append(cur.value)
            cur = cur.next
        return "->".join(s)

    def isEmpty(self):
        return self.head == None
    
total,bokies  = input("Enter input: ").split(" ")
bokies = bokies.split(",")
L = Link()
list_link = [L]
found = False
for boky in bokies:
    data,nextdata = boky.split("-")
    front_boky = Node(data)
    back_boky = Node(nextdata)
    for linklist in list_link:
        if not linklist.head :
            linklist.append(data)
            linklist.append(nextdata)
            found = True
        else:
            if linklist.tail.value == front_boky.value:
                linklist.tail.next = back_boky
                linklist.tail = back_boky
                found = True
                break
            elif linklist.head.value == back_boky.value:
                front_boky.next = linklist.head
                linklist.head = front_boky
                found = True
                break
    if found == True:
        found = False
    else:
        L2 = Link()
        L2.append(data)
        L2.append(nextdata)
        list_link.append(L2)
    

list_total = list(map(str,range(1,int(total)+1)))
for linked in list_link :
    cur = linked.head
    while cur :
        if cur.value in list_total:
            list_total.remove(cur.value)
        cur = cur.next
if list_total:
    for i in list_total:
        L3 = Link()
        L3.append(i)
        list_link.append(L3)

def bubblesort(arr):
    n = len(arr) 
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if int(arr[j].head.value) > int(arr[j+1].head.value):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break

bubblesort(list_link)

temp_list = list_link.copy()
for list_temp1 in temp_list:
    cur1 = list_temp1
    for list_temp2 in temp_list:
        cur2 = list_temp2
        if list_temp1 in list_link and list_temp2 in list_link:
            if cur1 is not cur2 and cur1.head.value == cur2.tail.value:
                cur2.tail.next = cur1.head.next
                list_temp2.tail = cur1.tail
                list_link.remove(list_temp1)
            elif cur1 is not cur2 and cur1.tail.value == cur2.head.value:
                cur1.tail.next = cur2.head.next
                list_temp1.tail = cur2.tail
                list_link.remove(list_temp2)

i = 0
for linked in list_link :
    i += 1
    print(f"{i}: {linked}")
print(f"Number of train(s): {i}")