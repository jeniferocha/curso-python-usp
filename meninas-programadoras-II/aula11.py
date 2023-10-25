# FUNÇÃO 1
def montar_dicionario_tarefa_tempo():
  # dicionario para receber tempo: tarefa
  # {1: ['Tocar violão', 25]}
  dicionario_tarefa_tempo = {}
  tarefa_id = 0

  # ler linha como string
  linha = input()

  # enquanto linha lida é diferente de ., ler as proximas
  while linha != '.':
    # recortar a linha, pra reconhecer o tempo e a tarefa
    recortada = linha.split()

    # recortada = ['25', 'tocar', 'violão']
    # ------

    # tranformar o tempo em inteiro
    tempo = int(recortada[0])

    # separar toda a lista exceto o primeiro elemento (que é nosso tempo)
    restante_da_lista_recortada = recortada[1:]

    # juntar toda a lista em uma string separa por espacos
    # para voltar a tarefa no sua versão original
    tarefa = " ".join(restante_da_lista_recortada)

    # atualizar nosso dicionar de tempo: tarefa
    dicionario_tarefa_tempo[tarefa_id] = [tarefa, tempo]
    # -----

    # receber uma nova linha
    linha = input()

    # id unico de tarefas
    tarefa_id += 1

  return dicionario_tarefa_tempo



# FUNÇÃO 2
def listar_tarefas_de_tempo_curto(dicionario):
  # criar lista para armazenar tarefas com tempo menor ou igual a 3
  tarefas_de_tempo_curto = []

  # para cada chave do par {chave:valor} do dicionario de id:[tarefa,tempo]
  for tarefa_id in dicionario:

    # reconhecer o tempo associado a essa tarefa
    tempo = dicionario[tarefa_id][1]
    tarefa = dicionario[tarefa_id][0]

    # atualizar a lista de tarefas com tempo curto
    if tempo <= 3:
      tarefas_de_tempo_curto.append(tarefa)

  return tarefas_de_tempo_curto


# FUNÇÃO 3

def listar_tarefas_longas(dicionario, tarefas_curtas):
  # criar lista para armazenar tarefas com tempo maior que 3
  tarefas_longas = []

  # para cada tarefa (que são as chaves do nosso dicionario)
  for tarefa_id in dicionario:

    tarefa = dicionario[tarefa_id][0]

    # se tarefa não tá presente na lista de tarefas curtas
    # então ela é uma tarefa longa
    if tarefa not in tarefas_curtas:

      # atualizar lista de tarefas longas
      tarefas_longas.append(tarefa)

  return tarefas_longas

dicionario = montar_dicionario_tarefa_tempo()
# {'Tocar violão': 25, 'Cantar 'Cálice': 3}
tarefas_curtas = listar_tarefas_de_tempo_curto(dicionario)
# ['Cantar 'Cálice']
tarefas_longas = listar_tarefas_longas(dicionario, tarefas_curtas)
# ['Tocar violão]

for tarefa in tarefas_curtas:
  print('Fazer agora a tarefa:', tarefa)
print(tarefas_longas)