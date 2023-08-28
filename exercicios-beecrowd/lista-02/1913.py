opcoesLista = str(input())

if opcoesLista == "s":
    valorCaracteres = input()
    caracteres = valorCaracteres.split()
    listaCaracteres = []
    for elemento in caracteres:
        listaCaracteres.append(str(elemento))
    print(listaCaracteres)
elif opcoesLista == "n":
    valorDecimal = input()
    decimal = valorDecimal.split()    
    listaDecimal = []
    for elemento in decimal:
        listaDecimal.append(float(elemento))
    print(listaDecimal)
elif opcoesLista == "f":
     valorInteiro = input()
     inteiro = valorInteiro.split()
     listaInteiro = []
     for elemento in inteiro:
        listaInteiro.append(int(elemento))
     print(listaInteiro)