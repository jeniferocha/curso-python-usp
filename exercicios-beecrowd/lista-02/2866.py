valorContaBancaria = int(input())
valorCarrinhoCompras = int(input())
calculo = valorContaBancaria - valorCarrinhoCompras 

if valorContaBancaria >= valorCarrinhoCompras:
    print("se você comprar tudo o saldo será: ",calculo)
else:
    print("seu saldo é insuficiente para essa compra")