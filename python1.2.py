print("*** multiplication or sum ***")
num1,num2 = input("Enter num1 num2 : ").split()
num1,num2 = int(num1),int(num2)
if (num1 * num2) > 1000:
    print("The result is",num1 + num2)
else:print("The result is",num1 * num2)