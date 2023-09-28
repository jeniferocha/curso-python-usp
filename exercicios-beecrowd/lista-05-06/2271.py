numeroAlvo = int(input())

while True:
    palpite = int(input())
    if palpite == numeroAlvo:
        print("igual")
        break
    elif palpite < numeroAlvo:
        print("maior")
    else:
        print("menor")