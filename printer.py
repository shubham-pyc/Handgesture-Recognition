from threading import Thread,Lock
import sys,time
class Printer:
    def __init__(self):
        self.message  = None
        self.stopped = False
        self.lock = Lock()
    def keep_printing(self):
        while not self.stopped:
            if self.message is not  None:
                self.lock.acquire()
                sys.stdout.write('\r'+self.message)
                sys.stdout.flush()
                self.message = None
                time.sleep(0.3)
                self.lock.release()
    def start(self):
        Thread(target=self.keep_printing,args=()).start()
        return self
    def stop(self):
        self.stopped = True
    def change_line(self):
        self.message = "\n"