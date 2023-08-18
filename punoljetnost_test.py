godine = float(input("Godine: "))
drzava = input("Drzava stanovanja (USA ili HR): ")

if drzava.upper() == "USA" and godine >= 16 or drzava.upper() == "HR" and godine >= 18:
    print("Osoba je punoljetna")
else:
    print("Osoba nije punoljetna")