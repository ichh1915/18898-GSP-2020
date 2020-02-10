Undirected Tree
import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,5)
G.add_edge(4,6)
G.add_edge(1,6)
G.add_edge(2,6)
G.add_edge(7,8)
G.add_edge(9,8)
tree = nx.bfs_tree(G, 2)
nx.draw(tree, with_labels=True, arrows= False)
plt.savefig('/tmp/bfs_image.png')
A = nx.adjacency_matrix(G)




Directed tree


import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,5)
G.add_edge(4,6)
G.add_edge(1,6)
G.add_edge(2,6)
G.add_edge(7,8)
G.add_edge(9,8)
tree = nx.bfs_tree(G, 2)
nx.draw(tree, with_labels=True, arrows= True)
plt.savefig('/tmp/bfs_image.png')
A = nx.adjacency_matrix(G)


DAG


import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt
G = nx.DiGraph()

G.add_node("1")


G.add_node("2")
G.add_node("3")
G.add_node("4")
G.add_edge("1", "2")
G.add_edge("1", "3")
G.add_edge("2 ", "3" )
G.add_edge("3", "4" )
# write dot file to use with graphviz
# run "dot -Tpng test.dot >test.png"
nx.nx_agraph.write_dot(G,'test.dot')

# same layout using matplotlib with no labels
plt.title('DAG')
pos=graphviz_layout(G, prog='dot')
nx.draw(G, pos, with_labels=True, arrows=True)
plt.savefig('nx_test.png')
A = nx.adjacency_matrix(G)
