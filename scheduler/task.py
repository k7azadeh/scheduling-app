from tornado.process import task_id


class Task:
    def __init__(self, task_id, name, duration, resource_required, predecessors=None):
        self.task_id = task_id
        self.name = name
        self.duration = duration
        self.resource_required = resource_required
        self.predecessors = predecessors if predecessors is not None else []
        self.start_time = None
        self.end_time = None
        self.remaining_duration = duration

    def __str__(self):
        return f"Task {self.task_id}: {self.name} ({self.duration} units, needs {self.resource_required} resources)"

    def is_ready(self, completed_task_ids):
        return all(pred in completed_task_ids for pred in self.predecessors)
