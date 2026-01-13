#euklidovský algoritmus pro výpočet největšího společného dělitele (NSD)

a = int(input("Zadej první číslo: "))
b = int(input("Zadej druhé číslo: "))
if a>b:
    while b!=0:
        a, b = b, a % b
    print("Největší společný dělitel je:",a)
elif b>a:
    while a!=0:
        b, a = a, b % a
    print("Největší společný dělitel je:",b)
else:
    print("Čísla jsou stejná, NSD je:",a)

#eukliduv algoritmus jako funkce

"""def eukliduv_algoritmus(a,b):
    while b!=0:
    
        c=a % b
        a=b
        b=c

        return a"""