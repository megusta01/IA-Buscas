import networkx as nx

# Cria o grafo a partir do dicionário fornecido
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
    'Vaslui': ['Urziceni', 'Lasi'],
    'Lasi': ['Vaslui', 'Neamt'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi'],
    'Fetesti': ['Giurgiu', 'Hirsova'],
}

# Cria um grafo vazio
graph = nx.Graph()

# Adiciona as arestas ao grafo a partir do dicionário
for node, neighbors in graph_dict.items():
    for neighbor in neighbors:
        graph.add_edge(node, neighbor)

# Função de busca em profundidade para encontrar um caminho entre dois nós
def dfs_path(graph, start, end):
    try:
        # Usa nx.dfs_tree para realizar a busca em profundidade
        dfs_tree = nx.dfs_tree(graph, source=start)
        # Extrai o caminho usando nx.shortest_path na árvore de busca em profundidade
        path = nx.shortest_path(dfs_tree, source=start, target=end)
        return path
    except nx.NetworkXNoPath:
        return None

# Testa a função de busca em profundidade
path = dfs_path(graph, 'Arad', 'Bucharest')
print(path)