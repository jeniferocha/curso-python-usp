piorEstimativa = float(input())
contador = 0
soma = 0
taxaObservacao = float(input())

while taxaObservacao != -1:
    contador += 1
    if taxaObservacao < piorEstimativa:
        soma += 1
    taxaObservacao = float(input())

print(contador, soma)
