#Volei: set

pontosEquipe1 = int(input())
pontosEquipe2 = int(input())

if pontosEquipe1 >= 25 and pontosEquipe1 - pontosEquipe2 >= 2:
    print("S")
elif pontosEquipe2 >= 25 and pontosEquipe2 - pontosEquipe1 >= 2:
    print("S")
else: 
    print("N")


