# break
available = 20
reqCandy = int(input("how much candy u want: "))
i = 1
while i <= reqCandy:
    if i>available:
        print("out of stock, we had only ", available,"candy")
        break
    print(i,"candy!")
    i+=1
