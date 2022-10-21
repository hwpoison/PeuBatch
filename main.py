#!/usr/bin/python3
import schedule, time

from objects.sequential.job import Job
from objects.scheduled.task import Task
from objects.sequential.session import Session
from objects.scheduled.queue import LeQueue


# Batch follows next hierarchy: LeQueue(Task(Session(Job)))
# Job: Minimal Unity (a simple script execution)
# ---> Session: A couple of conditionated Jobs
# -----> Task: A plannified Session
# --------> LeQueue: A couple of Sessions


# Session
sesion_0 = Session("Session_demo")
sesion_0.init_job = "U1"
sesion_0.jobs = {
    # Session design
    "U1": [Job("./scripts/test/job_1_OK.sh"), {0: "U3", 1: "U2"}],
    "U2": [Job("./scripts/test/job_3_custom_return.sh")],
    "U3": [Job("./scripts/test/job_error.sh"), {0: "U4"}],
    "U4": [Job("004.sh")],
}

# Task
task_demo = Task("DEMO_TASK", schedule.every(1).seconds)
task_demo.session = sesion_0

# Main Loop
if __name__ == "__main__":
    main = LeQueue()
    main.register_task(task_demo)
    main.start()

    while True:
        schedule.run_pending()
        time.sleep(0.3)
