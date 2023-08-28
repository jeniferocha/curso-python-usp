quantidadeTaxas = int(input())
maiorValorDigitado = 0
for i in range(quantidadeTaxas): 
    valoresTaxas = float(input())  
    if valoresTaxas > maiorValorDigitado:
        maiorValorDigitado = valoresTaxas 
print("%.2f" % maiorValorDigitado)


