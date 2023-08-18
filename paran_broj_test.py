broj = int(input('broj: '))

if broj % 2 == 0:
    print(f"{broj} je paran broj")
elif broj % 2 != 0:
    print(f"{broj} nije paran broj")
else:
    print(f"{broj} nije valjan broj")