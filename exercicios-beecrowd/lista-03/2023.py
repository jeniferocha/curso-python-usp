palavra = input()

listaPalavra = []

palavraInvertida = ""

for indice, letra in enumerate(palavra):
    listaPalavra.append(letra)

while listaPalavra != []:
    letra = listaPalavra.pop()
    palavraInvertida += letra

if palavra == palavraInvertida:
    print("S")
else:
    print("N")



