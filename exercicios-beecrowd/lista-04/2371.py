mlXicara = 240
mlColherSopa = 15
mlColherCha = 5

quantidadeXicaras = int(input())
quantidadeColherSopa = int(input())
quantidadeColherCha = int(input())

if quantidadeXicaras > 0:
    calculoMlXicara = quantidadeXicaras * mlXicara
else:
    calculoMlXicara = 0

if quantidadeColherSopa > 0:
    calculoMlColherSopa = quantidadeColherSopa * mlColherSopa
else:
    calculoMlColherSopa = 0

if quantidadeColherCha > 0:
    calculoMlColherCha = quantidadeColherCha * mlColherCha
else:
    calculoMlColherCha = 0

print(calculoMlXicara, "ml")
print(calculoMlColherSopa, "ml")
print(calculoMlColherCha, "ml")