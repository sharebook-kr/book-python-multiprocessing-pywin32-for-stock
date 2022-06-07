import multiprocessing as mp
import threading 


def worker():
    print("worker function")
    print(mp.current_process().name, threading.currentThread().getName())


if __name__ == "__main__":
    print("hello world")
    print(mp.current_process().name, threading.currentThread().getName())

    proc = mp.Process(name="SubProcess", target=worker)
    proc.start()