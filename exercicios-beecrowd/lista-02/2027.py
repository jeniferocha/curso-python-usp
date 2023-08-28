timeUm = str(input()) 
timeDois = str(input()) 
pontuacao = input() 

pontoTimeUm = "1"
pontoTimeDois = "2"
contadorTimeUm = 0
contadorTimeDois = 0
for pontos in pontuacao:     
    if pontos == pontoTimeUm:
        contadorTimeUm += 1
    elif pontos == pontoTimeDois:
        contadorTimeDois += 1   
    elif pontos == "0":
        print("Início do set")
        print(timeUm, contadorTimeUm) 
        print(timeDois, contadorTimeDois)
        break   

print(timeUm, contadorTimeUm) 
print(timeDois, contadorTimeDois)








