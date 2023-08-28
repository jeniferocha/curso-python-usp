algorismosDigitado = input()
   
caracteres = algorismosDigitado.split()
listaCaracteres = []
for elemento in caracteres:
    listaCaracteres.append(str(elemento))
print(listaCaracteres)

dobroValorInteiro = algorismosDigitado.split()    
listaValorInteiro = []
for elemento in dobroValorInteiro:
    listaValorInteiro.append(int(elemento)+int(elemento))
print(listaValorInteiro)


metadeValorInteiro = algorismosDigitado.split()
listaMetadeValor = []
for elemento in metadeValorInteiro:
    listaMetadeValor.append(float(elemento)/2)
print(listaMetadeValor)

print(len(listaCaracteres))