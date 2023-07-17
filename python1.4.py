print("*** Fun with Drawing ***")
input = int(input("Enter input : "))

# for i in range(input):
#     for j in range(((input)*2)-1): # 9 --> [0,1,2,3,4,5,6,7,8,9]
#         # print(j)
#         # print((input - 2) + i)
#         if j < (input-(i+1)) and j > (input-(i+1)):
#             print(".",end="")
#         if j == (input-(i+1)) or j == ((input - 1) + i):
#             print("*",end="")
#     print()

y1 = input - 1
y2 = input + (2 * input - 3)
y3 = 1
y4 = 4 * input - 5

for i in range(input + 2 * input - 2):
    for j in range(4 * input - 3):
        if i < input:
            if j == y1 - i or j == y1 + i or j == y2 - i or j == y2 + i :
                print("*",end="")
            elif j > y1 - i and j < y1 + i or (j > y2 - i and j < y2 + i):
                print("+",end="")
            else: print(".", end="")
        else:
            if j == y3 + (i - input) or j == y4 - (i - input):
                print("*",end="")
            elif j > y3 + (i - input) and j < y4 - (i - input):
                print("+",end="")
            else: print(".", end="")
    print()
    
