# Iterator for memory management in loop
# is used in conditon
# just want one value at a time


class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <=20:
            vals = self.num
            self.num += 1
            return vals
        else:
            raise StopIteration

Values = TopTen()
for i in Values:
    print(i)