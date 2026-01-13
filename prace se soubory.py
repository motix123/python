"""# Zápis do souboru
with open('ukazkovy.txt', 'w', encoding="utf-8") as soubor:
  soubor.write('Toto je ukázkový text.\n',)
  soubor.write('Další řádek textu.\n')

# Čtení ze souboru
with open('ukazkovy.txt', "r") as s:
  obsah = s.read()
  print(obsah)"""



def sito(n):
    n = n + 1
    if n <= 1:
        return []
    
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n, i):
                is_prime[j] = False
    primes = [i for i in range(n) if is_prime[i]]
    return primes
n = int(input("Zadej číslo n:"))
primes = sito(n)

with open('primes.txt', 'w', encoding="utf-8") as soubor:
    soubor.write("Prvočísla v rozsahu " + str(n) + " jsou: " + str(primes))

with open('primes.txt', "r", encoding="utf-8") as s:
    obsah = s.read()
    print(obsah)
