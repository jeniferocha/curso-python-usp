valor = int(input())
resultado = ""

if valor == 0:
  resultado = "."
else:
  for i in range(valor):
      resultado = resultado + "*"

print(resultado)
