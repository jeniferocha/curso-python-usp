#Eu divido, tu divides, ela divide: com resto

primeiroValor = int(input())
operador = (input())
segundoValor = int(input())
if operador == "%":
    print(primeiroValor % segundoValor)
elif operador == "/": 
    print("%.2f" % (primeiroValor / segundoValor))
elif operador == "//":
    print(primeiroValor // segundoValor)




