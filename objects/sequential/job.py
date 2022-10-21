import subprocess, os
import utils.timer as timer

from utils import errors
from utils.logger import logger


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

    def __init__(self, script=None, name=""):
        self.name: str = name
        self.script = script
        self.return_code = None

    def script_exists(self, path):
        # full_path = os.path.join(os.getcwd(), path)
        return True if os.path.exists(path) else False

    def executes_script(self, file_path):
        command = [f"{ file_path }"]
        execution = subprocess.run(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        return execution.returncode, execution.stdout, execution.stderr

    def execute(self) -> None:
        timer_clock = timer.Timer()
        timer_clock.start()
        if self.script_exists(self.script):
            logger.info(f"[+] Executing { self.name } -> { self.script }")
            # timer_clock.random_delay(0.4)
            return_code, stdout, stderr = self.executes_script(self.script)
            self.return_code = return_code

            logger.info(
                f"[+] '{self.name}' Finished with { self.return_code } ( { timer_clock.endf() } secs)."
            )
            return return_code, stdout, stderr

        message = f"Job script '{ self.script }' of job '{ self.name }' was not found!"
        logger.error(message)
        raise errors.ScriptNotFound(message)
