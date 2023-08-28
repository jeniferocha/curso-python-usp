# Calcular o delta de uma equação de 2o grau completa
# Notem, na preparação inicial da mensagem de resposta,
#   o uso da função str() para converter o valor de delta, 
#   que é um inteiro, para uma string; isso permite concactenar,
#   por meio do operador de adição, a string resultante 
#   com a primeira parte de mensagem

a = int(input())                  #obter os coeficientes
b = int(input())
c = int(input())
delta = (b * b) - (4 * a * c)     # calcular o delta
resposta = 'delta= ' + str(delta) # preparar resposta
if delta < 0:
  resposta = resposta + ': sem raízes reais'
elif delta == 0:
  resposta = resposta + ': uma raíz real'
else:
  resposta = resposta + ': duas raízes'
print(resposta)

###
# Calcular as raízes de uma equação de 2o grau completa

a = float(input())                  #obter os coeficientes
b = float(input())
c = float(input())
delta = (b * b) - (4 * a * c)     # calcular o delta
print(delta)
resposta = 'delta= ' + str(delta) # preparar resposta
if delta < 0:
  resposta = resposta + ': sem raízes reais'
elif delta == 0:
  x = -b / (2 * a)
  resposta = resposta + ': uma raíz real ('+ str(x)+')'
else:
  raiz2_delta = (delta)**(1/2)     # usamos potência de 1/2 para calcular a raiz quadrada
  print(raiz2_delta)
  x1 = (-b + raiz2_delta) / (2 * a)   
  x2 = (-b - raiz2_delta) / (2 * a)  
  resposta = resposta + ': duas raízes reais (' + str(x1) + ', ' + str(x2)+')'
print(resposta)


###

