from ._extract_nodes_and_relationships import extract_nodes_and_relationships
from ._save_nodes import save_nodes
from ._extract_clash_edges import extract_clash_edges
from ._save_clash_edges import save_clash_edges
from ._load_nodes import load_nodes
from ._load_edges import load_edges
from ._match_nodes_and_create_edges import match_nodes_and_create_edges
from ._create_node_embedding import create_node_embedding


class PreprocessData():

	def __init__(self, **params):
		
		for k, v in params.items():
			setattr(self, k, v)
		

	def _load_and_preprocess_data(self, **kwargs):

		# Step-1: Loading the ifc nodes from ifcxml files and pickling them
		# df_structural, df_mechanical\
		# 	   = extract_nodes_and_relationships(**self.__dict__)
		# save_nodes(df_structural, df_mechanical, **self.__dict__)
		# df_clash_edges = extract_clash_edges(**self.__dict__)
		# save_clash_edges(df_clash_edges, **self.__dict__)

		# Step-2: Loading the saved (pickled) ifc nodes
		df_structural, df_mechanical = load_nodes(**self.__dict__)
		df_clash_edges = load_edges(**self.__dict__)
		G = match_nodes_and_create_edges(df_structural, df_mechanical, df_clash_edges, **self.__dict__)
		create_node_embedding(G, **self.__dict__)
