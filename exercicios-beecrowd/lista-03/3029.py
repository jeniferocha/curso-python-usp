quantidade = int(input())
contador = 0

for item in range(quantidade):
    email = input()
    if "gmail" not in email:
        contador += 1

print(contador)
