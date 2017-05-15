import networkx as nx

G = nx.Graph()
G.add_nodes_from('nodes_final.csv')
G.add_edges_from('edges_final.csv')
betweennesscetrality=betweenness_centrality(G)
with open(betweenness_cetrality_measure, 'w') as f:
	for value in betweennesscetrality.items():
		f.write('%s\n' % value)
		