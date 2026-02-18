
# Generator using yield
# when it is used ?
# u r fetching 1000 records from DB but u want 1 value at a time
def topten():
    # This is not possible with return
    n = 1
    while n<=10:
        sq = n*n
        yield sq    # yield can b used multiple time unlike return
        n += 1

value = topten()

for i in value:
    print(i)