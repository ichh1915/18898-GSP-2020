import numpy as np
import matplotlib.pyplot as plt
from pygsp import graphs, plotting

# Question 2 - Star Graph

n = 10

#Undirected
W_star_u = np.zeros((n,n))
W_star_u[0] = np.ones(n)
np.fill_diagonal(W_star_u, 0)
W_star_u = W_star_u + W_star_u.T
G_star_u = graphs.Graph(W_star_u)
print("Undirected")
print('{} nodes, {} edges'.format(G_star_u.N, G_star_u.Ne))
print("Adjecency Matrix:")
print(W_star_u)
print("Laplacian:")
L_star_u = np.diag(np.sum(W_star_u, axis = 0)) - W_star_u
print(L_star_u)
fig, ax = plt.subplots()
G_star_u.set_coordinates()
G_star_u.plot(ax=ax)
_ = ax.set_title('Undirected Star Graph')

#Directed
W_star_d = np.zeros((n,n))
W_star_d[0] = np.ones(n)
np.fill_diagonal(W_star_d, 0)
G_star_d = graphs.Graph(W_star_d)
print("\nDirected")
print('{} nodes, {} edges'.format(G_star_d.N, G_star_d.Ne))
print("Adjecency Matrix:")
print(W_star_d)
fig, ax = plt.subplots()
G_star_d.set_coordinates()
G_star_d.plot(ax=ax)
_ = ax.set_title('Directed Star Graph')