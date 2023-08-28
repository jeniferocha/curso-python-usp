quantidade = int(input())
contador = 0

for item in range(quantidade):
  email = input()
  for i in email:
    if i == "@":
      contador += 1

print(quantidade - contador)
