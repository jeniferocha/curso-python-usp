valoresTaxas = 9999999999
maiorValorDigitado = 0
while 0 < valoresTaxas:
    valoresTaxas = float(input())
    if valoresTaxas > maiorValorDigitado:
        maiorValorDigitado = valoresTaxas 
print("%.2f" % maiorValorDigitado)


