nomes = []
print(nomes)

nomes = ["Jenifer","Thiago","Maya"]
print(nomes)

inteiros = [9,7,4,6,3,1]
print(inteiros)

reais = [3.14, 9.98]
print(reais)

############

bagunca = ["Jenifer",62,"Florinopolis",1.641]
print(bagunca)

######
lista = [1,[2,3],[5],["Maria","Fernanda"]]
print(lista)

#####

lista2 = [1,[2,3],[5],["Maria","Fernanda"]]

for item in lista:
    print(item)

####

lista2 = [1,[2,3],[5],["Maria","Fernanda"]]
tamanho = len(lista2)
print(tamanho)

#######

lista3 = [1,34,55,66,77,89,44,6666,3222,4455]
tamanho = len(lista3)
print(tamanho)

lista3 = [1,34,55,66,77,89,44,6666,3222,4455,22]
print(lista3[0])
print(lista3[7])
print(lista3[-1])
#print(lista3[11]) da erro de sintaxe

##


n = int(input())
nomes = []
for item in range(n):
    nome = input()
    nomes.append(nome)
    print(nomes)
