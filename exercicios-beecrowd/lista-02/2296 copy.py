quantidadeMovimentacao = int(input())

opcoes = {
   "A": 0,
   "M": 0,
   "T": 0,
   "S": 0,
   "L": 0,
   "SALARIO": 0,
   "P": 0,
}

for i in range(quantidadeMovimentacao):
   valor = float(input())
   letraOrigem = str(input()).upper()
   if valor > 0:
    if letraOrigem == "S":
     opcoes["SALARIO"] += valor
    elif letraOrigem == "P":
        opcoes["P"] += valor
    else:
         opcoes[letraOrigem] += valor

totalRenda = opcoes["SALARIO"] + opcoes["P"] 
totalGastos = sum(opcoes.values()) - totalRenda
balanco = (totalRenda) - (-totalGastos) 
print("Movimentações")
if opcoes["A"] != 0:
   print("Alimentação:","%.2f" % opcoes["A"])
if opcoes["M"] != 0:
   print("Moradia:","%.2f" % opcoes["M"])
if opcoes["T"] != 0:
   print("Transporte:","%.2f" % opcoes["T"])
if opcoes["S"] != 0:
   print("Saúde:","%.2f" % opcoes["S"])
if opcoes["L"] != 0:
   print("Lazer:","%.2f" % opcoes["L"])
if opcoes["SALARIO"] != 0:
   print("Salário:","%.2f" % opcoes["SALARIO"])
if opcoes["P"] != 0:
   print("Prestação de serviços:","%.2f" % opcoes["P"])

print("Total de Renda:","%.2f" % totalRenda)
print("Total de Gastos:","%.2f" % totalGastos)
print("Balanço:","%.2f" % balanco)