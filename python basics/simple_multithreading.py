import threading
import time

stopper = False

def worker(text):
    counter = 0
    while not stopper:
        print(f'{text} {counter}\n')
        time.sleep(1)
        counter += 1

# daemon True means thread will run in backgrouund and only stop if all the thread is stopped
t1 = threading.Thread(target=worker, daemon=False, args=('talha',))
t2 = threading.Thread(target=worker, daemon=False, args=('ikrama',))

t1.start()
t2.start()


## if you use join thread will wait for all joined thread to finish,
## in our case both are while loop and exit condition is outside of thread, so it will not stop if joined
# t1.join()
# t2.join()

input('Enter to quit')
