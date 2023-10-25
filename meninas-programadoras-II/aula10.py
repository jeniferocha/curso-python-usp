# Ideia geral de função:

# entrada -- -- saída
#           ^
#      função(entrada)


# 1. como receber nossas entradas
# ---- 10.2 --> float(input())
# ---- 102  --> int(input())
# ---- texto -> input()
# ---- sequencia
#      de inteiros  -> [int(i) for i in input().split()]


# Pin perigoso
ano1 = int(input())
ano2 = int(input())
resposta = ano1 + ano2
print(resposta)

# 2. transformando o código em função
# --- sem argumentos e sem retorno
def pin_perigoso():
  ano1 = int(input())
  ano2 = int(input())
  resposta = ano1 + ano2
  print(resposta)
pin_perigoso()



# --- com argumentos (params) mas ainda sem retorno
def pin_perigoso(ano1, ano2):
  resposta = ano1 + ano2
  print(resposta)
ano1 = int(input())
ano2 = int(input())
pin_perigoso(ano1, ano2)


# --- com argumentos e com retorno
def pin_perigoso(ano1, ano2):
  resposta = ano1 + ano2
  return resposta
ano1 = int(input())
ano2 = int(input())
pin = pin_perigoso(ano1, ano2)
print(pin)


# --- com operador *
ano1 = int(input())
ano2 = int(input())

def pin_perigoso(*anos):
  resposta = sum(anos)
  return resposta

resultado = pin_perigoso(ano1, ano2)
print(resultado)



#   entrada ---> funcao1(entrada) ---> saida1 --> funcao2(saida1) ---> saida
#     |
#     v
#     lista
#     numerica ----> funcao(lista) -----> saida   (esse é o caso do código abaixo)

def seu_maior(lista):
  maximo = lista[0]          # começo da escalada: valor inicial da lista [0]
  for elemento in lista:     # para cada elemento da nossa lista
    if elemento > maximo:    # se encontramos um novo valor de maximo
      maximo = elemento      # atualizar o valor de maximo

  # Alternativa (usando função já pronta!! -- cuidado caso peça que evite)
  # maximo = max(lista)
  return maximo

lista = []                    # lista iniciada vazia
linha = input()               # recebe linha toda como uma string
linha = linha.split()         # transforma a string em uma lista de strings
for elemento in linha:        # para cada elemento (string) da nossa linha
  numero = int(elemento)      # converte o elemento de string para inteiro
  lista.append(numero)        # atualiza a lista com o número que queremos

# Alternativa com compreensão de listas
# lista = [int(elemento) for elemento in input().split()]

# A partir daqui, em lista temos uma lista de números
resultado = seu_maior(lista)
print(resultado)




# Passando agora para esse fluxo:
#   entrada ---> funcao1(entrada) ---> saida1 --> funcao2(saida1) ---> saida2
def string_para_lista_numerica(entrada):
  lista_de_strings = entrada.split()
  lista_numerica = []
  for item in lista_de_strings:
    numero = int(item)
    lista_numerica.append(numero)
  return lista_numerica

def seu_maior(lista_numerica):
  maximo = lista_numerica[0]
  for item in lista_numerica:
    if item > maximo:
      maximo = item
  return maximo

entrada = input()
saida1 = string_para_lista_numerica(entrada)
saida2 = seu_maior(saida1)
print(saida2)


# Adicional: caso entrada como while

# se deu runtime, analisar:
# ---- variavel foi definida?
# ---- no loop, a variável está sendo atualizada?

def acumula_memoria(valor):
  acumulado = 0
  memorias_acumuladas = []
  while valor != 0:
    acumulado += valor
    memorias_acumuladas.append(acumulado)
    valor = int(input())
  return memorias_acumuladas

valor = int(input())
memorias_acumuladas = acumula_memoria(valor)
maximo = max(memorias_acumuladas)
print(maximo)


####################POS AULA
# Utilização com notação matemática
"""
y = 3x  equivalente f(x) = 3x
"""
def f(x):
  return 3*x

y = f(3)
print(y)

# Função recursiva
# Lembrete com fatorial

# Fatorial
# 4! = 4.3.2.1 = 24

# Como ficaria em notação matemática
# representação recursiva: fatorial(x) = x.fatorial(x-1)

"""
fatorial(4) = 4.fatorial(3)
            = 4.3.fatorial(2)
            = 4.3.2.fatorial(1)
            = 4.3.2.1
"""
def fatorial(n):
  if n == 1:
    return 1
  return n*fatorial(n-1)

y = fatorial(4)
print(y)




# Busca binária - iterativa
"""
motivação
-- tendo uma lista MUITO GRANDE e ordenada
-- precisamos de uma estratégia pra descobrir onde está
--  (e se existe) um certo valor que queremos

valores = [1, 2, 3, 5, 7, 9, 10]   buscar 3
           ^        x         ^
           ^  x  ^
                 ^                 encontrou 3
"""
def busca_binaria(valores, chave):
  inferior = 0
  superior = len(valores) - 1
  while inferior <= superior:
    meio = (superior + inferior) // 2
    if valores[meio] == chave:
      return f'{chave} na posição {meio}'
    elif valores[meio] > chave:
      superior = meio - 1
    elif valores[meio] < chave:
      inferior = meio + 1
  return 'Não encontrado'

lista = [1, 2, 3, 5, 7, 9, 10]
busca = -1
resultado = busca_binaria(lista, busca)
print(resultado)



# Utilização de parametros em funções

# Sem o parametro lista_a_ordenar
#  precisamos definir a lista de valores [1, 2, 3, 7, 5, 9, 10]
#  como variavel globale
def ordenar_lista(lista_a_ordenar):

  # Permitindo a ordenação de uma string
  if type(lista_a_ordenar) == str:
    return sorted(lista_a_ordenar)
  else:
    lista_a_ordenar.sort()
    return lista_a_ordenar


def busca_binaria(lista, chave):
  # ordenar a lista para garantir que
  #  a busca binaria funcione
  valores = ordenar_lista(lista)
  inferior = 0
  superior = len(valores) - 1
  while inferior <= superior:
    meio = (superior + inferior) // 2
    if valores[meio] == chave:
      return f'{chave} na posição {meio}'
    elif valores[meio] > chave:
      superior = meio - 1
    elif valores[meio] < chave:
      inferior = meio + 1
  return 'Não encontrado'

valores = 'aooakfoAAaosfuiSDASDF'
chave = 'f'
resultado = busca_binaria(valores, chave)
print(resultado)