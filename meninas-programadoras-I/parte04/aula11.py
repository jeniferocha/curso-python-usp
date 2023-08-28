nome = 'Maria'
print(nome, end='!')
print('Pimentel')

###
nome = 'Maria'
print(nome)
print('Pimentel')

###
idade = int(input())
if idade >= 18:
  print('maior idade')
else:
  print('ainda não chegou à maioridade')

  ####
  letra = input()
vogais = 'aeiou'
if letra in vogais:
  print('vogal')
else:
  print('não vogal')

  ###
  letra = input()
alvo = ['a', 'e', 'i', 'o', 'u', '0', '1', '2', '@', 'maria']
if letra in alvo:
  print('no alvo')
else:
  print('não há no alvo')

  ###
  palavra = input()
for letra in palavra:
  print(letra * 5)

  ###

  alvo = 'ana_maria'
for item in alvo:
  print(item)

  ##
  alvo = ['a', 'e', 'i', 'o', 'u', '0', '1', '2', '@', 'maria']
for letra in alvo:
  print(letra)

  ###
  palavra = input()
saida = ''
for letra in palavra:
  saida = saida + letra + '_'
print(saida)

##

inicio = 1
fim = 10
# 1 2 3 4 5 6 7 8 9 10
#enquanto item < fim:
#   imprime(item)
#   item = item + 1

item = inicio
while item <= fim:
  print(item)
  item = item + 1
print('fim')

##
turma = []
feminino = 'sim'
while feminino == 'sim':
  nome = input()
  genero = input()
  if genero == 'F':
    turma.append(nome)
  else:
    feminino = 'não'
print(turma)

###
valor_troco = int(input())
valor_acumulado = int(input())

while valor_acumulado < valor_troco:
  moeda = int(input())
  valor_acumulado = valor_acumulado + moeda

print(valor_acumulado)

###
valor_troco = int(input())
valor_acumulado = int(input())
total_moedas = 1

while valor_acumulado < valor_troco:
  moeda = int(input())
  total_moedas += 1
  valor_acumulado = valor_acumulado + moeda

print(valor_acumulado)
print(total_moedas)

###
bateria = int(input())
while bateria > 0:
  print('aspire...')
  bateria = bateria - 5
  print(bateria)
print('recarregar')

##
bateria = int(input())
while bateria > 0:
  print('aspire...')
  bateria = bateria - 5
  sensores = int(input('sensores:'))
  if sensores == 1:
    print('desvie')
    bateria = bateria - 10
  else:
    print('continue')
  print(bateria)
print('recarregar')