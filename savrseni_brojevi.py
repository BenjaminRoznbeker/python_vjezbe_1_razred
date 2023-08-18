#Napravi program koji ispisuje sve savršene brojeve do nekog broja.
#(Napomena: Savršeni broj je broj koji je jednak zbroju svojih djelitelja koji su manji od
#njega, npr. 6=1+2+3, 28=1+2+4+7+14)

broj = int(input('broj: '))
zbroj= 0
for i in range(1,broj+1):
    for j in range(i, 0, -1):
        if i % j == 0:
            zbroj += j
    print(zbroj)
    zbroj = 0
