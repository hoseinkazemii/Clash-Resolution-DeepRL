import matplotlib.pyplot as plt
import networkx as nx



def _visualize_graph(G, **params):

    # Draw graph using spring layout
    pos = nx.random_layout(G)
    # Separate nodes by bipartite attribute
    top_nodes = {n for n, d in G.nodes(data=True) if d["bipartite"] == 0}
    bottom_nodes = set(G) - top_nodes
    # Draw edges with narrower width
    nx.draw_networkx_edges(G, pos, width=0.01, edge_color='gray', alpha=0.5)
    # Draw nodes and edges
    nx.draw_networkx_nodes(G, pos, nodelist=top_nodes, node_color="b", label="Structural", node_size=0.01, node_shape="o")
    nx.draw_networkx_nodes(G, pos, nodelist=bottom_nodes, node_color="r", label="Mechanical", node_size=0.01, node_shape="o")
    nx.draw_networkx_edges(G, pos)
    # Display legend
    plt.legend()
    # Display
    plt.show()