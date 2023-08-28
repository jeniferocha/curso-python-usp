#Variável?

temErro = False
palavra = str(input())
if palavra[0].isalpha() or palavra[0] == "_":
    for letra in palavra:     
        if letra.isalnum() == False and letra != "_":
           temErro = True
           break         
else:
   temErro = True

if temErro == True:
    print("ERROR")
else:
    print("OK")







