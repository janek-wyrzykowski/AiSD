import networkx as nx
import matplotlib.pyplot as plt
import algorithms as alg
import graph_generation as gen

def main():
    G = gen.graph_generation()
    nx.draw(G)
    plt.show()
    
    H = alg.graph_simplify(G)
    nx.draw(H)
    plt.show()

    # print(H.number_of_nodes())
    # print(G.edges(data=True))
    # print(H.edges(data=True))

    path_opt = alg.solve_traveling_salesman(H)
    print(f'Optymalna kolejność odwiedzanych klientów: {path_opt}')
    input('Naciśnij ENTER, aby zamknąć.')

if __name__ == "__main__":
    main()
