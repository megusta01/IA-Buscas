import networkx as nx

# Classe Cidade que representa um nó com as propriedades nome e distância
class Cidade:
    def __init__(self, nome, distancia_objetivo):
        self.nome = nome
        self.distancia_objetivo = distancia_objetivo

# Função para adicionar arestas entre as cidades
def adicionar_arestas(G, cidade1, cidade2):
    G.add_edge(cidade1.nome, cidade2.nome, distancia_objetivo=cidade2.distancia_objetivo)

# Criação do grafo
G = nx.Graph()

# Criação das cidades
arad = Cidade("Arad", 366)
zerind = Cidade("Zerind", 374)
oradea = Cidade("Oradea", 380)
sibiu = Cidade("Sibiu", 253)
timisoara = Cidade("Timisoara", 329)
lugoj = Cidade("Lugoj", 244)
mehadia = Cidade("Mehadia", 241)
dobreta = Cidade("Dobreta", 242)
craiova = Cidade("Craiova", 160)
rimnicu_vilcea = Cidade("Rimnicu Vilcea", 193)
fagaras = Cidade("Fagaras", 178)
pitesti = Cidade("Pitesti", 98)
bucharest = Cidade("Bucharest", 0)
giurgiu = Cidade("Giurgiu", 77)
urziceni = Cidade("Urziceni", 80)
hirsova = Cidade("Hirsova", 151)
eforie = Cidade("Eforie", 161)
vaslui = Cidade("Vaslui", 199)
iasi = Cidade("Iasi", 226)
neamt = Cidade("Neamt", 234)

# Adicionando cidades ao grafo
G.add_node(arad.nome, distancia_objetivo=arad.distancia_objetivo)
G.add_node(zerind.nome, distancia_objetivo=zerind.distancia_objetivo)
G.add_node(oradea.nome, distancia_objetivo=oradea.distancia_objetivo)
G.add_node(sibiu.nome, distancia_objetivo=sibiu.distancia_objetivo)
G.add_node(timisoara.nome, distancia_objetivo=timisoara.distancia_objetivo)
G.add_node(lugoj.nome, distancia_objetivo=lugoj.distancia_objetivo)
G.add_node(mehadia.nome, distancia_objetivo=mehadia.distancia_objetivo)
G.add_node(dobreta.nome, distancia_objetivo=dobreta.distancia_objetivo)
G.add_node(craiova.nome, distancia_objetivo=craiova.distancia_objetivo)
G.add_node(rimnicu_vilcea.nome, distancia_objetivo=rimnicu_vilcea.distancia_objetivo)
G.add_node(fagaras.nome, distancia_objetivo=fagaras.distancia_objetivo)
G.add_node(pitesti.nome, distancia_objetivo=pitesti.distancia_objetivo)
G.add_node(bucharest.nome, distancia_objetivo=bucharest.distancia_objetivo)
G.add_node(giurgiu.nome, distancia_objetivo=giurgiu.distancia_objetivo)
G.add_node(urziceni.nome, distancia_objetivo=urziceni.distancia_objetivo)
G.add_node(hirsova.nome, distancia_objetivo=hirsova.distancia_objetivo)
G.add_node(eforie.nome, distancia_objetivo=eforie.distancia_objetivo)
G.add_node(vaslui.nome, distancia_objetivo=vaslui.distancia_objetivo)
G.add_node(iasi.nome, distancia_objetivo=iasi.distancia_objetivo)
G.add_node(neamt.nome, distancia_objetivo=neamt.distancia_objetivo)

# Adicionando as arestas entre as cidades
adicionar_arestas(G, arad, sibiu)
adicionar_arestas(G, arad, timisoara)
adicionar_arestas(G, arad, zerind)

adicionar_arestas(G, zerind, oradea)
adicionar_arestas(G, oradea, sibiu)

adicionar_arestas(G, sibiu, fagaras)
adicionar_arestas(G, sibiu, rimnicu_vilcea)

adicionar_arestas(G, timisoara, lugoj)

adicionar_arestas(G, lugoj, mehadia)

adicionar_arestas(G, mehadia, dobreta)

adicionar_arestas(G, dobreta, craiova)

adicionar_arestas(G, craiova, pitesti)
adicionar_arestas(G, craiova, rimnicu_vilcea)

adicionar_arestas(G, rimnicu_vilcea, pitesti)

adicionar_arestas(G, fagaras, bucharest)

adicionar_arestas(G, pitesti, bucharest)

adicionar_arestas(G, bucharest, giurgiu)
adicionar_arestas(G, bucharest, urziceni)

adicionar_arestas(G, urziceni, hirsova)
adicionar_arestas(G, urziceni, vaslui)

adicionar_arestas(G, hirsova, eforie)

adicionar_arestas(G, vaslui, iasi)

adicionar_arestas(G, iasi, neamt)

# Função de busca gulosa
def busca_gulosa(inicio, objetivo):
    # Lista para manter o caminho encontrado
    caminho = [inicio.nome]
    # Variável para acompanhar a cidade atual
    atual = inicio
    
    # Continue buscando enquanto a cidade atual não for a cidade objetivo
    while atual.nome != objetivo.nome:
        # Inicializa com um valor alto para encontrar o vizinho com a menor distância ao objetivo
        menor_distancia = float('inf')
        proxima_cidade = None
        
        # Itera sobre os vizinhos da cidade atual
        for vizinho in G[atual.nome]:
            vizinho_cidade = Cidade(vizinho, G[atual.nome][vizinho]['distancia_objetivo'])
            # Verifica se a cidade vizinha possui menor distância ao objetivo
            if vizinho_cidade.distancia_objetivo < menor_distancia:
                menor_distancia = vizinho_cidade.distancia_objetivo
                proxima_cidade = vizinho_cidade
        
        # Se não houver próximo vizinho, não é possível encontrar um caminho
        if proxima_cidade is None:
            return None
        
        # Atualiza a cidade atual para a próxima cidade com a menor distância ao objetivo
        atual = proxima_cidade
        # Adiciona a próxima cidade ao caminho
        caminho.append(atual.nome)
    
    # Retorna o caminho encontrado
    return caminho

# Cidade de início e cidade objetivo
inicio = arad
objetivo = bucharest

# Execução da busca gulosa
resultado = busca_gulosa(inicio, objetivo)

# Verifica se o resultado foi encontrado e exibe o caminho
if resultado is not None:
    print("Caminho encontrado:", " -> ".join(resultado))
else:
    print("Caminho não encontrado!")
