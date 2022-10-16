import time
import random 

class Timer:
    def __init__(self, show_log=False):
       self.start_time = None 
       self.show_log = show_log

    def start(self):
        self.start_time = time.time() 
    
    def end(self):
        if self.start_time is None:
            self.log(f"Timer is not started!")
            return False

        total = time.time() - self.start_time 
        self.log(f"Finished in { total } secs")
        return total

    def endf(self):
        total = time.time() - self.start_time 
        return '{:.2f}'.format(total)
        
    def log(self, msg):
        if self.show_log:
            print(msg)

    # simulate delay
    def random_delay(self, max=0.2):
        time.sleep(random.uniform(0.2, max)) 

    def get_timestamp(self):
        return time.time()