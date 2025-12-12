import random

n = 0
darabszam = 0 

while n < 20:
    szam = random.randint(1, 12)
    if szam % 3 == 0:
        print(szam)
        darabszam += 1
    n += 1

print("3 al osztható számok száma:", darabszam)