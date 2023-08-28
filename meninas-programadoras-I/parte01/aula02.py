valor1 = int(input())
valor2 = int(input())
resposta = valor1 > valor2
print(resposta)
resposta = valor1 >= valor2
print(resposta)
resposta = valor1 < valor2
print(resposta)
resposta = valor1 <= valor2
print(resposta)
resposta = valor1 == valor2
print(resposta)

######

a = int(input())
b = int(input())
c = int(input())
d = int(input())
resposta = (a > b) and (c < d) 
print(resposta)
resposta = (a > b) or (c < d) 
print(resposta)
resposta = not (a > b) 
print(resposta)

####

texto1 = input()
texto2 = input()
print('-----')
print()
print(texto1)
print(texto2)
print(texto1, texto2)

###

decimal = float(input())
print('%.3f' % decimal)
print('%.2f' % decimal)
print('%.1f' % decimal)
print('%.0f' % decimal)

###
nome = input('Seu nome:')
sobrenome = input('Sobrenome:')
print('Bem-vinda', nome, sobrenome, '!')

####
nome = input('Seu nome:')
sobrenome = input('Sobrenome:')
saida = 'Bem-vinda ' + nome + ' ' + sobrenome +'!'
print(saida)