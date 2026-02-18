# global and globals keywords

a = 1
b = 2

def fun_global():
    global a
    print(a,"global a inside fun_gloabal()")
fun_global()

print("===================================================")

def fun_globals():
    a = 6
    b = 7
    print(a,b,"loval a,b inside fun_globals()")
    # to access multiple global variable
    a = globals()["a"]
    b = globals()["b"]
    print(a,b,"global a,b inside fun_globals()")
fun_globals()
