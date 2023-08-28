numeroPalitosPorJogador = input().split()
palpitePalitosPorJogador = input().split()


listaNumerosPalitos = []
for elemento in numeroPalitosPorJogador:
    listaNumerosPalitos.append(int(elemento))
somaNumeroPalitosTotal = sum(listaNumerosPalitos)


listaPalpitePalitos = []
for item in palpitePalitosPorJogador:
    listaPalpitePalitos.append(int(item))

resultado = -1
tamanhoListaPalpitePalitos = len(listaPalpitePalitos)
for index in range(0, tamanhoListaPalpitePalitos):
    palpitePalitos = listaPalpitePalitos[index]
    if palpitePalitos == somaNumeroPalitosTotal:
        resultado = index + 1

print(resultado)
