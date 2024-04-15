import networkx as nx

# Criação do grafo
grafo = nx.Graph()

# Adicionando cidades ao grafo
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

# Adicionando arestas ao grafo (cidades vizinhas)
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

# Adicionando as arestas ao grafo
grafo.add_edges_from(arestas)

# Função de busca em profundidade limitada
def busca_em_profundidade_limitada(inicio, objetivo, limite_profundidade):
    try:
        # Busca utilizando NetworkX com limite de profundidade
        caminho = nx.bfs_edges(grafo, source=inicio, depth_limit=limite_profundidade)
        # Verifica se o objetivo está no caminho encontrado
        return objetivo in [v for u, v in caminho]
    except nx.NetworkXNoPath:
        return False

# Função de busca em profundidade iterativa
def busca_profundidade_iterativa(inicio, objetivo):
    limite_profundidade = 0  # Inicializa o limite de profundidade

    while True:
        print(f"Tentando com limite de profundidade: {limite_profundidade}")

        # Chama a função de busca em profundidade limitada
        encontrado = busca_em_profundidade_limitada(inicio, objetivo, limite_profundidade)

        # Verifica se o objetivo foi encontrado
        if encontrado:
            print(f"Objetivo encontrado com limite de profundidade {limite_profundidade}")
            return True
        else:
            print(f"Objetivo nao encontrado com limite de profundidade {limite_profundidade}")
            limite_profundidade += 1  # Aumenta o limite de profundidade

# Execução da busca em profundidade iterativa
resultado = busca_profundidade_iterativa("Arad", "Bucharest")

if resultado:
    print("Caminho encontrado!")
else:
    print("Caminho não encontrado!")
