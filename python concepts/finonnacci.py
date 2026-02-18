# python fibonacci

fibonacci = int(input("enter number for fibonacci: "))
i=1 #index
while fibonacci >= 0:

    a = 0
    b = 1

    if fibonacci == 0:
        print(i,"index",fibonacci)
    else:
        print(i,"index",0)
        i+=1 # index number increment
        print(i,"index",1)
    for i in range(2,fibonacci):
        i+=1 # index number increment
        c = a + b
        a = b
        b = c
        print(i,"index",c)

    print("bye")
    break


