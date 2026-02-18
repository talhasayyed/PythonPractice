# Multithreading
# and time module

from threading import *
from time import sleep

class Hello(Thread):
    def run(self):      # Inbuild function of thread
        for i in range(5):
            print('Hello')
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print('hi')
            sleep(1)

t1 = Hello()
t2 = Hi()

t1.start()      # It use start instead of run
sleep(0.2)
t2.start()

# for print bye at the end of t1 t2
t1.join()
t2.join()

print('bye')