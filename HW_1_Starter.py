
import numpy as np
import matplotlib.pyplot as plt
from pygsp import graphs, plotting


rs = np.random.RandomState(42)  # Reproducible results.
W = rs.uniform(size=(30, 30))  # Full graph.
W[W < 0.93] = 0  # Sparse graph.
W = W + W.T  # Symmetric graph.
np.fill_diagonal(W, 0)  # No self-loops.
G = graphs.Graph(W)
print('{} nodes, {} edges'.format(G.N, G.Ne))
G.set_coordinates('ring2D')
G.plot()


