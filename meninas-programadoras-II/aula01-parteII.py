
n = int(input())
nomes = []
for item in range(n):
    nome = input()
    nomes.append(nome)
    print(nomes)
    #insere no final da lista


    n = int(input())
nomes = []
for item in range(n):
    nome = input()
    nomes.insert(nome)
    print(nomes)
    #Insere na posição 0

    tirar = int(input())
    nome = nomes.pop(tirar)
    print(nome)
    print(nomes)


