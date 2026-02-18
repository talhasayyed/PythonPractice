# Method Overriding
# changing same name method in child class

class A:
    def show(self):
        print('in Show A')

class B(A):
    # pass
    def show(self):
        print('in Show B')

b = B()
b.show()