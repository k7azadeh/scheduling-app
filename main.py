from scheduler.utils import load_tasks_from_csv

if __name__ == "__main__":
    tasks = load_tasks_from_csv("data/example_tasks.csv")
    for task in tasks:
        print(task)