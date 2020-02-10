#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 16:39:46 2020

@author: hh1915
"""

import networkx as nx
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import community
import numpy as np
import collections

def save_graph(graph,values):
    #initialze Figure
    plt.figure(num=None, figsize=(20, 20), dpi=80)
    plt.axis('off')
    fig= plt.figure(figsize=(10,8))

    nx.draw_networkx(G, node_color=values, node_size=35, with_labels=False)

    file_name = 'Q9_Assets/facebook_subgraph.pdf'
    plt.savefig(file_name,bbox_inches="tight")
    plt.close(fig)
    del fig

def draw_degree_hist(G):
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
    file_name = 'Q9_Assets/Degree_facebook'
    plt.savefig(file_name,bbox_inches="tight")
    plt.close(fig)
    del fig
    
def graph_properties(G):
    # graph properties
    A = nx.adjacency_matrix(G).toarray() 
    L = nx.laplacian_matrix(G).toarray()
    betwn_ctrlity = nx.betweenness_centrality(G)
    names = ['id','data']
    formats = ['i','f8']
    dtype = dict(names = names, formats=formats)
    betwn_ctrlity_array = np.array(list(betwn_ctrlity.items()), dtype=dtype)
    c = nx.average_clustering(G)
    d = nx.diameter(G)
    p = nx.average_shortest_path_length(G)
        
    np.savetxt('Q9_Assets/Adjacency_N.csv', A, delimiter=",")
    np.savetxt('Q9_Assets/Betweeness_N.csv', betwn_ctrlity_array, delimiter=",")
    np.savetxt('Q9_Assets/Laplacian_N.csv', L, delimiter=",")
    print(nx.info(G), '\n')
    print('Clustering = ',c, '\n')
    print('Diameter = ',d, '\n')
    print('Avg_pathlength = ',p, '\n')





if __name__ == '__main__':

    
    G = nx.read_edgelist('facebook_combined.txt', create_using=nx.Graph(), nodetype=int)
    print(nx.info(G))
    

    
    # graph with community detection
    spring_pos = nx.spring_layout(G)
    parts = community.best_partition(G)
    values_G = [parts.get(node) for node in G.nodes()]
    values_arr = np.asarray(values_G)
    
    # subgraph of two of the communities
    comm_0 = np.where(values_arr == 0)
    comm_0_size = np.size(comm_0)
    comm_1 = np.where(values_arr == 2)
    comm_1_size = np.size(comm_1)

    comm_0 = comm_0[0].tolist()
    comm_1 = comm_1[0].tolist()
    H = G.subgraph(comm_0+comm_1)
    values_H = np.zeros((1,comm_0_size+comm_1_size))
    values_H[0,comm_0_size:comm_0_size+comm_1_size-1] = 1
    values_H = values_H.tolist()[0]
    print(nx.info(H), '\n')

    # plot
    plt.axis('off')
    fig= plt.figure(figsize=(20,20))

    nx.draw_networkx(H, node_color=values_H, node_size=5, with_labels=False)

    file_name = 'Q9_Assets/facebook_subgraph.pdf'
    plt.savefig(file_name,bbox_inches="tight")
    plt.close(fig)
    del fig
    
    # statistics
    Hcc = sorted(nx.connected_components(H), key=len, reverse=True)
    H_main = G.subgraph(Hcc[0])
    graph_properties(H_main)

    # Draw graph with community
    #save_graph(G,values)

