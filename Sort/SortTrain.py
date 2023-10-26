def check_sort(lst, dummy, i = 0):
    if not lst:
        return "Yes"
    if dummy > lst[0]:
        return "No"
    i += 1
    return check_sort(lst[1::], lst.pop(0), i)


inp = [int(i) for i in input("Enter Input : ").split( )]
print(check_sort(inp, inp[0]))