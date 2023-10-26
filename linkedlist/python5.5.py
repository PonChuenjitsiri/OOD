class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

def createLL(LL):
    # Code Here
    h = [Node(item) for item in LL]
    return h      

def printLL(head):
    # Code Here
    s = ""
    for item in head:
        s += item.value + " "
    return s

def SIZE(head):
    # Code Here
    return len(head)

def buttom_up(head, b):
    bottom_up = []
    temp = []
    count_but = b
    for count, item in enumerate(head):
        if count >= count_but:
            bottom_up.append(item.value)
        else:
            temp.append(item.value)
    bottom_up.extend(temp)
    return bottom_up

def scarmble(head, b, r, size):
    if size < 10:
        return
    riffle = []
    temp = []
    de_buttom = []
    count_but = int((b / 100)* size)
    count_rif = int((r / 100)* size)
    bottom = buttom_up(head,count_but)
    print(f"BottomUp {b:.3f} % : ", end="")
    print(*buttom_up(head,count_but), end=" ")
    print()
    for count, item in enumerate(bottom):
        if count < count_rif:
            riffle.append(item)
        else:
            temp.append(item)
    riffle_result = []
    for item in range(len(riffle)):
        if riffle:
            riffle_result.append(riffle.pop(0))
        if temp:
            riffle_result.append(temp.pop(0))
    if temp:
        while temp:
            riffle_result.append(temp.pop(0))
    print(f"Riffle {r:.3f} % : ", end="")
    print(*riffle_result, end=" ")
    print()
    print(f"Deriffle {r:.3f} % : ", end="")
    print(*buttom_up(head,count_but), end=" ")
    print()
    temp = []
    for count, item in enumerate(buttom_up(head,count_but)):
        if count >= count_but:
            de_buttom.append(item)
        else:
            temp.append(item)
    de_buttom.extend(temp)
    print(f"Debottomup {b:.3f} % : ", end="")
    print(*head, end=" ")
    print()

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)