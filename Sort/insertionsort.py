def insertionsort(lst, lstoutput = [], index = 0):
    if lstoutput == []:
        lstoutput.append(lst.pop(0))
    if index == len(lstoutput) or lst[0] <= lstoutput[index]:
        lstoutput.insert(index, lst.pop(0))
        print(f"insert {lstoutput[index]} at index {index} : {lstoutput}",end="")
        if lst == []:
            return lstoutput
        print("",lst)
        return insertionsort(lst, lstoutput)
    else:
        return insertionsort(lst, lstoutput, index+1)
inp = [int(i) for i in input("Enter Input : ").split()]
inp = insertionsort(inp)
print("\nsorted")
print(inp)