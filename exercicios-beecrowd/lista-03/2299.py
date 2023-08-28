numeroTabuada = int(input())
numeroInicio = int(input())
numeroFim = int(input())

print("Tabuada do",numeroTabuada, "de", numeroInicio, "até", numeroFim)
for item in range(numeroInicio,numeroFim+1):
  calculo = numeroTabuada * item
  print(numeroTabuada, "x" ,item, "=" ,calculo)

 