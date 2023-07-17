print("*** String Rotation ***")
string1,string2 = input("Enter 2 strings : ").split()
str1rotate = string1
str2rotate = string2
count = 1
def leftrotate(s, d):
    tmp = s[d : ] + s[0 : d]
    return tmp
   
def rightrotate(s, d):
   return leftrotate(s, len(s) - d)

while True:
    str1rotate = rightrotate(str1rotate,2)
    str2rotate = leftrotate(str2rotate,3)

    if str1rotate == string1 and str2rotate == string2:
        print(count,end=" ")
        print(str1rotate,end=" ")
        print(str2rotate)
        print("Total of  {} rounds.".format(count))
        break
    else :  
        if count <= 5:
            print(count,end=" ")
            print(str1rotate,end=" ")
            print(str2rotate)
        count += 1
        if count == 6:
            print(" . . . . . ")
