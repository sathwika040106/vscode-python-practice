from multiprocessing import Process
import time


def worker():
    for i in range(5):
        print("Processing", i + 1)
        time.sleep(1)


if __name__ == "__main__":

    p = Process(target=worker)

    p.start()

    p.join()

    print("Process Finished")