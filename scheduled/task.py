from sequential.session import Session

class Task:
    """ 
        A task is a scheduled object that point to a session

        Attributes
        ---------------
        session : Session
            Principal Session to schedule
        date : None
    """
    def __init__(self, session : Session, schedule : list):
        self.session = None 
        self.date = None

    
    def run(self):
        self.session.run()
        #schedule.every(1).seconds.do(self.session.run)
