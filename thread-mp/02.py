import multiprocessing as mp
import threading 

proc = mp.current_process()
thread = threading.currentThread()

print("PROCESS: ", proc.name)
print("THREAD : ", thread.getName())
print("hello world")