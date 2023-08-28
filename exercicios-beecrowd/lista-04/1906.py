listaTodosVotos = []

totalVotosCandidataUm = input()
listaTodosVotos.append(int(totalVotosCandidataUm))
totalVotosCandidataDois = input()
listaTodosVotos.append(int(totalVotosCandidataDois))
totalVotosCandidataTres = input()
listaTodosVotos.append(int(totalVotosCandidataTres))
totalVotosCandidataQuatro = input()
listaTodosVotos.append(int(totalVotosCandidataQuatro))

maiorNumeroVotos = 0

for voto in listaTodosVotos:
    if maiorNumeroVotos < voto:
        maiorNumeroVotos = voto

print("maior:", maiorNumeroVotos)