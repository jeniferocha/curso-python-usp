cartaMeninaUmDuplaUm = int(input())
cartaMeninaUmDuplaDois = int(input())
cartaMeninaDoisDuplaUm = int(input())
cartaMeninaDoisDuplaDois = int(input())

maiorCartaDuplaUm = 0
maiorCartaDuplaDois = 0

if cartaMeninaUmDuplaUm > cartaMeninaDoisDuplaUm:
    maiorCartaDuplaUm = cartaMeninaUmDuplaUm
else: 
    maiorCartaDuplaUm = cartaMeninaDoisDuplaUm

if cartaMeninaUmDuplaDois > cartaMeninaDoisDuplaDois:
    maiorCartaDuplaDois = cartaMeninaUmDuplaDois
else: 
    maiorCartaDuplaDois = cartaMeninaDoisDuplaDois

if maiorCartaDuplaUm > maiorCartaDuplaDois:
    print(maiorCartaDuplaUm)
elif maiorCartaDuplaDois > maiorCartaDuplaUm:
    print(maiorCartaDuplaDois)
else: 
    print("empate")