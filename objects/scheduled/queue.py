from objects.scheduled.task import Task


class LeQueue:
    """A couple of tasks"""

    def __init__(self):
        self.all_tasks = {}
        self.started = []

    def register_task(self, task: Task):
        self.all_tasks[len(self.all_tasks.keys()) + 1] = task

    def start(self):
        for id, task in self.all_tasks.items():
            print(f"[**] Task { task.name } loaded...")
            self.started.append(task)
            task.run()
