# řešení rovnice ax + b = 0 neboli lineární rovnice s jednou neznámou

a = int(input("Zadej první číslo: "))
b = int(input("Zadej druhé číslo: "))
if a==0 or b==0:
    print("rovnice má nekonečně mnoho řešení")
elif a==0 and b!=0:
    print("rovnice nemá řešení")
else:
    x = -b/a
    print("řešení rovnice je x =",x)

#linearni rovnice jako funkce

def linearni_funkce(b,c):

    if b==0 and c==0:
        return "rovnice má nekonečně mnoho řešení"
    
    if b==0 and c!=0:
        return "rovnice nemá řešení"
    
    x= -c/b
    return x

# řešení rovnice ax^2 + bx + c = 0 neboli kvadratické rovnice

a = int(input("Zadej první číslo: "))
b = int(input("Zadej druhé číslo: "))
c = int(input("Zadej třetí číslo: "))
if a==0:
    print("to není kvadratická rovnice")
    if b==0 or c==0:
        print("rovnice má nekonečně mnoho řešení")
    elif b==0 and c!=0:
        print("rovnice nemá řešení")
    else:
        x = -c/b
        print("řešení rovnice je x =",x)
elif b!=0 and c!=0 and a!=0:
    D =b**2 - 4*a*c
    if D<0:          
        print("rovnice nemá řešení v oboru reálných čísel")
    elif D==0:
        x = -b/(2*a)
        print("rovnice má jedno dvojnásobné řešení x =",x) 
    else:
        x1 = (-b + D**0.5)/(2*a)
        x2 = (-b - D**0.5)/(2*a)
        print("rovnice má dvě různá řešení x1 =",x1,"a x2 =",x2)
elif b==0:
    if -c/a < 0:
        print("rovnice nemá řešení v oboru reálných čísel")
    else:
        x1 = (-c/a)**0.5
        x2 = -(-c/a)**0.5
        print("rovnice má dvě různá řešení x1 =",x1,"a x2 =",x2)
elif c==0:
    x1 = 0
    x2 = -b/a
    print("rovnice má dvě různá řešení x1 =",x1,"a x2 =",x2)


#kvadraticka rovnice jako funkce

def kvadraticka_rovnice(a,b,c):

    if a==0:
        return linearni_funkce(b,c)
    
    D = b**2 - 4*a*c

    if D<0:
        return "rovnice nemá řešení"
    
    if D==0:
       return [-b/(2*a)]
    
    x1=(-b + D**0.5)/(2*a)
    x2=(-b - D**0.5)/(2*a)

    return [x1,x2]
        


