frases = []

while True:
    frase = input()
    if frase == "CDA":
        frases.append("CDA 1942")
        break
    else:
        frases.append(frase)

for frase in frases:
    print(frase)