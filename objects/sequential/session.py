import sys

import utils.timer as timer
from utils.logger import logger


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
        self.init_job = "U1"  # default value
        self.jobs = {}

    def run_job(self, job_name) -> None:
        job_ = self.jobs[job_name]
        job = job_[0]
        job.name = job_name
        ribb = job_[1] if len(job_) > 1 else None

        return_code, output, stderr = job.execute()

        logger.info(f"Executing {job.script} .....")
        if output:
            logger.debug(f"\n{ str(output, 'utf-8') }")
        if stderr:
            logger.error(f"\n{ str(stderr, 'utf-8') }")

        if ribb is None:
            return True
        if return_code > 1:
            return False

        if next_job := ribb.get(return_code):
            logger.info(f"Next job is { next_job }")
            self.run_job(next_job)

    def run(self):
        timer_clock = timer.Timer()
        timer_clock.start()

        logger.info("")
        logger.info(f" ||    Running session '{self.name}   ||")
        try:
            return_ = self.run_job(self.init_job)
            if return_ is False:
                logger.error("Job finish in error.")
                logger.error(
                    f"Aborting Session '{ self.name }' finished in { timer_clock.end() }"
                )
                return False
        except Exception as error:
            error = sys.exc_info()
            logger.debug(error)
            logger.error(
                f"Aborting Session '{ self.name }' finished in { timer_clock.end() }"
            )
            logger.info(f" ||    End of session '{self.name}   ||")
            return False

        logger.info(f"Session '{ self.name }' finished in { timer_clock.end() }")
        logger.info(f" ||    End of session '{self.name}   ||")

        return True
