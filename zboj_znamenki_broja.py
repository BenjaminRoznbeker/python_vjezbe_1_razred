broj = int(input("Broj: "))
zbroj = 0
while broj > 0:
    zbroj += broj % 10
    broj //= 10

print(zbroj)