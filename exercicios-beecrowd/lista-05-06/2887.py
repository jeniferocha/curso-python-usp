contadorX = 0
contadorN = 0
contadorM = 0

while True:
    pesoCrianca = input()
    if pesoCrianca == ".":
        break
    elif pesoCrianca == "X":
        contadorX +=1
    elif pesoCrianca == "N":
        contadorN +=1
    elif pesoCrianca == "M":
        contadorM +=1

totalCriancas = contadorX + contadorM + contadorN
print("Abaixo do peso:", contadorX)
print("Peso normal:", contadorN)
print("Acima do peso:", contadorM)
print("Total de crianças:", totalCriancas)   