n = int(input("koliko brojeva: "))
zbroj = 0

for i in range(n):
    zbroj += int(input('broj: '))

aritmeticka_sredina = zbroj/n
print(aritmeticka_sredina)
