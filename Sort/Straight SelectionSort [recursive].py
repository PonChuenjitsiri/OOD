def check_sort(lst, dummy, i = 0):
    if lst == []:
        return True
    if dummy > lst[0]:
        return False
    i += 1
    return check_sort(lst[1::], lst.pop(0), i)

def sort_selections(lst, size, count = 1):
    if check_sort(lst.copy(), lst[0]):
        return lst
    maxindex = lst.index(max(lst[:size:]))
    if maxindex == size-1:
        return sort_selections(lst, len(lst[:len(lst)-count:]), count+1)
    lst[maxindex] , lst[size-1] = lst[size-1] , lst[maxindex]
    print(f"swap {lst[maxindex]} <-> {lst[size-1]} : {lst}")
    return sort_selections(lst, len(lst[:len(lst)-count:]), count+1)
    

lst = [int(i) for i in input("Enter Input : ").split()]
print(sort_selections(lst, len(lst)))
