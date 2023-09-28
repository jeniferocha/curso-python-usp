resultado1 = "No"
resultado2 = "No"
resultado3 = "No"
resultado4 = "No"

while True:
    submeter = str(input())

    if submeter == "accepted 1":
        resultado1 = "Yes"
    elif submeter == "accepted 2":
        resultado2 = "Yes"
    elif submeter == "accepted 3":
        resultado3 = "Yes"
    elif submeter == "accepted 4":
        resultado4 = "Yes"
    elif submeter == "timeout":
        print(resultado1, resultado2, resultado3, resultado4)
        break