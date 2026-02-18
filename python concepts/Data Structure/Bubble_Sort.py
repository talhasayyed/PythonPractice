
# bubble sort start from end placing highest at end

list = [7,5,3,1,2,6,4,9,8]

print(list)
def BubbleSort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                list[j], list[j + 1] = list[j+1], list[j]   # swap


BubbleSort(list)
print(list,' sorted')