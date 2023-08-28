quantidadeAreaDesmatada = float(input())
taxaDesmatamento = float(input())

taxaDecimal = taxaDesmatamento / 100

quantidadeAreaAnoAnterior = quantidadeAreaDesmatada / (1 + taxaDecimal)

print("%.1f" % quantidadeAreaAnoAnterior)
