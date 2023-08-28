numeroVotos = int(input())

somaVotoX = 0
somaVotoY = 0
somaVotoBeN = 0
for votos in range(0, numeroVotos):
    voto = input()
    if voto == "X":
        somaVotoX += 1
    elif voto == "Y":
        somaVotoY += 1
    elif voto == "B" or voto == "N":
        somaVotoBeN += 1

print("X", somaVotoX)
print("Y", somaVotoY)
print("Brancos e nulos", somaVotoBeN)

if somaVotoX > somaVotoY:
    print("vitoria: X")
elif somaVotoX < somaVotoY:
    print("vitoria: Y")
else:
    print("empate!")
