import networkx as nx

# Cria um grafo não dirigido a partir do dicionário fornecido
graph_dict = {
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Rimnicu Vilcea': ['Sibiu', 'Pitesti'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Craiova': ['Pitesti', 'Drobeta'],
    'Drobeta': ['Craiova', 'Mehadia'],
    'Mehadia': ['Drobeta', 'Lugoj'],
    'Lugoj': ['Mehadia', 'Timisoara'],
    'Timisoara': ['Lugoj', 'Arad'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest', 'Fetesti'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Vaslui': ['Urziceni', 'Lasi', 'Iasi'],
    'Lasi': ['Vaslui', 'Neamt'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi'],
    'Fetesti': ['Giurgiu', 'Hirsova'],
}

# Cria um grafo não dirigido
graph = nx.Graph()

# Adiciona as arestas ao grafo a partir do dicionário fornecido
for node, neighbors in graph_dict.items():
    for neighbor in neighbors:
        graph.add_edge(node, neighbor)

# Função para realizar a busca limitada em profundidade usando networkx
def dls(graph, start, goal, limit=3):
    # Utiliza a função `nx.dfs_edges` para realizar a busca limitada em profundidade
    def dfs_limited(current, goal, depth):
        if depth > limit:
            return None
        if current == goal:
            return [goal]
        for neighbor in graph.neighbors(current):
            path = dfs_limited(neighbor, goal, depth + 1)
            if path:
                return [current] + path
        return None
    
    # Chama a função auxiliar para iniciar a busca
    return dfs_limited(start, goal, 0)

# Testa a função de busca limitada em profundidade
path = dls(graph, 'Arad', 'Bucharest')
print(path)
