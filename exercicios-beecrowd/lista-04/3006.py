piorTaxaEstimativa = float(input())
quantidadeTaxas = int(input())

valoresTaxas = []

for item in range(quantidadeTaxas):
    taxa = float(input())
    valoresTaxas.append(float(taxa))

soma = 0

for item in valoresTaxas:
    if item > piorTaxaEstimativa:
        soma += 1

print(soma)
