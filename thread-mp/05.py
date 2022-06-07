import multiprocessing as mp
import threading 
import time


def worker():
    print("worker function start")
    print(mp.current_process().name, threading.currentThread().getName())
    time.sleep(10)
    print("worker function end")


if __name__ == "__main__":
    print("main start")
    print(mp.current_process().name, threading.currentThread().getName())
    proc = mp.Process(name="SubProcess", target=worker)
    proc.start()
    print("main end")