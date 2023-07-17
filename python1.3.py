print(" *** Summation of each digit ***")
num = input("Enter a positive number : ")
res = 0
for i in num:
    res += int(i)
print("Summation of each digit = ",res)