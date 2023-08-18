broj = int(input('Koliko brojeva: '))
parno = 0
neparno = 0

for i in range(broj):
    if int(input("Broj: ")) % 2 == 0:
        parno += 1
    else:
        neparno += 1

print(f'{parno} parna broja')
print(f'{neparno} neparna broja')