broj = int(input("dvoznamekasti broj: "))

prva_znamenka = int(broj/10)
druga_znamenka = broj - 10*prva_znamenka

if prva_znamenka == 1 or 0 and druga_znamenka == 1 or 0:
    print(f'{broj} je binaran broj')
else:
    print(broj)