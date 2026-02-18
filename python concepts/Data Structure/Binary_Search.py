# binary search

#      [0][1]......[7]
list0 = [1,7,3,8,5,6,9]
list = sorted(list0)
n = 6       # Search Value
pos = 0


def search(list,n):
    lowerLim = 0
    upperLim = len(list)-1

###     using while loop
    while lowerLim <= upperLim:
        mid = (lowerLim + upperLim) // 2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                lowerLim = mid
            else:
                upperLim = mid
    return False




###     using for loop

    # for i in list:
    #     if i == n:
    #         return True
    #
    # return False


if search(list,n):
    print('fount',n,'at pos=',pos+1)
else:
    print('not found')