verso = input().lower()

a_substituir = [",", ".", '"', "'"]

for ponto in a_substituir:
    verso = verso.replace(ponto, "")

lista_de_palavras = verso.split()

dicionario = {}
for palavra in lista_de_palavras:
    if palavra in dicionario:
        dicionario[palavra] += 1
    else:
        dicionario[palavra] = 1

print(dicionario)
