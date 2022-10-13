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
    
    def register_task(self, task : Task):
        self.all_tasks[task] = task 

    def start(self):
        for id, task in self.all_tasks:
            print(id, task)


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
# demo task , that uses the demo session
task_demo = Task('DEMO_TASK', ['every','day', '10:30'])
task_demo.session = sesion_0
task_demo.session.start()

main = LeQueue()
main.register_task(task_demo)

#####
schedule.every(2).seconds.do(task_demo.session.start)

while True:
    schedule.run_pending()
    time.sleep(1)


if __name__ == '__main__':
    pass 