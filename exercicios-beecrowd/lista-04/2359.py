numeroAlunas = int(input())

for item in range(numeroAlunas):
    nomeAluna = input()
    monitoria1 = int(input())
    monitoria2 = int(input())
    monitoria3 = int(input())
    monitoria4 = int(input())    
    if monitoria1 >= 120 and monitoria2 >= 120 and monitoria3 >= 120 and monitoria4 >= 120:
        print(nomeAluna, "tem monitorias OK! :-)")
    else:
        print(nomeAluna, "não tem monitorias suficientes :-(")
