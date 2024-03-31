import pandas as pd
import pickle


def load_nodes(**params):
    data_directory = params.get("data_directory")
    nodes_file_directory = params.get("nodes_file_directory")

    print("loading the nodes from csv files...")

    df_structural = pd.read_csv(f"{data_directory}/Structural.csv", dtype=str)
    df_mechanical = pd.read_csv(f"{data_directory}/Mechanical.csv", dtype=str)

    return df_structural, df_mechanical

'''''''''
    print("unpickling the nodes...")

    with open(nodes_file_directory, 'rb') as f:
        return pickle.load(f)
'''''''''