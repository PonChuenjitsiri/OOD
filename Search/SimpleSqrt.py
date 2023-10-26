def Simplesqrt(lst, x):
    if len(lst) == 1:
        return print(lst[0])
    if lst[int(len(lst)/2)] * lst[int(len(lst)/2)] == x:
        return print(lst[int(len(lst)/2)])
    if lst[int(len(lst)/2)] * lst[int(len(lst)/2)] < x:
        return Simplesqrt(lst[int(len(lst)/2)::], x)
    return Simplesqrt(lst[:int(len(lst)/2):], x)

inp = [i for i in range(1,int(input("simple sqrt: "))+1)]
Simplesqrt(inp, inp[len(inp)-1])


