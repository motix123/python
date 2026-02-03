#počítání minima a maxima ze seznamu tří čísel
"""a = int(input("Enter first number: "))
b = int(input("Enter second  number: "))
c = int(input("Enter third number: "))
if a>b and a>c:
    print("The biggest number is:",a)
    if b<=c:
        print("The smallest number is:",b)
    else:
        print("The smallest number is:",c)
elif b>a and b>c:
    print("The biggest number is:",b)
    if a<=c:
        print("The smallest number is:",a)
    else:
        print("The smallest number is:",c)
elif c>a and c>b:
    print("The biggest number is:",c)
    if a<=b:
        print("The smallest number is:",a)
    else:
        print("The smallest number is:",b)
else:
    print("All the numbers are same:",a)"""


# linearni rovnice jako funkce
"""
def linear_fce(y, z):

    if y == 0 and z == 0:
        return "equation has infinite solutions"

    if y == 0 and z != 0:
        return "equation has no solutions"

    fce = -z / y
    return fce"""


# řešení rovnice ax^2 + bx + c = 0 neboli kvadratické rovnice
"""
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a == 0:
    print("that's not a quadratic equation")
    if b == 0 or c == 0:
        print("The equation has infinitely many solutions")
    elif b == 0 and c != 0:
        print("Equation has no solutions")
    else:
        x = -c / b
        print("Solution je x =", x)
elif b != 0 and c != 0 and a != 0:
    D = b ** 2 - 4 * a * c
    if D < 0:
        print("The equation has no solution in the set of real numbers")
    elif D == 0:
        x = -b / (2 * a)
        print("the equation has one double solution x =", x)
    else:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        print("The equation has two distinct solutions x1 =", x1, "a x2 =", x2)
elif b == 0:
    if -c / a < 0:
        print("The equation has no solution in the set of real numbers")
    else:
            x1 = (-c / a) ** 0.5
            x2 = -(-c / a) ** 0.5
            print("The equation has two distinct solutions x1 =", x1, "a x2 =", x2)
elif c == 0:
    x1 = 0
    x2 = -b / a
    print("The equation has two distinct solutions x1 =", x1, "a x2 =", x2)"""


# kvadraticka rovnice jako funkce
"""
    def quadratic_formula(k, l, m):

        if k == 0:
            return linear_fce(b, c)

        D = l ** 2 - 4 * k * m

        if D < 0:
            return "Equation doesn't have an answer"

        if D == 0:
            return [-l / (2 * k)]

        answer_1 = (-l + D ** 0.5) / (2 * k)
        answer_2 = (-l - D ** 0.5) / (2 * k)

        return [answer_1, answer_2]"""


# euklidovský algoritmus pro výpočet největšího společného dělitele (NSD)

"""a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    while b != 0:
            a, b = b, a % b
    print("The greatest common divisor is:", a)
elif b > a:
    while a != 0:
            b, a = a, b % a
    print("The greatest common divisor is:", b)
else:
    print("Numbers are same, NSD je:", a)

# eukliduv algoritmus jako funkce


def Euclidian_algorithms(a, b):
    while b:
        a, b = b, a % b
    return a"""



# eratosthénovo síto složí k nalezení všech prvočísel menších než zadané číslo n jako funkce

"""def sieve(n):
    #Funkce vrátí seznam všech prvočísel menších než n pomocí Eratosthénova síta.
    n = n + 1

    if n <= 1:
        return []

# Vytvoření seznamu pravdivostních hodnot pro čísla od 0 do n

    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False  # 0 a 1 nejsou prvočísla

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False

# Sestavení seznamu prvočísel
    primes = [i for i in range(n) if is_prime[i]]
    return primes"""


# eratosthénovo síto jako skript

"""n = int(input("Enter number n:"))
primes = sieve(n)
print("Prime numbers in the range ", n, "are:", primes)"""


# toto je fce na fibonacci sequence
"""def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


answer = fibonacci(8)
print(answer)"""


# factorial recursive

"""def factorial_rec(n):
    if n == 0:
        return 1
    return n * factorial_rec(n - 1)"""


# factorial

"""def factorial(n):
    answer =1
    for num in range(n, n + 1):
        answer = answer * num
    return answer"""

class Zeton:
  def __init__(self,value):
    self.__value = value

try:
  Z1 = Zeton(10)
  expected_var = "value"
  all_vars = dir(Z1)
  if "_Zeton__"+expected_var in all_vars:
    print("Is OK")
  elif expected_var in all_vars:
    print(expected_var, "no hidden atribut")
  elif "_"+expected_var in all_vars:
    print("_"+expected_var, "no hidden atribut")
  else:
    print(expected_var, "Error 404")
except NameError as e:
  print("Class Zeton not found")
except TypeError as e:
  print("Class Zeton should receive one argument while creating  ")