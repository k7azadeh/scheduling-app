import pandas as pd
from scheduler.task import Task


def parse_predecessors(x):
    parts = str(x).split(",")
    valid = []
    for p in parts:
        p_clean = p.strip()
        if p_clean.isdigit():
            valid.append(int(p_clean))
        elif p_clean:  # not empty, but not valid
            print(f"⚠️ Warning: Ignored invalid predecessor '{p_clean}'")
    return valid


def load_tasks_from_csv(file_path):
    df = pd.read_csv(file_path)

    # Convert predecessor string to list of ints

    df["predecessors"] = df["predecessors"].fillna("").apply(parse_predecessors)
    # df["predecessors"] = df["predecessors"].fillna("").apply(
    #     lambda x: [int(p.strip()) for p in str(x).split(",") if p.strip().isdigit()]
    # )

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