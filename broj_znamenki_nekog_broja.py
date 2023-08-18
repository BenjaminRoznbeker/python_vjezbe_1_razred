def broj_znamenki_broja(n):
    broj_znamenki = 0
    while int(n) > 0:
        broj_znamenki += 1
        n = int(n/10)
    print(broj_znamenki)

broj = int(input('broj: '))
broj_znamenki_broja(broj)