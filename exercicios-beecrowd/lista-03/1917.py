nomeTimeUm = str(input())
nomeTimeDois = str(input())
pontosCadaSetTimeUm = input().split()
pontosCadaSetTimeDois = input().split()

listaPontosCadaSetTimeUm = []
for elemento in pontosCadaSetTimeUm:
    listaPontosCadaSetTimeUm.append(int(elemento))
somaPontosCadaSetTimeUm = sum(listaPontosCadaSetTimeUm)

listaPontosCadaSetTimeDois = []
for elemento in pontosCadaSetTimeDois:
    listaPontosCadaSetTimeDois.append(int(elemento))
somaPontosCadaSetTimeDois = sum(listaPontosCadaSetTimeDois)

for indice, pontuacao in enumerate(pontosCadaSetTimeUm):
    totalSets = indice+1

if somaPontosCadaSetTimeUm > somaPontosCadaSetTimeDois:
    print(nomeTimeUm, "(total",totalSets,"sets)")
elif somaPontosCadaSetTimeDois > somaPontosCadaSetTimeUm:
    print(nomeTimeDois, "(total",totalSets,"sets)")