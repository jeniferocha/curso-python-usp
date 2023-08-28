manilhasFixas = ["4Paus", "7Copas", "AEspadas", "7Ouros"]

listaCartasJogadas = []
cartaUm = input()
listaCartasJogadas.append(str(cartaUm))
cartaDois = input()
listaCartasJogadas.append(str(cartaDois))
cartaTres = input()
listaCartasJogadas.append(str(cartaTres))

soma = 0

for item in listaCartasJogadas:
    if item in manilhasFixas:
        soma += 1

print(soma)