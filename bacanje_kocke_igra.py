import random

print('Ovo je igra u kojoj 1-4 igraca baca kocku')
print('igrac dobiva bod za svaki broj na kockici.')
print('Igra zavrsava kad se dobiju dvije jedinice za redom')
broj_igraca = int(input('Koliko igraca zelis(1-4): '))

igra = {
    "broj_igraca": broj_igraca,
    "bodovi" : [0]*broj_igraca,
    "proslo_bacanje" : 0,
    "krug" : 0
}


def bacanje_kocke(igra):
    igra["krug"] += 1
    for igrac in range(broj_igraca):
        bacanje = random.randint(1, 6)
        igra["bodovi"][igrac] += bacanje
        print(f'Igrac {igrac+1} je dobio {bacanje}')
        if bacanje == 1 and igra["proslo_bacanje"] == 1:
            return igra
        igra["proslo_bacanje"] = bacanje
    return bacanje_kocke(igra)

igra = bacanje_kocke(igra)
print(f'Igrac {igra["bodovi"].index(max(igra["bodovi"]))+1} je pobijedio sa {max(igra["bodovi"])} bodova')
print(f'Odigralo se {igra["krug"]} krugova')



