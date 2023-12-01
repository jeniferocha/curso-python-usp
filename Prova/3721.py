dados = {}
linha = input()

while linha != "fim":
    nome, idade = linha.split()
    dados[nome] = int(idade)
    print(dados)
    linha = input()

