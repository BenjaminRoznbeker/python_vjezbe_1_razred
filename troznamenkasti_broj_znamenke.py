broj = int(input('Troznamenkasti broj: '))

zn1 = int(broj/100)
zn2 = int((broj - 100*zn1)/10)
zn3 = int(broj - 100*zn1 - 10*zn2)

print(zn1)
print(zn2)
print(zn3)