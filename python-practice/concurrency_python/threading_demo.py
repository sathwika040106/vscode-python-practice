import threading
import time


def task():
    for i in range(5):
        print(f"Thread Running {i + 1}")
        time.sleep(1)


thread = threading.Thread(target=task)

thread.start()

thread.join()

print("Main Program Finished")