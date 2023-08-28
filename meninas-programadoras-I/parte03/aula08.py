dim = int(input())
for i in range(dim):
  print('*')
  for j in range(dim):
    print('-')
print('fim')

###
dim = int(input())
for i in range(dim):
  print('*', end='')
  for j in range(dim):
    print('-', end='')
print('fim')

###
dim = int(input())
for i in range(dim):
  print('*', end='')
  for j in range(dim):
    print('-', end='')
print('\nfim')

###
dim = int(input())
for i in range(dim):
  for j in range(dim):
    print('*', end='')
  print()
print('fim')

###
dim = int(input())
for i in range(dim):
  for j in range(dim):
    if i == j:
      print(' ', end='')
    else:
      print('*', end='')
  print()
print('fim')

###
dim = int(input())
for i in range(dim):
  for j in range(dim):
    if i + j == dim:
      print(' ', end='')
    else:
      print('*', end='')
  print()
print('fim')

###
dim = int(input())
for i in range(dim):
  for j in range((i)):
    print('*', end='')
  print()
print('fim')

###
dim = int(input())
for i in range(dim):
  for j in range((dim-i)):
    print('*', end='')
  print()
print('fim')

###
dim = int(input())
for i in range(dim):
  for j in range((i)):
    print('*', end='')
  print()
for i in range(dim):
  for j in range((dim-i)):
    print('*', end='')
  print()
print('fim')

