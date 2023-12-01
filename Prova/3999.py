def extrair_elementos_centrais(array, indice_central):
    novo_array = []
    
    if len(array) % 2 == 0: 
        meio = len(array) // 2
        novo_array.append(array[meio])  
        for i in range(1, meio + 1):
            if meio - i >= 0:
                novo_array.append(array[meio - i])  
            if meio + i < len(array):
                novo_array.append(array[meio + i]) 
    else: 
        meio = len(array) // 2
        novo_array.append(array[meio])  
        for i in range(1, meio + 1):
            if meio + i < len(array):
                novo_array.append(array[meio + i])  
            if meio - i >= 0:
                novo_array.append(array[meio - i])  

    return novo_array[:indice_central]  


entrada_array = input()
array = list(map(int, entrada_array.split()))
indice_central = int(input().format(len(array) - 1))

resultado = extrair_elementos_centrais(array, indice_central)

print(array)
print(resultado)
