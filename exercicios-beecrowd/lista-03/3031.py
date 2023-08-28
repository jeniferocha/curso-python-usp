cpfDigitado = input()

cpfCorrigido = cpfDigitado.replace(".", "").replace("-", "")
tamanho = len(cpfCorrigido)

if tamanho == 11 and cpfCorrigido.isdigit():
    print(cpfCorrigido)
elif tamanho == 11 and cpfCorrigido.isdigit() == False:
    print("ENCODING ERROR")
elif tamanho != 11 and cpfCorrigido.isdigit():
    print("SIZE ERROR")
elif tamanho != 11 and cpfCorrigido.isdigit() == False:
    print("ENCODING ERROR")
    print("SIZE ERROR")