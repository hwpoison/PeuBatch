import schedule
import threading

from objects.sequential.session import Session


class Task:
    """
    A task is a scheduled object that point to a session

    Attributes
    ---------------
    task_name : str
        Task name
    session : Session
        Principal Session to schedule
    schd : schedule
        Schedule lib args
            i.e : https://schedule.readthedocs.io/en/stable/examples.html
    """

    def __init__(self, task_name: str, schd: schedule):
        self.name = task_name
        self.session: Session = None
        self.schd = schd

    def session_thread(self):
        session_thread = threading.Thread(
            target=self.session.run, name=self.session.name
        )
        session_thread.start()

    def run(self):
        self.schd.do(self.session_thread)
