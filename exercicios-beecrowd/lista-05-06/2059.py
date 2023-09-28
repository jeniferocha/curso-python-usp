criptografar = int(input())
descriptografar = str(input())

if criptografar == 0:    
    descriptografar = descriptografar.replace("a", "@").replace("A", "@").replace('e', "&").replace("E", "&").replace("o", "*").replace("O", "*")
    print(descriptografar)
elif criptografar == 1:
    descriptografar = descriptografar.replace("@", "a").replace("@", "A").replace('&', "e").replace("&", "E").replace("*", "o").replace("*", "O")
    print(descriptografar)