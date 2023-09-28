maiorValor = 0
somaValores = 0

while True:
    valorDigitado = int(input())
    if valorDigitado == 0:
        print(maiorValor)
        break
    somaValores += valorDigitado
    if somaValores > maiorValor:
        maiorValor = somaValores    