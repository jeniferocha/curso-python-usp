valorParaGastar = float(input())
somaValores = 0
contador = 0
saldo = valorParaGastar
while True:   
    valorItem = float(input())    
    somaValores += valorItem
    
    if somaValores <= valorParaGastar:
        contador += 1
        saldo = float(valorParaGastar) - float(somaValores)
    elif somaValores >= valorParaGastar:
        print("Número de itens", contador)
        print('Saldo:',('%.2f' % saldo))
        break