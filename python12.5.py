class MyInt():
    def __init__(self, num):
        self.num = num

    def toRoman(self):
        res = ""
        copy = self.num
        sym = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        i=0
        while copy>0:
            res += sym[i]*(copy//val[i])
            copy -= val[i]*(copy//val[i])
            i+=1
        return res
    
    def __add__(self, other):
        return int((self.num + other.num)*1.5)

num1,num2 = input(' *** class MyInt ***\nEnter 2 number : ').split()
a = MyInt(int(num1))
b = MyInt(int(num2))
print(f'{num1} convert to Roman : {a.toRoman()}')
print(f'{num2} convert to Roman : {b.toRoman()}')
print(f'{num1} + {num2} = {a+b}')

