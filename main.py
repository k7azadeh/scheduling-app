from scheduler.scheduler import Scheduler
from scheduler.utils import load_tasks_from_csv, load_total_resources
from scheduler.visualization import plot_gantt

if __name__ == "__main__":
    tasks = load_tasks_from_csv("data/example_tasks.csv","data/example_resources.csv" )
    for task in tasks:
        print(task)
    total_resources = load_total_resources("data/total_resources.csv")
    print(total_resources)
    scheduler = Scheduler(tasks, total_resources)
    scheduler.schedule()

    print("\nFinal schedule:")
    for task in tasks:
        print(f"{task.name}: starts at {task.start_time}, ends at {task.end_time}")
    #
    # plot_gantt(tasks)