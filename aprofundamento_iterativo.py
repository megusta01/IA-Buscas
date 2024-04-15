import networkx as nx

grafo = nx.Graph()

grafo.add_node("Arad")
grafo.add_node("Zerind")
grafo.add_node("Oradea")
grafo.add_node("Sibiu")
grafo.add_node("Timisoara")
grafo.add_node("Lugoj")
grafo.add_node("Mehadia")
grafo.add_node("Dobreta")
grafo.add_node("Craiova")
grafo.add_node("Rimnicu Vilcea")
grafo.add_node("Fagaras")
grafo.add_node("Pitesti")
grafo.add_node("Bucharest")
grafo.add_node("Giurgiu")
grafo.add_node("Urziceni")
grafo.add_node("Hirsova")
grafo.add_node("Eforie")
grafo.add_node("Vaslui")
grafo.add_node("Iasi")
grafo.add_node("Neamt")

arestas = [
    ("Arad", "Sibiu"),
    ("Arad", "Timisoara"),
    ("Arad", "Zerind"),
    ("Zerind", "Oradea"),
    ("Oradea", "Sibiu"),
    ("Sibiu", "Fagaras"),
    ("Sibiu", "Rimnicu Vilcea"),
    ("Timisoara", "Lugoj"),
    ("Lugoj", "Mehadia"),
    ("Mehadia", "Dobreta"),
    ("Dobreta", "Craiova"),
    ("Craiova", "Rimnicu Vilcea"),
    ("Craiova", "Pitesti"),
    ("Rimnicu Vilcea", "Pitesti"),
    ("Fagaras", "Bucharest"),
    ("Pitesti", "Bucharest"),
    ("Bucharest", "Giurgiu"),
    ("Bucharest", "Urziceni"),
    ("Urziceni", "Hirsova"),
    ("Hirsova", "Eforie"),
    ("Urziceni", "Vaslui"),
    ("Vaslui", "Iasi"),
    ("Iasi", "Neamt")
]

grafo.add_edges_from(arestas)

def busca_em_profundidade_limitada(inicio, objetivo, limite_profundidade):
    try:
        caminho = nx.bfs_edges(grafo, source=inicio, depth_limit=limite_profundidade)
        return objetivo in [v for u, v in caminho]
    except nx.NetworkXNoPath:
        return False

def busca_profundidade_iterativa(inicio, objetivo):
    limite_profundidade = 0 
    while True:
        print(f"Tentando com limite de profundidade: {limite_profundidade}")
        encontrado = busca_em_profundidade_limitada(inicio, objetivo, limite_profundidade)
        if encontrado:
            print(f"Objetivo encontrado com limite de profundidade {limite_profundidade}")
            return True
        else:
            print(f"Objetivo nao encontrado com limite de profundidade {limite_profundidade}")
            limite_profundidade += 1  # Aumenta o limite de profundidade

path = busca_profundidade_iterativa("Arad", "Bucharest")

if path:
    print("Caminho encontrado!")
else:
    print("Caminho não encontrado!")
