def first_greater(left, right, indexR = 0, indexL = 0):
    if right == []:
        return
    if right[indexR] > left[indexL] and indexL == len(left)-1:
        print("No First Greater Value")
        return first_greater(left, right[1::])
    if right[indexR] < left[indexL]:
        print(left[indexL])
        return first_greater(left, right[1::])
    return first_greater(left, right, 0, indexL+1)
    

inp = input("Enter Input : ").split("/")
left , right = [int(i) for i in inp[0].split()], [int(i) for i in inp[1].split()]
left.sort()
right.sort()
first_greater(left, right)
