#!/usr/bin/python3
import schedule 
import time

from sequential.job import Job
from scheduled.task import Task
from sequential.session import Session


class LeQueue:
    """ A couple of tasks """
    def __init__(self):
        self.all_tasks = {}
        self.started = [] 

    def register_task(self, task : Task):
        self.all_tasks[len(self.all_tasks.keys()) + 1] = task 

    def start(self):
        for id, task in self.all_tasks.items():
            print(f"Starting { task.name } task...")
            self.started.append(task)
            task.run()


# demo session
sesion_0 = Session('Session_demo')
sesion_0.init_job = 'U1'
sesion_0.jobs_seq = {
    'U1':[Job('U1', '001.sh'), {0:'U3',1:'U2'}],
        'U2':[Job('U2', '002.sh')],
            'U3':[Job('U3', '003.sh'), {0:'U4'}],
                'U4':[Job('U4', '004.sh')],
}

############################
task_demo = Task('DEMO_TASK', schedule.every(5).seconds)
task_demo.session = sesion_0

main = LeQueue()
main.register_task(task_demo)
main.register_task(task_demo)
main.start()

while True:
    schedule.run_pending()
    time.sleep(0.3)


if __name__ == '__main__':
    pass 