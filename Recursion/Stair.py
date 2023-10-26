def staircase(n,row):
    if n == 1:
        print("_" * (n-1) + "#" * (row+1))
    elif n > 0 :
        print("_" * (n-1) + "#" * (row+1))
        staircase(n - 1,row + 1)
staircase(4,0)