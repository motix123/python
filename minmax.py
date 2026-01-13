#počítání minima a maxima ze seznamu tří čísel
a = int(input("Zadej první číslo: "))
b = int(input("Zadej druhé číslo: "))   
c = int(input("Zadej třetí číslo: "))
if a>b and a>c:
    print("Největší číslo je:",a)
    if b<=c:
        print("Nejmenší číslo je:",b)
    else:
        print("Nejmenší číslo je:",c)
elif b>a and b>c:
    print("Největší číslo je:",b)
    if a<=c:
        print("Nejmenší číslo je:",a)
    else:
        print("Nejmenší číslo je:",c)
elif c>a and c>b:
    print("Největší číslo je:",c)
    if a<=b:
        print("Nejmenší číslo je:",a)
    else:
        print("Nejmenší číslo je:",b)
else:
    print("Všechna čísla jsou stejná:",a)