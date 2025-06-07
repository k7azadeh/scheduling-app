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

def extract_resources_from_df(df_resources):
    resource_columns = df_resources.columns.drop("task_id")
    df_resources["resource_required"] = df_resources.apply(
        lambda row: {
            res: int(row[res])
            for res in resource_columns
            if int(row[res]) > 0
        },
        axis=1
    )
    return df_resources[["task_id", "resource_required"]]


def load_tasks_from_csv(file_path_task, file_path_resource):
    df_task = pd.read_csv(file_path_task)
    df_resources = pd.read_csv(file_path_resource)

    # Convert predecessor string to list of ints

    df_task["predecessors"] = df_task["predecessors"].fillna("").apply(parse_predecessors)
    # df["predecessors"] = df["predecessors"].fillna("").apply(
    #     lambda x: [int(p.strip()) for p in str(x).split(",") if p.strip().isdigit()]
    # )

    # extract resources clean
    df_resources_clean = extract_resources_from_df(df_resources)

    df = df_task.merge(df_resources_clean, on="task_id")

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