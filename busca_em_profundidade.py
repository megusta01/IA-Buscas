import networkx as nx

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

graph = nx.Graph()
for node, neighbors in graph_dict.items():
    for neighbor in neighbors:
        graph.add_edge(node, neighbor)

def dfs_path(graph, start, end):
    try:
        dfs_tree = nx.dfs_tree(graph, source=start)
        path = nx.shortest_path(dfs_tree, source=start, target=end)
        return path
    except nx.NetworkXNoPath:
        return None

path = dfs_path(graph, 'Arad', 'Bucharest')
if path:
    print(path)
else:
    print('Caminho não encontrado.')