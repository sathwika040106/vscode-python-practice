import threading
import time


def work():
    time.sleep(2)


# Sequential
start = time.time()

work()
work()

print("Sequential:", round(time.time() - start, 2), "seconds")


# Multithreading
start = time.time()

t1 = threading.Thread(target=work)
t2 = threading.Thread(target=work)

t1.start()
t2.start()

t1.join()
t2.join()

print("Multithreading:", round(time.time() - start, 2), "seconds")