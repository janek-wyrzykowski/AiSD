import networkx as nx
import matplotlib.pyplot as plt
import algorithms as alg
import graph_generation as gen
import numpy as np

def main():
    G = gen.graph_generation()

    pos = nx.circular_layout(G)
    n = len(G.nodes)

    plt.figure(figsize=(12,12))
    plt.gca().set_aspect('equal')
    plt.gca().axis('off')

    nx.draw_networkx_nodes(G, pos, node_color=['#C1121F' if G.nodes[n]['toVisit'] else '#669BBC' for n in G.nodes], node_size=1500-13*n)
    G_edge_weights = nx.get_edge_attributes(G, 'weight').values()
    nx.draw_networkx_edges(G, pos, edge_color='#003049', alpha=[1 - i/150 for i in G_edge_weights], width=[max(0.2, 2-np.log10(i)) for i in G_edge_weights])
    nx.draw_networkx_labels(G, pos)

    # plt.show()
    plt.savefig('img/test_3_1.png')

    
    H = alg.graph_simplify(G)

    path_opt = alg.solve_traveling_salesman(H)
    print(f'Optymalna kolejność odwiedzanych klientów: {path_opt}')

    plt.figure(figsize=(12,12))
    plt.gca().set_aspect('equal')
    plt.gca().axis('off')

    nx.draw_networkx_nodes(H, pos, node_color='#C1121F', node_size=1500-13*n)
    H_edge_weights = nx.get_edge_attributes(H, 'weight').values()
    nx.draw_networkx_edges(H, pos, edge_color='#003049', alpha=[max(0.33, 1 - i/150) for i in H_edge_weights], width=[max(0.2, 2-np.log10(i)) for i in H_edge_weights])
    nx.draw_networkx_edges(H, pos, edgelist=[(path_opt[i], path_opt[i+1]) for i in range(len(path_opt)-1)], edge_color='#780000', width=2)
    nx.draw_networkx_labels(H, pos)

    # plt.show()
    plt.savefig('img/test_3_2.png')

    input('Naciśnij ENTER, aby zamknąć.')

if __name__ == "__main__":
    main()
