def calcularRaizes(a, b, c):    
    delta = (b**2 - 4*a*c)
    if delta > 0:
        return 2  
    elif delta == 0:
        return 1  
    else:
        return 0  

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

numeroRaizes = calcularRaizes(a, b, c)
print(numeroRaizes)