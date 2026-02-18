# Comparing obj, Operator Overloading (Polymorphism)
# same operator name but arguments or the type of arguments is different
class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    #   Overloading + Operator
    def __add__(self,others):
        m1 = self.m1 + others.m1
        m2 = self.m2 + others.m2
        s3 = Student(m1,m2)
        return s3

    #   Overloading > Operator
    def __gt__(self,other): # (s1,s2)
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    # to Print object value
    #   Overloading __str__
    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)

s1 = Student(12,10)
s2 = Student(10,23)

s3 = s1 + s2    # + ==> Student.__add__(s1,s2)

if s1 > s2:
    print('s1 wins')
else:
    print('s2 wins')

# printing obj s3
print(s3)