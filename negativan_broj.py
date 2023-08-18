#Napiši program koji, ukoliko je uneseni broj x negativan,
# pretvara ga u pozitivan a u suprotnom ispisuje ((x+5)/2)-3x**2

broj = int(input('broj: '))
if broj < 0:
    print(broj*-1)
else:
    print(((broj+5)/2)-3*broj**2)