# coding:utf-8
from artlog import *
import artssh
# import models
import threading
import time


class openthread():
    def __init__(self,func,threadtime):
        self.func = func
        self.threadtime = threadtime
        self.stop = threading.Event()
        self.new_thread = threading.Thread(target=func, args=(self.threadtime,self.stop))
    def start_thread(self):
        self.new_thread.start()
        self.new_thread.join()
    def stop_thread(self):
        self.stop.set()

        # def thread1(arg1, stop_event):
        #     while (not stop_event.is_set()):

def collectMCinfo(argtime,stop_event):
    info("messages.log", "The thread has been started.")
    while (not stop_event.is_set()):
        info("messages.log", "10seconds passed")
        time.sleep(argtime)



def artop():
    mcDATA = {}

    return mcDATA


def mcAlertCheck():
    mcAlertDATA = {}
    return mcAlertDATA

if __name__ == '__main__':
    new_connector = openthread(collectMCinfo,10)
    new_connector.start_thread()
