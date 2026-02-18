


def SelectionSort(lst):
    for i in range(len(list)):
        minpos = i
        for j in range(i,len(list)):
            if list[i]>list[j]:
                minpos = j
        # swap(list[i],list[minpos])
        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp


# def swap(a,b):
#     a,b=b,a
#     return a,b

list = [9,7,8,5,6,4,2,3,1]
SelectionSort(list)

print(list)