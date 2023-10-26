def Simplesqrt(lst, x):
    if len(lst) == 1:
        return lst[0]
    if lst[int(len(lst)/2)] * lst[int(len(lst)/2)] == x:
        return lst[int(len(lst)/2)]
    if lst[int(len(lst)/2)] * lst[int(len(lst)/2)] < x:
        return Simplesqrt(lst[int(len(lst)/2)::], x)
    return Simplesqrt(lst[:int(len(lst)/2):], x)

def squareRoot(number):
    ans = Simplesqrt([i for i in range(0,int(number)+1)], number)
    increment = 0.1
    for i in range(0, 5):
        while (ans * ans <= number):
            ans += increment
        ans = ans - increment
        increment = increment / 10

    return round(ans,6)

def distanceCal(start, end):
    return squareRoot(((start[0] - end[0])** 2) + ((start[1] - end[1])** 2))

def ConnectDaDot(start, point, dummy = []):
    if len(point) == 0: return
    for i in point:
        dummy.append(float(distanceCal(start, i)))
    distance = "{:.4f}".format(round(min(dummy), 4))
    print(f"{start} -> {point[dummy.index(min(dummy))]} | The distance is {distance}")
    return ConnectDaDot(point.pop(dummy.index(min(dummy))), point, [])

lst = input("Enter a list of points: ").split("/")
groups = lst[0].split(",")
point = []
start = [float(i) for i in lst[1].split()]
for group in groups:
    values = group.split()
    inner_list = [float(value) for value in values]
    point.append(inner_list)
if start not in point: print(f"{start} is not in {point}")
else:
    point.remove(start)
    ConnectDaDot(start, point)




