quantidadeMovimentacao = int(input())
alimentacao = 0
moradia = 0
transporte = 0
saude = 0
lazer = 0
salario = 0
prestacaoServico = 0

contador = 0
while quantidadeMovimentacao > contador:
    contador += 1
    valor = float(input())
    letraOrigem = str(input()).upper()
    if valor > 0:
        if letraOrigem == "S":
            salario += valor
        elif letraOrigem == "P":
            prestacaoServico += valor
    else:
        if letraOrigem == "A":
            alimentacao += valor
        elif letraOrigem == "M":
            moradia += valor
        elif letraOrigem == "T":
            transporte += valor
        elif letraOrigem == "S":
            saude += valor
        elif letraOrigem == "L":
            lazer += valor
totalRenda = salario + prestacaoServico
totalGastos = alimentacao + moradia + transporte + saude + lazer
balanco = totalRenda + (totalGastos)
print("Movimentações")
if alimentacao != 0:
    print("  Alimentação: %.2f" % alimentacao)
if moradia != 0:
    print("  Moradia: %.2f" % moradia)
if transporte != 0:
    print("  Transporte: %.2f" % transporte)
if saude != 0:
    print("  Saúde: %.2f" % saude)
if lazer != 0:
    print("  Lazer: %.2f" % lazer)
if salario != 0:
    print("  Salário: %.2f" % salario)
if prestacaoServico != 0:
    print("  Prestação de serviços: %.2f" % prestacaoServico)

print("Total de Renda: %.2f" % totalRenda)
print("Total de Gastos: %.2f" % totalGastos)
print("Balanço: %.2f" % balanco)
