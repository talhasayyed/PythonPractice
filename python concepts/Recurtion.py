# recursion of function

import sys

sys.setrecursionlimit(24)
print(sys.getrecursionlimit())

n = 0
def greet():
    global n
    n+=1
    print("greet",n)
    greet()


result = greet()
