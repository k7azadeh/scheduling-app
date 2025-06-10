

class Scheduler:
    def __init__(self, tasks, total_resources):
        self.tasks = tasks
        self.total_resources = total_resources
        self.time = 0
        self.scheduled_tasks = []
        self.in_progress = []
        self.completed_tasks = []
        self.make_span = 0


    def schedule(self, verbose=False):
        print("Starting Scheduling...")
        while len(self.completed_tasks) < len(self.tasks):
            #move completed tasks
            for task in self.in_progress[:]:
                task.remaining_duration -=1
                if task.remaining_duration == 0:
                    task.end_time = self.time
                    self.in_progress.remove(task)
                    self.completed_tasks.append(task)
                    if verbose:
                        print(f"Completed: {task}")
            available_resources = self.get_available_resources()
            # available_resources = self.total_resources - sum(t.resource_required for t in self.in_progress)

            if verbose:
                print(f"time:{self.time}")
                for task in self.in_progress:
                    print(f"{task.name}")
                print(f" in progress")
                print(f"Available resources: {available_resources}")


            completed_ids = [t.task_id for t in self.completed_tasks]

            #Start new ready tasks if resources are available
            for task in self.tasks:
                if task.start_time is None and task.is_ready(completed_ids):
                    if verbose:
                        print(f"predecessors of {task.name} have been completed and task is not in progress")
                    if self.can_start(task, available_resources):
                        if verbose:
                            print(f"there are enough resources available to start {task.name}")
                        task.start_time = self.time
                        self.in_progress.append(task)
                        self.scheduled_tasks.append(task)
                        for res, amount in task.resource_required.items():
                            available_resources[res] -= amount
                        if verbose:
                            print(f"Started: {task.name}")
            self.time += 1

        self.make_span = max([t.end_time for t in self.completed_tasks])
        print("Scheduling complete!")
        print("\nFinal schedule:")
        for task in self.tasks:
            print(f"{task.name}: starts at {task.start_time}, ends at {task.end_time}")
        print(f"Total makespan is: {self.make_span}")

    def get_available_resources(self):
        available_resource = self.total_resources.copy()
        for task in self.in_progress:
            for res, amount in task.resource_required.items():
                available_resource[res] -= amount
        return available_resource

    def can_start(self, task, available_resources):
        for res, amount in task.resource_required.items():
            if available_resources.get(res, 0) < amount:
                return False
        return True
