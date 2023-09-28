# linha = input()
# print([linha])
# separada = linha.split()
# print(separada)


linha = input()
separador = input()
print([linha])
separada = linha.split(separador)
print(separada)

# usando o mesmo exemplo de cima para função

def separar_elementos_de_string(linha, separador):    
    print([linha])
    separada = linha.split(separador)
    print(separada)
#define os parametros da função
linha = input()
separador = input()
#chama a função
separar_elementos_de_string(linha, separador)


#Gerar listas com numeros inteiros
linha = input().split() #quebrar e por em lista de strings
print(linha)
lista = []
for item in linha:
    inteiro = int(item) #transformar pra inteiro
    lista.append(inteiro) # add na lista vazia o numero inteiro
print(lista)


