palavraEncontrada = str(input())
contador = 0

while True:
    entrada = str(input())

    if entrada == ".":
        break
  
    contador += entrada.count(palavraEncontrada)

print(contador)
