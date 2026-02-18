class Pycharm:
    def execute(self):
        print('compiler start')

class Laptop:
    def code(self,ide):
        print('laptop start')
        ide.execute()

ide = Pycharm()

l1 = Laptop()
l1.code(ide)