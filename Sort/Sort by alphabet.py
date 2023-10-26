inp = input("Enter Input : ")
out = inp.split()
list = []
for i in inp:
    if i.isalpha():
        list.append(ord(i))

def get_index(lst, index2, index1 = 0):
    if index1 == len(lst):
        return
    if index1 == index2:
        return get_index(lst, len(lst)-1, index1+1)
    if lst[index1] > lst[index2]:
        lst[index1],lst[index2] = lst[index2], lst[index1]
        out[index1],out[index2] = out[index2], out[index1]
    return get_index(lst, index2-1, index1)
get_index(list, len(list)-1)
for i in out:
    print(""+ i,end=" ")