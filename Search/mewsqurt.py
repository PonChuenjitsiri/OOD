def squre(lst,num):
    if len(lst) == 1:
        return print(lst[0])
    print(lst)
    middle = lst[int(len(lst)//2)]
    print(middle)
    if middle * middle == num: return print(middle)
    elif middle * middle > num:
        return squre(lst[:int(len(lst)//2):],num)
    return squre(lst[0:int(len(lst)//2):],num)
    


inp = input("input : ")
lst = []
for i in range(1,int(inp)+1):
    lst.append(int(i))
squre(lst,int(inp))