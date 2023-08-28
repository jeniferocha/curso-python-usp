valor = int(input())
if valor > 0:
  print(valor, 'é positivo') # bloco interno ao if, indicado pelo deslocamento
print('fim.')                # comando seguinte ao bloco

###
nome = input()                # lê nome
idade = int(input())          # lê idade
resposta = 'não pode votar'   # prepara resposta para 'não pode votar'
if idade >= 16:               # testa condição para idade de votante
  resposta = 'pode votar'     # se condição for verdadeira, corrige a resposta
print(nome, resposta)         # executado depois do bloco if

###


nome = input()                # lê nome
idade = int(input())          # lê idade
if idade >= 16:               # testa condição para idade de votante
  resposta = 'pode votar'     # se condição for verdadeira, prepara resposta positiva
else:                         # identifica bloco executado se condição for negativa
  resposta = 'não pode votar' # prepara resposta negativa
print(nome, resposta)         # executado depois do bloco if-else

####
valor = int(input())
if valor % 2 == 0: 
  resposta = 'par'
else:
  resposta = 'ímpar'
print(valor, 'é', resposta)

####

nome = input()
idade = int(input())
if idade < 16:
  resposta = 'é muito cedo para você votar'
elif idade < 18:
  resposta = 'seu voto facultativo'
elif idade < 70:
  resposta = 'seu voto obrigatório'
else:
  resposta = 'seu voto facultativo'
print(nome, 'sua idade indica que', resposta)

####


# vamos observar o resultado das operações envolvendo dois valores
# constantes e tabelas-verdade

print(bool(True), bool(False))            # as constantes booleanas
print(bool(1), bool(0))                   # mapeamento de valores inteiros para booleanos
print(not 1, not 0)                       # tabela-verdade operador or
print(0 or 0, 0 or 1, 1 or 0, 1 or 1)     # tabela-verdade operador or 
print(0 and 0, 0 and 1, 1 and 0, 1 and 1) # tabela-verdade operador and 

###

a = int(input())
b = int(input())
c = int(input())
print(bool(a), bool(b), bool(c))
print((not a), (not b), not(c))
print((a or b), (a or b), (a or c), (b or c))
print((a and b), (a and b), (a and c), (b and c))
print((a or b or c), (a and b and c), (a and b or c), (a or b and c))
print(not(a or b), not(a or c), not(b or c))
print(not(a and b), not(a and c), not(b and c))

####

a = int(input())
b = int(input())

if a:
  if b: 
    print(a, 'and', b, ':', (a and b))
  else:
    print(a, 'and not', b, ':', (a and not b))
else:
  if b:
    print('not', a, 'and', b, ':', (not a and b))
  else:
    print('not', a, 'and', 'not', b, ':', (not a and not b))
print('fim')

###
