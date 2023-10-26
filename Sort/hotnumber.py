def convert_list_to_tuple(lst, list_tuple = [], tuple = ()):
    if len(tuple) == 2:
        list_tuple.append(tuple)
        return convert_list_to_tuple(lst, list_tuple, ())
    if lst == []:
        return list_tuple
    tuple += (lst.pop(0),)
    return convert_list_to_tuple(lst, list_tuple, tuple)

def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

def get_hotnumber(lst, start = 0, Count_index = 1, hotnumber_list = []):
    if start == len(lst):
        return hotnumber_list
    if Count_index == len(lst):
        return get_hotnumber(lst, start + 1, 0, hotnumber_list)
    if lst[start][0] > lst[Count_index][0] and lst[start][1] < lst[Count_index][1]:
        hotnumber_list.append(lst[start])
        hotnumber_list.append(lst[Count_index])
    return get_hotnumber(lst, start, Count_index + 1, hotnumber_list)

def sum_Ai(lst, sum = 0):
    if lst == []:
        return sum
    sum += lst[0][0]
    return sum_Ai(lst[1::], sum)

inp = [int(i) for i in input("input : ").split()]
list_tuple = convert_list_to_tuple(inp)
mergeSort(list_tuple)
list_tuple.reverse()
print(f"ans = {sum_Ai(get_hotnumber(list_tuple))}")

