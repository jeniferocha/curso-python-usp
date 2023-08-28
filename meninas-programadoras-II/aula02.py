# nome = "Jenifer"
# for letra in nome:    
#     print(letra)

# nome = input()
# for letra in nome:    
#     print(letra)


# nome = input()
# for letra in nome:    
#     print(letra, end="-")



# nome = input()
# tamanho = len(nome)
# for indice in range(tamanho):
#     letra = nome[indice]
#     if letra in "aeiou":
#         print("vogal")
#     else:
#         print("Não vogal")


# nome = "Jenifer Rocha"
# lista = nome.split()
# print(lista)

# nome = input()
# lista = nome.split()
# print(lista)

# a, b, c = input().split()
# print(a, b, c)

# a, b, c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# print(a + b + c)

# nome, sobrenome = input().split()
# print(nome)
# print(sobrenome)

# nome = input().split()
# print(nome)

# nome = input().split()
# tamanho = len(nome)
# print(nome, "tem", tamanho, "elementos")

# nome = input().split()    
# tamanho = len(nome)
# for i in nome:
#     print(i)    
# print(nome, "tem", tamanho, "elementos")


# inteiros = input().split()    
# soma = 0
# for i in inteiros:
#     i = int(i)
#     soma += i
# print(soma) 



# inteirosComoStrings = input().split()    
# listaDeInteiros = []
# for item in inteirosComoStrings:
#     item = int(item)
#     listaDeInteiros.append(item)   
# print(listaDeInteiros) 


listaDeInteiros = [int(item) for item in input().split()]
print(listaDeInteiros)

listaDeStrings = [item.upper() for item in input().split()]
print(listaDeStrings)





