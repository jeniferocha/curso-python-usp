contador = 0

while True:
    submeter = str(input())

    if submeter == "accepted":
        contador +=1
    elif submeter == "timeout":
        print(contador)
        break