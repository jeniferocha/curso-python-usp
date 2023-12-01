# Função lambda que calcula o quadrado de um número
quadrado = lambda x: x ** 2

# Usando a função lambda para calcular o quadrado de 5
resultado = quadrado(15)

print(resultado)  # Saída: 225


# Lista de números de entrada
numeros = [1, 2, 3, 4, 5]


# Usando map() com uma função lambda para elevar ao quadrado cada número
quadrados = map(lambda x: x ** 2, numeros)

# Convertendo o resultado de map() em uma lista
quadrados = list(quadrados)

print(quadrados)  # Saída: [1, 4, 9, 16, 25]


tabela_de_dados = [
  {'id': 1, 'valor': 1},
  {'id': 2, 'valor': 17},
  {'id': 3, 'valor': 12},
  {'id': 4, 'valor': 20},
  {'id': 5, 'valor': 15},
]






# Filtrar resultados da nossa lista cujo valor é menor que 15
resultado = list(filter(lambda x: x['valor'] < 15, tabela_de_dados))
print(resultado) # [{'id': 1, 'valor': 1}, {'id': 3, 'valor': 12}]


# coletar indices das tarefas curtas
indices_tarefas_curtas = list(filter(lambda id_tarefa: dicionario[id_tarefa][1] <= 3, dicionario))

# coletar as tarefas dos indices
tarefas_curtas = list(map(lambda id: dicionario[id][0], indices_tarefas_curtas))

# imprimir apenas as tarefas curtas
imprimir_tarefa_curta = lambda tarefa: print('Fazer agora a tarefa:', tarefa)
[imprimir_tarefa_curta(tarefa) for tarefa in tarefas_curtas]

# coletar indices das tarefas longas
indices_tarefas_longas = list(filter(lambda id_tarefa: dicionario[id_tarefa][1] > 3, dicionario))

# coletar as tarefas dos indices
tarefas_longas = list(map(lambda id: dicionario[id][0], indices_tarefas_longas))
print(tarefas_longas)





# CURIOSIDADES

# Busca em largura: BFS
visitados = []
fila = []

def busca_em_largura(visitados, grafo, no):
  visitados.append(no)
  fila.append(no)

  while len(fila) != 0:
    print(fila)
    proximo = fila.pop(0)
    print(proximo, end = " ")


    for vizinho in grafo[proximo]:
      if vizinho not in visitados:
        visitados.append(vizinho)
        fila.append(vizinho)

grafo = {
   'a': ['b','c'],
   'b': ['d','e'],
   'c': ['f','g'],
   'd': [],
   'e': ['h'],
   'f': [],
   'g': [],
   'h': [],
}

print("Busca em largura (BFS)")
busca_em_largura(visitados, grafo, 'a')





# Busca em profundidade: DFS
visitados = []
def busca_em_profundidade(visitados, grafo, no):
    if no not in visitados:
      print(visitados)
      print(no, end = " ")
      visitados.append(no)
      for vizinho in grafo[no]:
          busca_em_profundidade(visitados, grafo, vizinho)


grafo = {
   'A':['B','C','E'],
   'B':['D','F','E'],
   'C':['G'],
   'D':[],
   'E':[],
   'F':['E'],
   'G':[],
}


print("Busca em profundidade (DFS)")
busca_em_profundidade(visitados, grafo, 'A')