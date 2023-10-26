def pantip(k, n, arr, path):
    if arr == []:
        return [[]]
    else:
        patt = pantip(k,n,arr[1])
    pass

inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
pattern = pantip(int(inp[0]), 0, arr, [])
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))