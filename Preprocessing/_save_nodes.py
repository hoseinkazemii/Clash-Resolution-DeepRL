import pickle

def save_nodes(df_structural, df_mechanical, **params):
    data_directory = params.get("data_directory")
    
    print("saving the nodes with tags into csv files...")
    
    df_structural.to_csv(f"{data_directory}/Structural.csv", index=False)
    df_mechanical.to_csv(f"{data_directory}/Mechanical.csv", index=False)


    '''''
    # Pickling the extracted elements
    nodes = {"structural_types_and_elements": structural_types_and_elements,
             "mechanical_types_and_elements": mechanical_types_and_elements}
    
    with open("./Data/nodes.pkl", 'wb') as f:
        pickle.dump(nodes, f)
    '''''