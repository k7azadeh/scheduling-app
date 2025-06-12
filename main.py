from scheduler.scheduler import Scheduler
from scheduler.utils import load_tasks_from_csv, load_total_resources
from scheduler.visualization import plot_gantt, plot_resource_utilization

if __name__ == "__main__":
    tasks = load_tasks_from_csv("data/example_tasks.csv","data/example_resources.csv" )
    for task in tasks:
        print(task)
    total_resources = load_total_resources("data/total_resources.csv")
    print(total_resources)
    scheduler = Scheduler(tasks, total_resources)
    scheduler.schedule()

    #plot_gantt(tasks)
    plot_resource_utilization(scheduler.utilization_log, total_resources)
