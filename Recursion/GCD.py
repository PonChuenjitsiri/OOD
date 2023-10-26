def GCD(num1, num2):
    if num2 == 0:
        return abs(num1)
    else:
        return GCD(num2 , num1 % num2)
inp = input("Enter Input : ").split()
if int(inp[0]) == 0 and int(inp[1]) == 0:
    print("Error! must be not all zero.")
else:
    if int(inp[0]) > int(inp[1]):
        print(f"The gcd of {inp[0]} and {inp[1]} is : {GCD(int(inp[0]) , int(inp[1]))}")
    else:
        print(f"The gcd of {inp[1]} and {inp[0]} is : {GCD(int(inp[0]) , int(inp[1]))}")