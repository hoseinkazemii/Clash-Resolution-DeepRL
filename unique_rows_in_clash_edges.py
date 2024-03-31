# import pandas as pd

# # Load the CSV files into DataFrames
# clash_edges_df = pd.read_csv("clash_edges.csv", dtype=str)
# edges_df = pd.read_csv("edges.csv", dtype=str)

# # Find the rows that exist in clash_edges.csv but not in edges.csv
# unique_clash_edges_df = clash_edges_df[~clash_edges_df.apply(tuple, axis=1).isin(edges_df.apply(tuple, axis=1))]

# # Display or further process unique_clash_edges_df
# print(len(unique_clash_edges_df))


# import pandas as pd

# # Convert datasets to pandas DataFrames
# df1 = pd.read_csv("clash_edges.csv", dtype=str)
# df1 = df1['Node2']
# df2 = pd.read_csv("mechanical_nodes.csv", dtype=str)
# df2 = df2['Node2']

# df1_sorted = df1.sort_values(by=['Node2']).reset_index(drop=True)
# df2_sorted = df2.sort_values(by=['Node2']).reset_index(drop=True)

# # Find rows in df1_sorted that are not in df2_sorted
# result = df1_sorted[~df1_sorted.isin(df2_sorted)].dropna()

# # Output the result
# print("Rows in Dataset1 that do not exist in Dataset2:")
# print(len(result))



import pandas as pd
df2 = pd.read_csv("mechanical_nodes.csv", dtype=str)
df1 = pd.read_csv("clash_edges.csv", dtype=str)
df1_sorted = df1.sort_values(by=['Node2']).reset_index(drop=True)
df2_sorted = df2.sort_values(by=['Node2']).reset_index(drop=True)

result = df2_sorted[~df2_sorted.isin(df1_sorted)].dropna()
print(len(result))


# print(len(df1['Node2']))