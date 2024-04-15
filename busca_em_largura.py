import networkx as nx

# Define the graph using NetworkX
grafo = nx.Graph()

# Add edges representing the Romania map
edges = [
    ('Arad', 'Zerind'),
    ('Arad', 'Sibiu'),
    ('Arad', 'Timisoara'),
    ('Zerind', 'Oradea'),
    ('Oradea', 'Sibiu'),
    ('Sibiu', 'Fagaras'),
    ('Sibiu', 'Rimnicu Vilcea'),
    ('Fagaras', 'Bucharest'),
    ('Rimnicu Vilcea', 'Pitesti'),
    ('Pitesti', 'Craiova'),
    ('Pitesti', 'Bucharest'),
    ('Craiova', 'Drobeta'),
    ('Drobeta', 'Mehadia'),
    ('Mehadia', 'Lugoj'),
    ('Lugoj', 'Timisoara'),
    ('Bucharest', 'Giurgiu'),
    ('Bucharest', 'Urziceni'),
    ('Giurgiu', 'Fetesti'),
    ('Urziceni', 'Hirsova'),
    ('Urziceni', 'Vaslui'),
    ('Hirsova', 'Eforie'),
    ('Vaslui', 'Iasi'),
    ('Vaslui', 'Neamt'),
    ('Iasi', 'Neamt')
]

# Add edges to the graph
grafo.add_edges_from(edges)

# Define the BFS function using NetworkX
def bfs(graph, start, end):
    # Use NetworkX's shortest_path function to perform BFS
    path = nx.shortest_path(graph, source=start, target=end)
    return path

# Find the shortest path from Arad to Bucharest using BFS
caminho = bfs(grafo, 'Arad', 'Bucharest')
print(caminho)