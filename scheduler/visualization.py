import matplotlib.pyplot as plt
import pandas as pd

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

def plot_resource_utilization(utilization_log, total_resources):
    df = pd.DataFrame(utilization_log)
    time = df["time"]
    resource_names = [col for col in df.columns if col != "time"]

    num_resources = len(resource_names)

    fig, axes = plt.subplots(num_resources,1, figsize=(10,2.5*num_resources), sharex=True)

    if num_resources ==1:
        axes = [axes]

    for i, res in enumerate(resource_names):
        total = total_resources[res]
        absolute = df[res]
        percent_used = df[res] / total_resources[res] * 100

        ax1 = axes[i] #primary y axis
        ax2 = ax1.twinx() #secondary y axis

        # Bar chart on left axis (percent)
        bars = ax1.bar(time, percent_used, label=f"{res} usage (%)", color='skyblue')
        ax1.axhline(100, color='red', linestyle='--', label="Max capacity")
        ax1.set_ylabel(f"{res} (% used)")
        ax1.set_ylim(0, 110)
        #axes[i].legend(loc="upper right")
        ax1.grid(True, axis='y')

        #Rigt y axis (actual valus)

        ax2.set_ylabel(f"{res} (used out of {total})", color = 'grey')
        ax2.set_ylim(0, total * 1.1)
        ax2.tick_params(axis='y', color = 'grey')

        # Sync the bar heights on right axis using absolute values (for reference ticks)
        ax2.set_yticks(range(0, total + 1))

        #legend
        ax1.legend(loc="upper right")

    axes[-1].set_xlabel("Time")
    plt.suptitle("Resource Utilization Over Time (%)")
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()

