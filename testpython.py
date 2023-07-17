class MyInt():
    def __init__(self,value):
        self.value = value
        self.int_in_value = value
        self.dict_roman ={
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',   
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I',
        }

    def toRoman(self):
        temp =''
        for key,symbol in self.dict_roman.items():
            while self.value >= key:
               temp += symbol
               self.value -= key
        return temp
    
    def __add__(self,other):
        new_value = (self.int_in_value+other)*1.5
        return int(new_value)
    
    def toInteger(self):
        return self.int_in_value
    
num1,num2 = input(' *** class MyInt ***\nEnter 2 number : ').split()
a = MyInt(int(num1))
b = MyInt(int(num2))
print(f'{num1} convert to Roman : {a.toRoman()}')
print(f'{num2} convert to Roman : {b.toRoman()}')
print(f'{num1} + {num2} = {a+b.toInteger()}')