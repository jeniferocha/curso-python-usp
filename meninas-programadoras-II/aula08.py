# linha = input()
# print([linha])
# separada = linha.split()
# print(separada)


linha = input()
separador = input()
print([linha])
separada = linha.split(separador)
print(separada)

# usando o mesmo exemplo de cima para função

def separar_elementos_de_string(linha, separador):    
    print([linha])
    separada = linha.split(separador)
    print(separada)
#define os parametros da função
linha = input()
separador = input()
#chama a função
separar_elementos_de_string(linha, separador)


#Gerar listas com numeros inteiros
linha = input().split() #quebrar e por em lista de strings
print(linha)
lista = []
for item in linha:
    inteiro = int(item) #transformar pra inteiro
    lista.append(inteiro) # add na lista vazia o numero inteiro
print(lista)


# Reduzindo um pouco o código
linha = input().split()
lista = []
for item in linha:
  lista.append(int(item))
print(lista)

# 2. Criando uma lista já com os elementos convertidos em
#    inteiros
linha = input().split()
lista = [int(item) for item in linha]
print(lista)

# Reduzindo pra 1 linha *** <3
linha = [int(item) for item in input().split()]
print(linha)

# Utilizando função list e tuple para criação de
#   listas/tuplas
linha = input().split()
lista = list(int(item) for item in linha)
print(lista)

# LEMBRETE:
# -- 1. Importancia de tuplas
# -- 2. Uso de *args
# -- 3. Uso de **kwargs

# *args: arguments (posicionais - ordem importa)
# **kwargs: key-word arguments (chave-valor - ordem não importa)


def controi_lista(*args, **kwargs):
  print(args) # Tupla: não podemos mudar os valores dos parametros
  print(kwargs) # Dicionario
controi_lista('B', 'A', 'C', 'D', Rua='Deodoro', Casa='Apto 10')


# Aproveitando *args para caso fatorial
# 5! = 5.4.3.2.1 = 120
def fatorial_um_a_um(*numeros):
  fatorial = 1
  for numero in numeros:
    fatorial *= numero
  return fatorial

resultado = fatorial_um_a_um(1,2,3,4,5,6,7,8,9,10,11,12,13)
print(resultado)


# Busca sequencial
lista = [int(item) for item in input().split()]
buscar = int(input())
encontrou = 'Não'
for item in lista:
  if item == buscar:
    encontrou = 'Sim'

print(encontrou)

# Dúvida: funcionamento do método .join()
def habilidades_aluna(nome, habilidades=['programação', 'matemática', 'python']):
    print(f'{nome} tem habilidades em {", ".join(habilidades)}.')

habilidades_aluna('Ana')