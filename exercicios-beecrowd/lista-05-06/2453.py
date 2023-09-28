numeroVelas = int(input())
contador = 0
while True:
    sopro = str(input())

    if sopro == "fuuuuuuu":
        contador += 1
        print("bom sopro!")
    elif sopro == "fu":
        print("precisa de muito mais força no sopro!")
    elif sopro == "fuuu":
        print("um pouco mais de força no sopro!")
    
    if numeroVelas == contador:
        print("Parabéns para pelo seu aniversário de", numeroVelas, "anos!")
        break