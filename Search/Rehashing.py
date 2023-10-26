def find_prime(num,i = 2):
    if num%i != 0:
        return num
    return find_prime(num+1, i+1)

def hashing(lst, collision_num, collisionCount, maxcollosion, index = 1 ):
    hash = collision_num % len(lst)
    if index > len(lst):
        return

    if lst[hash] == None:
        lst[hash] = collision_num
        return
    else:
        new_hash = (hash + index * index) % len(lst)
        if lst[new_hash] is not None:
            if collision_num == maxcollosion: return
            print(f"collision number {collisionCount} at {new_hash}")
        if lst[new_hash] == None:
            lst[new_hash] = collision_num
            return
        return hashing(lst, collision_num,collisionCount,maxcollosion, index + 1)

def Rehashing(table, maxcollosion, threshole, lst, key, datasize = 0, collisionCount = 0, dummy = []):
    if key == []:
        return
    print(f"Add : {key[0]}")
    dummy = []
    for i in lst:
        if i is not None:
            dummy.append(i)
    dummy.append(key[0])

    datasize += 1

    if lst[key[0]%table] is not None:
        collisionCount += 1
        print(f"collision number {collisionCount} at {key[0]%table}")

    if collisionCount >= maxcollosion:
        print("****** Max collision - Rehash !!! ******")
        table = find_prime(table*2)
        lst = [None] * (table)
        
        collisionCount = 0
        for i in dummy:
            if lst[i%table] is not None:
                print(f"collision number {collisionCount} at {i%table}")
                collisionCount += 1
            hashing(lst, i,collisionCount,maxcollosion)

    elif datasize/table > threshole:
        print("****** Data over threshold - Rehash !!! ******")
        table = find_prime(table*2)
        lst = [None] * (table)
        for i in dummy:
            if lst[i%table] is not None:
                print(f"collision number {collisionCount} at {i%table}")
                collisionCount += 1
            hashing(lst, i,collisionCount,maxcollosion)
    else:
        hashing(lst, key[0],collisionCount,maxcollosion)
    get_output(lst)
    return Rehashing(table, maxcollosion, threshole, lst, key[1::], datasize, collisionCount)
    
def get_output(lst):
    for i in enumerate(lst):
        print(f"#{i[0]+1}	{i[1]}")
    print("----------------------------------------")

print(" ***** Rehashing *****")
inp = input("Enter Input : ").split("/")
condition, key = [int(i) for i in inp[0].split()], [int(i) for i in inp[1].split()]
Table, Maxcollosion, Threshole = condition[0], condition[1], condition[2]/100
lst = [None] * Table
print("Initial Table :")
get_output(lst)
Rehashing(Table, Maxcollosion, Threshole, lst, key)
