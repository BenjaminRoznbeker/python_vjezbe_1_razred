broj = int(input("dvoznamekasti broj: "))

prva_znamenka = int(broj/10)
druga_znamenka = broj - 10*prva_znamenka

print(f"Prva znamenka: {prva_znamenka}")
print(f"Druga znamenka: {druga_znamenka}")