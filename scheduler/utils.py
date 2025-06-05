import pandas as pd


def load_tasks_from_csv(file_path):
    df = pd.read_csv(file_path)

    # Convert predecessor string to list of ints
    df["predecessors"] = df["predecessors"].fillna("").apply(
        lambda x: list(map(int, x.split("|"))) if x else []
    )

    tasks = df.to_dict(orient="records")
    return tasks