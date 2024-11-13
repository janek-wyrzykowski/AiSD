import networkx as nx
import random
import numpy
import matplotlib.pyplot as plt
# import algorithms as alg
import graph_generation as gen

def main():
    G = gen.graph_generation()

    print(G)
    nx.draw(G)

    plt.show()
    print(G.nodes(data=True))


if __name__ == "__main__":
    main()