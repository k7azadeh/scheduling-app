import pandas as pd
from scheduler.task import Task



def load_tasks_from_csv(file_path):
    df = pd.read_csv(file_path)

    # Convert predecessor string to list of ints
    df["predecessors"] = df["predecessors"].fillna("").apply(
        lambda x: list(map(int, x.split("|"))) if x else []
    )

    tasks =[]
    for row in df.to_dict(orient="records"):
        task= Task(
            task_id=row["task_id"],
            name = row["task_name"],
            duration = row["duration"],
            resource_required = row["resource_required"],
            predecessors = row["predecessors"]
        )
        tasks.append(task)
    return tasks