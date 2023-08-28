valor_depositado = float(input())
rendimento_poupanca = float(input())
calculo_rendimento = valor_depositado * (rendimento_poupanca / 100)
valor_conta = calculo_rendimento + valor_depositado
print("%.2f" % valor_conta)
