import numpy as np
import matplotlib.pyplot as plt
from pygsp import graphs, plotting

#Question 1 - Complete Graph:
n = 10

W_complete = np.ones((n,n))
np.fill_diagonal(W_complete, 0)  # No self-loops.
g_complete = graphs.Graph(W_complete)
print("Complete Graph")
print("Adjecency Matrix:")
print(W_complete)
print("Laplacian:")
L_complete = np.diag(np.sum(W_complete, axis = 0)) - W_complete
print(L_complete)
fig, ax = plt.subplots()
g_complete.set_coordinates("ring2D")
g_complete.plot(ax=ax)
_ = ax.set_title('Complete Graph (n = 10)')
