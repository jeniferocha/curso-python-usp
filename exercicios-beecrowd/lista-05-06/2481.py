somaNotas = 0

while True:
    valorNota = int(input())

    if valorNota == 0:
        print(somaNotas)
        break
    else:
        somaNotas += valorNota    