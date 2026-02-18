# linear search

#      [0][1]......[7]
list = [1,7,3,8,5,6,9]
n = 6
position = -1
def search(list,n):
    i = 0

###     using while loop
    while i<=len(list):     # [0][1]....[7]
        if list[i] == n:
            globals() ['position'] = i
            return True
        i += 1
    return False


###     using for loop

    # for i in list:
    #     if i == n:
    #         return True
    #
    # return False


if search(list,n):
    print('fount',n,'at pos=',position)
else:
    print('not found')