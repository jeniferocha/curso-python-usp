numeroUm = int(input())
numeroDois = int(input())
numeroTres = int(input())
numeroQuatro = int(input())

calculoNumeroUm = numeroUm * (2 ** 3)
calculoNumeroDois = numeroDois * (2 ** 2)
calculoNumeroTres = numeroTres * (2 ** 1)
calculoNumeroQuatro = numeroQuatro * (2 ** 0)

resultado = (
    calculoNumeroUm
    + calculoNumeroDois
    + calculoNumeroTres
    + calculoNumeroQuatro
)
print(resultado)