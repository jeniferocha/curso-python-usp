condicaoParada = input()
contador = 0
while True:
    condicaoEntrada = input()
    if condicaoEntrada != condicaoParada:
        contador += 1
    else:
        print(contador)
        break