inp = input("input : ")
lst = [st for st in inp.split(",")]

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
        return str(self.items)

queue = Queue()
enqueue_count = 0
error_dequeue = 0
error_input = 0
for st in lst:
    print("Step : {step}".format(step = st))
    if st.startswith("D"):
        if queue.isEmpty():
            print("Dequeue : []")
            error_dequeue += int(st[1:])
        else:
            for i in range(int(st[1:])):  
                if queue.isEmpty():
                    error_dequeue += 1
                else:
                    queue.deQueue()
            print("Dequeue : {dequeue}".format(dequeue = queue))
    elif st.startswith("E"):
        for i in range(int(st[1:])):
            queue.enQueue("*"+str(enqueue_count))
            enqueue_count += 1
        print("Enqueue :", queue)
    else:
        error_input += 1
        print(queue)
    print("Error Dequeue : {deerror}".format(deerror = error_dequeue))
    print("Error input : {error_input}".format(error_input = error_input))
    print("--------------------")