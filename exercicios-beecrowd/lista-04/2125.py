diaAtual, mesAtual, anoAtual = input().split()
diaValidade, mesValidade, anoValidade = input().split()

diaAtual = int(diaAtual)
mesAtual = int(mesAtual)
anoAtual = int(anoAtual)
diaValidade = int(diaValidade)
mesValidade = int(mesValidade)
anoValidade = int(anoValidade)


if anoValidade > anoAtual + 1:
    print("na validade")
elif anoValidade == anoAtual + 1 and mesValidade >= mesAtual:
    print("na validade")
elif anoValidade == anoAtual and mesValidade > mesAtual:
    print("vence este ano")
elif anoValidade == anoAtual and mesValidade == mesAtual and diaValidade >= diaAtual:
    print("vence este mês")
else:
    print("vencido!")
