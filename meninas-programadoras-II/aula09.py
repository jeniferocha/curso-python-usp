# Função para buscar um valor em uma lista ordenada usando busca binária
def busca_binaria(lista, alvo):
  esquerda, direita = 0, len(lista) - 1
  while esquerda <= direita:
    meio = (esquerda + direita) // 2
    if lista[meio] == alvo: # acheiiiiii
        return True
    elif lista[meio] < alvo:
        esquerda = meio + 1
    else:
        direita = meio - 1
  return False

# leio sequência de valores inteiros em uma linha
valores = [int(valor) for valor in input().split()]

# uso sort() pronto do Python
valores.sort()
print(valores)

# busca chave
valor_procurado = int(input())
contador = 0

if busca_binaria(valores, valor_procurado):
  print('achei')
else:
  print('não achei')



# Função para buscar um valor em uma lista ordenada usando busca binária
def busca_binaria(lista, alvo):
  esquerda, direita = 0, len(lista) - 1
  while esquerda <= direita:
    meio = (esquerda + direita) // 2
    if lista[meio] == alvo:   # acheiiiiii
        return meio
    elif lista[meio] < alvo:
        esquerda = meio + 1
    else:
        direita = meio - 1
  return -1

# leio sequência de valores inteiros em uma linha
valores = [int(valor) for valor in input().split()]

# uso sort() pronto do Python
valores.sort()
print(valores)

# busca chave
valor_procurado = int(input())
contador = 0

posicao = busca_binaria(valores, valor_procurado)

if posicao != -1:
  print('achei na posição', posicao )
else:
  print('não achei')



def maior(lista):
  if len(lista) > 0:
    maior = lista[0]
    for elemento in lista:
      if elemento > maior:
        maior = elemento
    return maior
  else:
    return -1

inteiros = [int(item) for item in input().split()]
if len(inteiros) > 0:
  print(maior(inteiros))
else:
  print('lista vazia')




def selection_sort(lista):
    n = len(lista)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if lista[j] < lista[min_index]:
                min_index = j

        lista[i], lista[min_index] = lista[min_index], lista[i]

lista = [64, 25, 12, 22, 11]
selection_sort(lista)
print('Lista ordenada pelo Selection Sort:', lista)




def insertion_sort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key

lista = [64, 25, 12, 22, 11]
insertion_sort(lista)
print('Lista ordenada pelo Insertion Sort:', lista)



def merge_sort(lista):
  if len(lista) > 1:
    meio = len(lista) // 2
    metade_esquerda = lista[:meio]
    metade_direita = lista[meio:]

    merge_sort(metade_esquerda)
    merge_sort(metade_direita)

    i = j = k = 0

    while i < len(metade_esquerda) and j < len(metade_direita):
      if metade_esquerda[i] < metade_direita[j]:
        lista[k] = metade_esquerda[i]
        i += 1
      else:
        lista[k] = metade_direita[j]
        j += 1
      k += 1

    while i < len(metade_esquerda):
      lista[k] = metade_esquerda[i]
      i += 1
      k += 1

    while j < len(metade_direita):
      lista[k] = metade_direita[j]
      j += 1
      k += 1

lista = [38, 27, 43, 3, 9, 82, 10]
merge_sort(lista)
print('Lista ordenada pelo Merge Sort:', lista)


