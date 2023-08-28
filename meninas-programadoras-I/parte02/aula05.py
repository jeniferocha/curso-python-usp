genero = input('gênero: F ou M? ')
if genero == 'F':
  nome = input('nome: ')
  resposta = 'Bem-vinda ' + nome + '!\n'
  mae = input('mãe: S ou N?')
  if mae == 'S':
    filhos = input('nome dos filhos: ')
    resposta += 'Para o evento, traga seus filhos: ' + filhos
  else:
    resposta += 'para o evento, traga alguma criança'
else:
  resposta = 'Evento apena para pessoas do gênero Feminino'
print(resposta)

###
sensor = input()
if sensor == 'alho':
  print('vá para a esquerda')
  sensor = input()
  if sensor == 'grande':
    print('vá para a esquerda')
  else: # pequeno
    print('vá para a direita')
else: # bugalho
  print('vá para a direita')
  sensor = input()
  if sensor == 'mole':
    print('vá para a esquerda')
  else: #duro
    print('vá para a direita')

    ###


    nome = input()
if 'a' in nome:   # verifica se 'a' está contida em nome
  print('contém a')
else:
  print('não contém a')  

  ##

  original = input()
parte = input()
if parte in original: # verifica se parte está contida em orignal
  print(original, 'contém', parte)
else:
  print(original, 'não contém', parte)


###

original = input()
parte = input()
if parte.lower() in original.lower(): # compara os valores convertidos usando lower() sem sobrescrever as versões originais
  print(original, 'contém', parte)
else:
  print(original, 'não contém', parte)

  ##


  original = input()
parte = input()
if parte.upper() in original.upper(): # compara os valores convertidos usando upper() sem sobrescrever as versões originais
  print(original, 'contém', parte)
else:
  print(original, 'não contém', parte)

  ###


  print("banana".count('na'))
print("oftalmotorrinolaringologista".count('o'))

print("men1nas".isalnum())
print("meninas".isalnum())

print("men1nas".isalpha())
print("meninas".isalpha())

print("men1nas".isdigit())
print("5647282910".isdigit())

###
