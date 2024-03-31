import pandas as pd

def load_edges(**params):
    data_directory = params.get("data_directory")
    clash_edges_file = params.get("clash_edges_file")

    print("loading clash edges from csv file...")

    df_clash_edges = pd.read_csv(f"{data_directory}{clash_edges_file}.csv", dtype=str)

    return df_clash_edges