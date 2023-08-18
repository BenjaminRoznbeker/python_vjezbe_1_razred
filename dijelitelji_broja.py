broj = int(input('broj: '))

for i in range(broj, 0, -1):
    if broj % i == 0:
        print(i)