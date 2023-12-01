def ordenar_lista(lista):
    nova_lista = []
    print("-", lista)

    while lista:
        print("+", nova_lista)
        menor_elemento = min(lista)
        nova_lista.append(menor_elemento)
        lista.remove(menor_elemento)
        if lista:
            print("-", lista)

    return nova_lista

entrada = input()
lista_original = [int(x) for x in entrada.split()]
lista_ordenada = ordenar_lista(lista_original)
print("-", lista_original)
print("+", lista_ordenada)
