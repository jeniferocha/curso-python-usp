nomeTimeUm = str(input())
nomeTimeDois = str(input())
pontosCadaTimeUltimoPonto = input().split()

listapontosCadaTimeUltimoPonto = []
for elemento in pontosCadaTimeUltimoPonto:
    listapontosCadaTimeUltimoPonto.append(int(elemento))

if listapontosCadaTimeUltimoPonto[2] == 1:
    placarTimeUm = listapontosCadaTimeUltimoPonto[0] + 1   
    print(nomeTimeUm, placarTimeUm)
    print(nomeTimeDois, listapontosCadaTimeUltimoPonto[1]) 
elif listapontosCadaTimeUltimoPonto[2] == 2:
    placarTimeDois = listapontosCadaTimeUltimoPonto[1] + 1
    print(nomeTimeUm, listapontosCadaTimeUltimoPonto[0])
    print(nomeTimeDois, placarTimeDois)