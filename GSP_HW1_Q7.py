
import matplotlib
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import collections
from networkx import nx

def save_graph(graph,n,p):
    #initialze Figure
    plt.figure(num=None, figsize=(20, 20), dpi=80)
    plt.axis('off')
    fig= plt.figure(figsize=(20,15))

    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph,pos)
    nx.draw_networkx_edges(graph,pos)
    nx.draw_networkx_labels(graph,pos)

    file_name = 'Q7_Assets/ErdosRenyi_N_'+str(n)+'_P_'+str(p)+'.pdf'
    plt.savefig(file_name,bbox_inches="tight")
    plt.close(fig)
    del fig

def draw_degree_hist(G,n,p):
    # Degree distribution
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
    # print "Degree sequence", degree_sequence
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())
    fig, ax = plt.subplots()
    plt.bar(deg, cnt, width=0.80, color='b')
    plt.title("Degree Histogram")
    plt.ylabel("Count")
    plt.xlabel("Degree")
    
    file_name = 'Q7_Assets/Degree_ErdosRenyi_N_'+str(n)+'_P_'+str(p)+'.pdf'
    plt.savefig(file_name,bbox_inches="tight")
    plt.close(fig)
    del fig
    
def graph_properties(G,G_main,n,p):
    # graph properties
    A = nx.adjacency_matrix(G).toarray()
    L = nx.laplacian_matrix(G).toarray()
    betwn_ctrlity = nx.betweenness_centrality(G)
    names = ['id','data']
    formats = ['i','f8']
    dtype = dict(names = names, formats=formats)
    betwn_ctrlity_array = np.array(list(betwn_ctrlity.items()), dtype=dtype)

    c = nx.average_clustering(G)
    d = nx.diameter(G_main)
        
    np.savetxt('Q7_Assets/Adjacency_N_'+str(n)+'_P_'+str(p)+'.csv', A, delimiter=",")
    np.savetxt('Q7_Assets/Laplacian_N_'+str(n)+'_P_'+str(p)+'.csv', L, delimiter=",")
    np.savetxt('Q7_Assets/Betweeness_N_'+str(n)+'_P_'+str(p)+'.csv', betwn_ctrlity_array, delimiter=",")
    print('Clustering = ',c, '\n')
    print('Diameter = ',d, '\n')



def ErdosRenyi(n,p):
    # generate Erdos Renyi graph given (n,p)
    G = nx.erdos_renyi_graph(n=n, p=p, seed=5)
    
    # Find the giant component
    Gcc = sorted(nx.connected_components(G), key=len, reverse=True)
    G_main = G.subgraph(Gcc[0])
    
    # compute graph properties
    graph_properties(G,G_main,n,p)

    # draw degree distribution
    draw_degree_hist(G,n,p)
    
    # draw the giant component
    save_graph(G_main,n,p)



##############################################################################################################################################################
if __name__ == '__main__':
    
        
    ### Question 7 ###
    # Gen undirected Erdos-Renyi graphs with n nodes and link formation probability p
    for n in [200, 1000]:
        for p in [.5/n, 5/n]:
                print('\nErdos_Renyi_graph with: n=',n, ', p=',p,'\n')
                ErdosRenyi(n,p)










