lista = [int(i) for i in input().split()]
for i in lista:
  linha = ''
  for j in range(i):
    linha += '*'
  print(linha)

  ###

  linha = input()
palavra = input()

nro_palavras_na_linha = linha.count(palavra)
print('[', palavra, '] ocorre', nro_palavras_na_linha, 'vez em: [', linha, ']')

###

linha = input()
palavra = input()

primeira_vez_palavra_na_linha = linha.find(palavra)

if primeira_vez_palavra_na_linha == -1:
  print('[', palavra, '] não ocorre em: [', linha, ']')
else:
  print('[', palavra, '] ocorre pela primeira vez em: [', linha, '] na posição:', primeira_vez_palavra_na_linha)

  ###

  linha = input()
palavra = input()

tamanho_palavra = len(palavra) 
trocar = ''
for i in range(tamanho_palavra):
  trocar += '*'
linha_palavra_escondida = linha.replace(palavra, trocar)
print(linha_palavra_escondida)

###


linha = input()
palavra = input()

tamanho_palavra = len(palavra) 
trocar = ''
for i in range(tamanho_palavra):
  trocar += '*'
linha_palavra_escondida = linha.replace(palavra, trocar, 1)
print(linha_palavra_escondida)

###
