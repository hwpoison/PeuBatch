import utils.timer as timer
import time
import random

class Job:
    """
        A job is a simple job that run a script and return a status code.

        Attributes
        -----------------
        script : string
        return_code : int

        Methods
        -----------------
        execute() -> None
            Run the default script

    """
    def __init__(self, name, script=None):
        self.name : str = name
        self.script = script
        self.return_code = None

    def execute(self) -> None:
        timer_clock = timer.Timer()
        timer_clock.start()
        if self.script:
            print(f"[+] Executing { self.name } -> { self.script }")
            timer_clock.random_sleep(0.4)
            self.return_code = 0 
            print(f"[+] '{self.name}' Finished with { self.return_code } ( { timer_clock.endf() } secs).")
            return self.return_code
            
        return self.return_code
