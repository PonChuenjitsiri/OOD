input = int(input("Enter Input : "))
topleft = input + 2
for i in range(2 * input + 4):
    for j in range(2 * input + 4):
        if i < (topleft):
            if (j == topleft-(i + 1) or j <= topleft -1) and j >= topleft-(i + 1):
                print("#",end="")
            elif (j == topleft or j == 2 * input + 3) or ((j >topleft or j == 2 * input + 3) and i == 0 or i == topleft-1):
                print("+",end="")
            else:
                if j < topleft: 
                    print(".",end="")
                if j > topleft and j < 2 * input + 3  and i != 0 or i == topleft-1:
                    print("#",end="")
        else:
            if (j == topleft -1 or j == 0) or (j < topleft-1 and (i == 2 * input + 3 or i == topleft)):
                print("#",end="")
            elif (j == (2 * input + 3) - (i - (input + 2)) or j >= topleft) and  j <= (2 * input + 3) - (i - (input + 2)):
                print("+",end="")
            else:
                if j > topleft:
                    print(".",end="")
                if j < topleft and j > 0 and i != 2 * input + 3:
                    print("+",end="")

    print()    