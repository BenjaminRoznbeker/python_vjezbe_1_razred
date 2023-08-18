broj = int(input('broj: '))
testbroj = broj
naopaki_broj = 0
broj_znamenki = 0
g = 0
while int(testbroj) > 0:
    broj_znamenki += 1
    testbroj = int(testbroj/10)


for i in range(broj_znamenki):
    broj_znamenki -= 1
    naopaki_broj += (10**broj_znamenki) * int(((broj-g) / (10 ** (i))) % (10))
    g = int(((broj-g) / (10 ** (i))) % (10))

print(naopaki_broj)

#ILI broj = int(input("Broj: "))
#while broj > 0:
#    print(broj % 10)
#    broj //= 10