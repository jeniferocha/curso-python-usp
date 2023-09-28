def maiorValor(lista):
    maior = lista[0]
    for valor in lista:
        if valor > maior:
            maior = valor      
    return maior

entrada = input()
listaInteiros = [int(x) for x in entrada.split()]
resultado = maiorValor(listaInteiros)
print(resultado)