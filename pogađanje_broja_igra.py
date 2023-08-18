import random
pokusaji = 0
print('Ovo je igra u kojoj cete pogadjati broj')
random_start = int(input('Broj koji cete pogadjati je izmedju(izaberite broj): '))
random_stop = int(input(f'Broj koji cete pogadjati je izmedju {random_start} i (izaberite broj): '))
broj_pokusaja = int(input('broj pokusaja koji cete imati je(izaberite broj): '))

broj = random.randint(random_start, random_stop)

pbroj = int(input('Pogodite broj: '))
while broj_pokusaja > 0 and pbroj != broj:
    broj_pokusaja -= 1
    pokusaji += 1
    if pbroj == broj:
        print(f"BRAVO!, pogodili ste broj {broj} u {pokusaji} pokusaja")
    else:
        print(f'{pbroj} nije broj koji sam smislio')
        print(f'ostalo vam je {broj_pokusaja} pokusaja')
    pbroj = int(input('Pogodite broj: '))

if broj_pokusaja == 0:
    print('Nazalost niste uspijeli pogoditi broj u zadanim pokusajima')
    print(f'broj koji sam smislio je {broj}')
