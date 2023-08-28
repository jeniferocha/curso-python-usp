

valorProduto = float(input())
valorDesconto = float(input())
valorEconomizado = valorProduto * (valorDesconto / 100)
valorProdutoDesconto = valorProduto - valorEconomizado
print("%.2f" % valorProduto)
print("%.2f" % valorProdutoDesconto)
print("%.2f" % valorEconomizado)  