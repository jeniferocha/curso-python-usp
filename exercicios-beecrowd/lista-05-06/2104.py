palavraInteira = str(input())

listaPalavraSoletrada = []

while True:
    palavraSoletrada = str(input())
    if palavraSoletrada == ".":
        break            
    else:
        listaPalavraSoletrada.append(palavraSoletrada)

verificar = ("".join(listaPalavraSoletrada))
if verificar == palavraInteira:       
    print("True")
else:      
    print("False")