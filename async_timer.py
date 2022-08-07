from threading import Thread
import time



class AsyncTimer:
    is_running = False

    def __init__(self, func, args_list = []):
        self.func = func
        self.args_list = args_list

    def start(self, time):
        self.time = time
        self.is_running = True
        
        self.executing_thread = Thread(target = self.executing, args = [])
        self.executing_thread.start()
    
    def executing(self):
        while self.is_running:
            self.func_thread = Thread(target = self.func, args = self.args_list)
            self.func_thread.start()
            time.sleep(self.time) # * 0.96
    
    def stop(self):
        self.is_running = False
