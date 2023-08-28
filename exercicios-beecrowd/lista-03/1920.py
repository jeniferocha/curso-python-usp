numeroUm = int(input())
numeroDois = int(input())
numeroTres = int(input())
numeroQuatro = int(input())

calculoNumeroUm = numeroUm * (10 ** 3)
calculoNumeroDois = numeroDois * (10 ** 2)
calculoNumeroTres = numeroTres * (10 ** 1)
calculoNumeroQuatro = numeroQuatro * (10 ** 0)

resultado = (
    (calculoNumeroUm * 2)
    + (calculoNumeroDois * 2)
    + (calculoNumeroTres * 2)
    + (calculoNumeroQuatro * 2)
)
print(resultado)