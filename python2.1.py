class Calculator :

    ### Enter Your Code Here ###
    def __init__(self,value):
        self.value = value

    def __add__(self,num):
        ###Enter Your Code For Add Number###
        return self.value + num.value
    
    def __sub__(self,num):
        ###Enter Your Code For Sub Number### 
        return self.value - num.value

    def __mul__(self,num):
        ###Enter Your Code For Mul Number###
        return self.value * num.value

    def __truediv__(self,num):
        ###Enter Your Code For Div Number###
        return self.value / num.value

x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))

print(x+y,x-y,x*y,x/y,sep = "\n")