import threading
import time


def background_task():
    while True:
        print("Running Background Task...")
        time.sleep(2)


thread = threading.Thread(target=background_task, daemon=True)

thread.start()

time.sleep(6)

print("Main Program Finished")