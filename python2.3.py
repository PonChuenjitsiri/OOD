def mod_position(arr, s):
    temp = []
    for i in range(1,len(arr)+1):
        if i % s == 0:
            temp.append(arr[i-1])
    return temp

print("*** Mod Position ***")
string,mod = input("Enter Input : ").split(",")
letter = [x for x in string]
print(mod_position(letter, int(mod)))
