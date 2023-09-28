parado = 1
movimento = 0
dado = input()

while dado != "f":
    if dado == "p":
        parado +=1
    elif dado == "m":
        movimento +=1
    dado = input()

if parado >= movimento:
    print("sedentário")
else:
    print("ativo")