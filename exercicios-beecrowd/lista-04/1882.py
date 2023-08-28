qtdadeMeninasIniciais = int(input())
qtdadeDiasIniciais = int(input())
qtdadeMonitoresIniciais = int(input())

demandaAlunas = int(input())
demandaDias = int(input())

parteI = (qtdadeMeninasIniciais * qtdadeDiasIniciais) 
parteII = (demandaAlunas * demandaDias)
parteII = qtdadeMonitoresIniciais * parteII
demandaMonitor = parteII / parteI

print("%.0f" % demandaMonitor)

