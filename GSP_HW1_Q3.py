import numpy as np
import matplotlib.pyplot as plt
from pygsp import graphs, plotting

# Question 3 - Bipartite graph

n = 3
m = 5

#Undirected
W_bi_u = np.zeros((m+n,m+n))
for i in range(n):
    for j in range(m):
        W_bi_u[n+j][i] = 1
np.fill_diagonal(W_bi_u, 0)
W_bi_u = W_bi_u + W_bi_u.T
G_bi_u = graphs.Graph(W_bi_u)
print("\nUndirected")
print('{} nodes, {} edges'.format(G_bi_u.N, G_bi_u.Ne))
print("Adjecency Matrix:")
print(W_bi_u)
print("Laplacian:")
L_bi_u = np.diag(np.sum(W_bi_u, axis = 0)) - W_bi_u
print(L_bi_u)
fig, ax = plt.subplots()
G_bi_u.set_coordinates()
G_bi_u.plot(ax=ax)
_ = ax.set_title('Undirected Bipartite Graph')

#Directed
W_bi_d = np.zeros((m+n,m+n))
for i in range(n):
    for j in range(m):
        W_bi_d[n+j][i] = 1
np.fill_diagonal(W_bi_d, 0)
G_bi_d = graphs.Graph(W_bi_d)
print("\nDirected")
print('{} nodes, {} edges'.format(G_bi_d.N, G_bi_d.Ne))
print("Adjecency Matrix:")
print(W_bi_d)
fig, ax = plt.subplots()
G_bi_d.set_coordinates()
G_bi_d.plot(ax=ax)
_ = ax.set_title('Directed Bipartite Graph') 