def move(n, A, C, B,maxn):
    if n == 1:
        print("move",n,"from","", dict[A], 'to', dict[C])
        res[C].append(res[A].pop(-1))
        printR(maxn)
    else:
        move(n-1, A, B, C, maxn)
        print("move",n,"from","", dict[A], 'to', dict[C])
        res[C].append(res[A].pop(-1))
        printR(maxn)
        move(n-1, B, C, A, maxn) 

def printR(size):
    if size == 0:
        return
    if len(res[0]) < size:
        print("|",end="  ")    
    else:
        if res[0]:
            print(res[0][size-1],end="  ")    
    if len(res[1]) < size:
        print("|",end="  ")
    else:
        if res[1]:
            print(res[1][size-1],end="  ")      
    if len(res[2]) < size:
        print("|")
    else:
        if res[2]:
            print(res[2][size-1])
    printR(size-1)        

n = int(input("Enter Input : "))
res = [list(range(n, 0, -1)),[],[]]
dict = {
    0 : "A",
    1 : "B",
    2 : "C"
}
if n > 0 :
    printR(n+1)
    move(n,0,2,1,n+1)

