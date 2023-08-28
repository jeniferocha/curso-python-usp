original = input()      # string onde queremos procurar um caractere
caractere = input()     # caractere a ser procurado
contador = 0            # começamos a contar a partir do zero

for letra in original:
  if letra == caractere: 
    contador += 1       # atalho para contador = contador + 1
print(contador)

####

original = input()  
vogais = input()
contador = 0      # começamos a contar a partir do zero

for letra in original:
  if letra in vogais: 
    contador += 1       # atalho para contador = contador + 1
print(contador)


###
original = input()
trocar = input()
resultado = ''
for letra in original:
  if letra in trocar:
    resultado += '*'
  else:
    resultado += letra
print(resultado)

##

cpf = input()   # não convertemos para inteiro pois tratamos o valor com cadeia de caracteres
resultado = ''  # vai apontar para o CPF com os separadores
contador = 0    # vai controlar quando devemos inserir os separadores
for digito in cpf:
  resultado += digito                 # somamos strings aqui!
  contador += 1                       # avançamos com o contador
  if contador == 3 or contador == 6:
    resultado += '.'
  elif contador == 9:
    resultado += '-'
print(resultado)

###

cpf = input()   # não convertemos para inteiro pois tratamos o valor com cadeia de caracteres

# colocamos as máscaras

resultado = ''  # vai apontar para o CPF com os separadores
contador = 0    # vai controlar quando devemos inserir os separadores
for digito in cpf:
  contador += 1           # avançamos com o contador
  if contador % 2 == 0:   # se for casa par
    resultado += '*'
  else:
    resultado += digito
print(resultado)

# reinicializamos cpf, resultado e contador
cpf = resultado
resultado = ''
contador = 0

# colocamos os separadores

for digito in cpf:
  resultado += digito                 # somamos strings aqui!
  contador += 1                       # avançamos com o contador
  if contador == 3 or contador == 6:
    resultado += '.'
  elif contador == 9:
    resultado += '-'
print(resultado)


###
