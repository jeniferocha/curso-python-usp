def montar_dicionario_tarefa_tempo():
  dicionario_tarefa_tempo = {}
  tarefa_id = 0

  linha = input()

  while linha != '.':    
    recortada = linha.split()


    tempo = int(recortada[0])
   
    restante_da_lista_recortada = recortada[1:]
    
    tarefa = " ".join(restante_da_lista_recortada)
    
    dicionario_tarefa_tempo[tarefa_id] = [tarefa, tempo]   

    linha = input()

    tarefa_id += 1

  return dicionario_tarefa_tempo



def listar_tarefas_de_tempo_curto(dicionario): 
  tarefas_de_tempo_curto = []

  for tarefa_id in dicionario:
    tempo = dicionario[tarefa_id][1]
    tarefa = dicionario[tarefa_id][0]

    if tempo <= 3:
      tarefas_de_tempo_curto.append(tarefa)

  return tarefas_de_tempo_curto


def listar_tarefas_longas(dicionario, tarefas_curtas): 
  tarefas_longas = []

  for tarefa_id in dicionario:
    tarefa = dicionario[tarefa_id][0]

    if tarefa not in tarefas_curtas:
      tarefas_longas.append(tarefa)

  return tarefas_longas

dicionario = montar_dicionario_tarefa_tempo()

tarefas_curtas = listar_tarefas_de_tempo_curto(dicionario)

tarefas_longas = listar_tarefas_longas(dicionario, tarefas_curtas)


for tarefa in tarefas_curtas:
  print('Fazer agora a tarefa:', tarefa)
print(tarefas_longas)