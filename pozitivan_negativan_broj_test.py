broj = float(input("broj: "))

if broj > 0:
    print(f'{broj} je pozitivan broj')
elif broj < 0:
    print(f'{broj} je negativan broj')
elif broj == 0:
    print(f'{broj} je jednak nuli')
else:
    print(f'{broj} nije valjan broj')