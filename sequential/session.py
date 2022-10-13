import utils.timer as timer

class Session:
    """
    A session is a sequential object that containsa chain of Jobs.

    Attributes
    ------------
    name : str
        Session name
    init_job : str 
        First Job
    job_seq : dict
        Job chain

    Methods
    ------------
    run_job(job_name=None)
        Run a job by his name
    start()
        Start the Session at the first job
    """
    def __init__(self, name):
        self.name = name 
        self.init_job = 'U1' # default value
        self.jobs_seq = {

        }

    def run_job(self, job_name) -> None: 
        job_ =  self.jobs_seq[job_name]
        job = job_[0]
        ribb = job_[1] if len(job_)>1 else None

        return_code = job.execute()
        
        if ribb is None:
            return True

        if next_job := ribb.get(return_code):
            print(f"Next job is { next_job }")
            self.run_job(next_job)
        
    def start(self):
        timer_clock = timer.Timer()
        timer_clock.start()
        print(f"[+] Running { self.name }...") 
        self.run_job(self.init_job)
        print(f"[*] Session '{ self.name }' finished in { timer_clock.end() }")
    