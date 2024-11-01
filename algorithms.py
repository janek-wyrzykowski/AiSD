# TODO usunąć importy - nie będą potrzebne, jeśli funkcje będą wywoływane w main
import networkx as nx
import copy

def graph_simplify(g: nx.Graph) -> nx.Graph:
    """
    Zwraca graf pełny składający się z wierzchołków z `g` mających parametr `toVisit=True` i krawędziami o wagach równych długości najkrótszej ścieżki między danymi wierzchołkami w grafie `g`.

    Argumenty:
        `g` (`networkx.Graph`): graf do uproszczenia.

    Zwraca:
        `k` (`networkx.Graph`): uproszczony graf pełny.
    """

    # Tworzenie grafu składającego się tylko z wierzchołków wymagających odwiedzenia
    k = nx.Graph()
    k.add_nodes_from([node for (node, node_data) in g.nodes(data=True) if node_data['toVisit']])

    # Dopisanie do grafu `k` krawędzi o optymalnych długościach 
    for node in k.nodes:
        optimal_path_lenghts = dijkstra_optimal_paths(g, node)
        k.add_edges_from([(node, key, {'weight': value}) for (key, value) in optimal_path_lenghts.items() if key in k.nodes])
        
    return k

def dijkstra_optimal_paths(g: nx.Graph, start: int) -> dict[int, int]:
    """
    Zwraca słownik długości optymalnych ścieżek w grafie `g` od wierzchołka `start` do każdego pozostałego wierzchołka.

    Argumenty:
        `g` (`networkx.Graph`): graf, w którym poszukiwane są ścieżki.
        `start` (`int`): wierzchołek startowy.

    Zwraca:
        `lengths` (`dict[int, int]`): słownik z kluczami będącymi numerami wierzchołków i wartościami będącymi długościami najkrótszych ścieżek między danymi wierzchołkami a wierzchołkiem `start`.
    """
    n = len(g.nodes)
    # Tworzenie grafu pełnego o krawędziach długości nieskończonej, a następnie nadpisanie niektórych krawędzi tymi z grafu g
    h = nx.complete_graph(range(1, n+1))
    h.add_edges_from(h.edges, weight=float('inf'))
    h.add_edges_from(g.edges(data=True))

    # Algorytm Dijkstry
    lengths = {node: h[start][node]['weight'] for node in set(h.nodes) - {start}}
    visited = [start]

    while len(visited) != n:
        mindist = float('inf')
        for node in set(h.nodes) - set(visited):
            if lengths[node] < mindist:
                minnode = node
                mindist = lengths[node]
        visited.append(minnode)
        for node in set(h.nodes) - set(visited):
            if lengths[node] > mindist + h[minnode][node]['weight']:
                lengths[node] = mindist + h[minnode][node]['weight']
    return lengths



# TODO usunąć testy poniżej

g = nx.Graph()
g.add_nodes_from([(1, {'toVisit': True}), (2, {'toVisit': False}), (3, {'toVisit': True}), (4, {'toVisit': True})])
g.add_edges_from([(1, 2, {'weight': 1}), (1, 3, {'weight': 2}), (2, 4, {'weight': 2}), (3, 4, {'weight': 1})])
graph_simplify(g)