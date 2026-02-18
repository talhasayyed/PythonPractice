# 43
# filter , map , reduce
# filter use ( function , iterables )
# Eg perform funct to list

from functools import reduce

nums = [1,2,3,4,5,6,7,8,9]
even = list(filter(lambda a: a%2==0,nums))

# map
# map is used to perform 1 operation each iterables
# Eg add 1 to each iterable of list
add1 = list(map(lambda a: a+1,nums))

# Reduce
# Reduce belong to functools module
r = reduce(lambda a,b: a+b, nums)

print('list',nums)
print('filter even',even)
print('map a+1=',add1)
print('reduce a+b',r)