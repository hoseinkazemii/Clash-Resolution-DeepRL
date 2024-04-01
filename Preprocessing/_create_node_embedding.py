# from node2vec import Node2Vec



def create_node_embedding(G, **params):


    print("creating graph embedding...")

    # Generate walks
    node2vec = Node2Vec(G, dimensions=64, walk_length=30, num_walks=200, workers=1)

    # Train node2vec model
    model = node2vec.fit(window=10, min_count=1, batch_words=4)

    # Obtain the embeddings
    node_embeddings = {node: model.wv[node] for node in G.nodes()}

    print(node_embeddings)
    raise ValueError
    # Now node_embeddings contains the embedding vectors for each node in the graph G
    # You can use these embeddings for further analysis or tasks such as clash resolution.

# Example usage of node embeddings
# For example, to get the embedding of a specific node:
# print(node_embeddings['IfcWall1'])

# Further analysis or tasks using embeddings can be performed here