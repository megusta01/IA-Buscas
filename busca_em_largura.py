import networkx as nx

grafo = nx.Graph()

neighbors = [
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

grafo.add_edges_from(neighbors)

def bfs(graph, start, end):
    path = nx.shortest_path(graph, source=start, target=end)
    return path

path = bfs(grafo, 'Arad', 'Bucharest')
if path:
    print(path)
else:
    print('Caminho não encontrado.')