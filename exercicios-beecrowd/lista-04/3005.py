primeiroAno = int(input())
taxaPrimeiroAno = float(input())
segundoAno = int(input())
taxaSegundoAno = float(input())

if taxaPrimeiroAno == taxaSegundoAno:
    print("iguais")
elif taxaPrimeiroAno > taxaSegundoAno:
    print(primeiroAno)
elif taxaPrimeiroAno < taxaSegundoAno:
    print(segundoAno)