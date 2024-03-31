

def save_clash_edges(clash_edges_df, **params):
    data_directory = params.get("data_directory")
    clash_edges_file = params.get("clash_edges_file")

    print("exporting clash edges into a csv file...")

    clash_edges_df.to_csv(f"{data_directory}{clash_edges_file}.csv", index=False)
