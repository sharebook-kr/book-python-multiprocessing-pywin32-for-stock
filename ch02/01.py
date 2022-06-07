import sys 
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
import multiprocessing as mp 
import threading


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()



if __name__ == "__main__":
    proc = mp.current_process()
    thread = threading.currentThread().getName()
    print(proc.name, thread)
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()