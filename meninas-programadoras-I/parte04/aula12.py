lista = [19, 9, -55, 99, 8, 7, 5, -9]

minimo = min(lista)
maximo = max(lista)

print(minimo, maximo)

###
chave = int(input())
lista = [19, 9, -55, 99, 8, 7, 5, -9]

if chave in lista:
    print('tem aqui')
else:
    print('nao tem aqui')


###

chave = int(input())
lista = [19, 9, -55, 99, 8, 7, 5, -9]

for i in lista:
  if i == chave:
    print('achei')
  else:
    print('nao é este aqui', i)


###
chave = int(input())
lista = [19, 9, -55, 99, 8, 7, 5, -9]

for i in lista:
  if i == chave:
    print('achei')
    break
  else:
    print('nao é este aqui', i)

###
OK = 'tem aqui!'
ERRO = 'não tem aqui'

chave = int(input())
lista = [19, 9, -55, 99, 8, 7, 5, -9]

if chave in lista:
  resposta = OK
else:
  resposta = ERRO
print(resposta)

###
import random 
rand = int(random.uniform(0, 99999))
print(rand)

###
from math import sqrt  # "square root" sq abreviatura de square  / rt é abreviatura de root
numero = int(input())
raiz2 = sqrt(numero)   # sqrt() é função que retorna raiz quadrada do valor especificado
print(raiz2)

##

import random
lista = []
print(lista)
for i in range(12):
  numero = int(random.uniform(1,99999))
  lista.append(numero)
  print(lista)

  ###
import random
lista = []
for i in range(9999):
  numero = int(random.uniform(1,99999))
  lista.append(numero)
print(lista)


##

import random
OK = 'achei'
ERRO = 'nao tem'

# primeiro geramos uma lista para termos com o que trabalhar
lista = []
for i in range(9999):
  numero = int(random.uniform(1,99999))
  lista.append(numero)
print(lista)

chave = int(input())
resposta = ERRO
trabalhao = ''
for i in lista:
  if chave == i:
    resposta = OK
  else:
    trabalhao += '.'
print(resposta)
print(trabalhao)

###
# Ler primeiro e últimos elementos
# Imprimir todos os inteiros entre o primeiro e o último, inclusive o primeiro e o último
# e.g.
#  de 7    a   10
#     7  8  9  10
# neste, imprimimos todos os valores na mesma linha

inicio = int(input())
final = int(input())
contador = 0
while inicio <= final:
  print(inicio, end='-')
  contador += 1
  inicio += 1


##

import random
OK = 'achei'
ERRO = 'nao tem'

# gerar uma lista para ter com o que trabalhar
lista = []
for i in range(2000):
  numero = int(random.uniform(1,999))
  lista.append(numero)
print(lista)

# obter  chave a ser buscada 
chave = int(input())

resposta = ERRO   # inicializar resposta para o caso de não encontrar
contador = 0      # inicializar contador 
for i in lista:   # mandar Python passear na lista
  if chave == i:  # compararar item com chave
    resposta = OK # atualizar resposta toda vez que encontrar
    contador += 1 # atualizar contador

print(resposta)
print('ocorrências:', contador)

##

import random

# gerar uma lista para ter com o que trabalhar
lista = []
for i in range(20):
  numero = int(random.uniform(1,20))
  lista.append(numero)

chute = int(input())          # obter chute do usuário
contador = lista.count(chute) # mandar Python contar quantos tem

if contador > 0:              # verificar se tem algum ou não
  print('achou')
else:
  print('dançou')

print(lista)

###



import random

# gerar uma lista para ter com o que trabalhar
lista = []
for i in range(20):
  numero = int(random.uniform(1,20))
  lista.append(numero)

chute = int(input())          # obter chute do usuário
contador = lista.count(chute) # mandar Python contar quantos tem

while contador == 0:          # repetir até encontrar pelo menos 1
  print('tente de novo 8^)')
  chute = int(input())
  contador = lista.count(chute)
else:
  print('achou')

print(lista)


###

conta = int(input())
montinho = 0
while montinho < conta:
  valor = int(input())
  montinho += valor
print(montinho)

###
import random

# primeiro geramos uma lista para termos com o que trabalhar
lista = []
for i in range(20):
  numero = int(random.uniform(1,20))
  lista.append(numero)

while True:
  chute = int(input())
  contador = lista.count(chute)
  if contador != 0:
    print('achou')
    break
  else:
    print('tente de novo 8^)')

print(lista)

##

