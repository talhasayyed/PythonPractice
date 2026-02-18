# Generator using yield
# when it is used ?
# u r fetching 1000 records from DB but u want 1 value at a time
def topten():
    # This is not possible with return
    yield 1
    yield 2
    yield 3

value = topten()

print(value.__next__())
# or
print(next(value))
print(next(value))