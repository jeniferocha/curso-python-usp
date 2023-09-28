valorMinimo = int(input())
soma = 0

while soma < valorMinimo:
    valores = int(input())
    soma += valores
    if soma == valorMinimo:
        break

sobra = soma - valorMinimo 
print("minimo", valorMinimo)
print("total", soma)
print("sobra", sobra)