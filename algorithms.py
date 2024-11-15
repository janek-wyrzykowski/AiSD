import networkx as nx
import itertools

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

def solve_traveling_salesman(g: nx.Graph) -> list[int]:
    """
    Dla grafu pełnego `g` zwraca listę wierzchołków, które w kolejności tworzą najkrótszy cykl rozpinający - rozwiązanie problemu komiwojażera.

    Argumenty:
        `g` (`networkx.Graph`): graf ważony pełny, dla którego szukane jest rozwiązanie problemu komiwojażera.

    Zwraca:
        `nodes_order` (`list[int]`): lista wierzchołków ułożonych w optymalnej kolejności.
    """
    n = len(g.nodes)

    # Algorytm: Held-Karp

    # Podzbiory zbioru wierzchołków zapsujemy ciągami binarnymi - odpowiadają im koszty ścieżek oraz numer ostatnio odwiedzonego wierzchołka
    costs = {}
    # Wpisujemy początkowe odległości dla zbiorów 1-elementowych
    for k in set(g.nodes) - {1}:
        costs[(1 << k, k)] = (g[1][k]['weight'], 1)

    # Badamy kolejne podzbiory wierzchołków (w kolejności rosnącej rozmiarów podzbiorów) i zapisujemy wyniki pośrednie
    for set_size in range(2, n):
        for subset in itertools.combinations(set(g.nodes) - {1}, set_size):

            # Zapisujemy podzbiór w notacji bitowej
            subset_bits = 0
            for bit in subset:
                subset_bits |= 1 << bit

            # Znajdujemy najkrótsze ścieżki przez ten podzbiór kończące się na każdym z wierzchołków k tego podzbioru
            for k in subset:
                subset_prev = subset_bits & ~(1 << k)

                # Zapisujemy wszystkie ścieżki od 1 do k i wybieramy najkrótszą
                paths = []
                for m in subset:
                    # Nie nteresują nas ścieżki, w których poprzednim wierzchołkiem jest 1 lub k 
                    if m == 1 or m == k:
                        continue
                    paths.append((costs[(subset_prev, m)][0] + g[m][k]['weight'], m))
                costs[(subset_bits, k)] = min(paths)
    
    # Mając obliczone optymalne ścieżki przechodzące przez n wierzchołków, łączymy ich końce i wybieramy najlepszą
    # Podzbiorem jest teraz zbiór wszystkich wierzchołków oprócz pierwszego 
    subset_bits = sum([2**i for i in set(g.nodes) - {1}])
    paths = []
    for k in set(g.nodes) - {1}:
        paths.append((costs[(subset_bits, k)][0] + g[k][1]['weight'], k))
    
    (optimal_len, parent) = min(paths)

    # Pozostaje odtworzyć znaleziony cykl
    min_path = [1]
    for i in range(n - 1):
        min_path.append(parent)
        new_bits = subset_bits & ~(1 << parent)
        (_, parent) = costs[(subset_bits, parent)]
        subset_bits = new_bits
    min_path.append(1)

    return min_path
