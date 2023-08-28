vazia = []
vogais = ['a', 'o', 'i', 'u', 'e']
frutas = ['banana', 'laranja', 'abacaxi']
alunas = ['Paola', 'Nathane', 'Ana', 'Filipa']
notas = [10, 9.5, 10, 9.0]
print(vazia)
print(vogais)
print(frutas)
print(alunas)
print(notas)

###
lista = []
print(lista)
lista.append('Ana')
print(lista)
lista.append('Paola')
print(lista)
lista.append('Nathane')
print(lista)
lista.append('Ariele')
print(lista)
lista.insert(10,'Agnes')  # nao gostei
print(lista)
lista.insert(1, 'Laura')
print(lista)

####

lista = []
print(lista)
lista.append('Ana')
print(lista)
lista.append('Paola')
print(lista)
lista.append('Nathane')
print(lista)
lista.append('Ariele')
print(lista)
nome = lista.pop()  # ultimo
print(nome, '-', lista)
lista.insert(1, 'Laura')
print(lista)
nome = lista.pop(0)  # primeiro
print(nome, '-', lista)

####

total = int(input())
meninas = []
for valor in range(total):
  menina = input()
  meninas.append(menina)
print(meninas)

for menina in meninas:
  print(menina)

# i = int(input())
# print(meninas[i])

###

total = int(input())
meninas = []
for valor in range(total):
  menina = input()
  meninas.append(menina)
print(meninas)

for i in range(total):
  print(meninas[i])

###
total = int(input())
meninas = []
for valor in range(total):
  menina = input()
  meninas.append(menina)
print(meninas)

for i in range(len(meninas)):
  print(meninas[i])
print(meninas)

###

total = int(input())
meninas = []
for valor in range(total):
  menina = input()
  meninas.append(menina)
print(meninas)

for i in range(len(meninas)):
  print(meninas.pop())
print(meninas)

####
total = int(input())
meninas = []
for valor in range(total):
  menina = input()
  meninas.append(menina)
print(meninas)

for i in range(len(meninas)):
  print(meninas.pop(0))
print(meninas)

####
lista = ['Vera', 'Olga', 'Bia', 'Mariana', 'Gabriela']
print(lista)
lista.sort()
print(lista)


##

lista = ['Vera', 'Olga', 'Bia', 'Mariana', 'Gabriela']
print(lista)
ordenada = sorted(lista)
print(lista)
print(ordenada)

