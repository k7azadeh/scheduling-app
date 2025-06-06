import matplotlib.pyplot as plt

def plot_gantt(tasks):
    fig, ax = plt.subplots(figsize=(10, 6))

    for i, task in enumerate(tasks):
        ax.barh(
            y=i,
            width = task.end_time - task.start_time,
            left = task.start_time,
            height = 0.5,
            align = "center",
            edgecolor = "black"
        )
        ax.text(
            task.start_time + 0.1,
            i,
            f"{task.name}",
            va = "center",
            ha = "left",
            fontsize = 9
        )
    ax.set_yticks(range(len(tasks)))
    ax.set_yticklabels([f"Task {task.task_id}" for task in tasks])
    ax.set_xlabel("Time")
    ax.set_title("Gant Chart of Scheduled Tasks")
    plt.tight_layout()
    plt.show()

