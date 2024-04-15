import networkx as nx

# Cria um grafo dirigido ponderado
graph = nx.DiGraph()

# Adiciona as arestas e pesos ao grafo a partir do dicionário fornecido
mapa_romenia = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Oradea', 71), ('Arad', 75)],
    'Oradea': [('Sibiu', 151), ('Zerind', 71)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101)]
}

for city, neighbors in mapa_romenia.items():
    for neighbor, distance in neighbors:
        graph.add_edge(city, neighbor, weight=distance)

# Função para encontrar o caminho mais curto de menor custo usando o algoritmo Dijkstra
def find_shortest_path(graph, start, end):
    # Usa a função nx.shortest_path para encontrar o caminho mais curto com base no peso
    path = nx.shortest_path(graph, source=start, target=end, weight='weight')
    return path

# Testa a função para encontrar o caminho mais curto de Arad para Bucharest
shortest_path = find_shortest_path(graph, 'Arad', 'Bucharest')
print(shortest_path)