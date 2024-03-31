import networkx as nx
import pandas as pd

def match_nodes_and_create_edges(df_structural, df_mechanical, df_clash_edges, **params):

    print("matching the nodes from structural and mechanical nodes and tags; creating the edges based on Navisworks export...")

    # Create a graph
    G = nx.Graph()

    # Add nodes from df_structural and df_mechanical
    structural_nodes = df_structural['Tag'].astype(str).tolist()
    mechanical_nodes = df_mechanical['Tag'].astype(str).tolist()

    # Add structural nodes
    G.add_nodes_from(structural_nodes, bipartite=0)
    # Add mechanical nodes
    G.add_nodes_from(mechanical_nodes, bipartite=1)

    # Add edges from df_clash_edges
    edges = []
    # Add edges from clash_edges data
    i=0
    for _, row in df_clash_edges.iterrows():
        node1 = row['Node1']
        node2 = row['Node2']
        status = row['Status']
        
        # Check if both nodes exist in the graph
        if node1 in G.nodes() and node2 in G.nodes():
            G.add_edge(node1, node2, status=status)

    return G
