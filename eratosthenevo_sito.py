# eratosthénovo síto složí k nalezení všech prvočísel menších než zadané číslo n jako funkce

def sito(n):
    """Funkce vrátí seznam všech prvočísel menších než n pomocí Eratosthénova síta."""
    n = n + 1

    if n <= 1:
        return []
    
    # Vytvoření seznamu pravdivostních hodnot pro čísla od 0 do n

    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False  # 0 a 1 nejsou prvočísla

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n, i):
                is_prime[j] = False

    # Sestavení seznamu prvočísel
    primes = [i for i in range(n) if is_prime[i]]
    return primes

#eratosthénovo síto jako skript

n = int(input("Zadej číslo n:"))
primes = sito(n)
print("Prvočísla v rozsahu ", n, "jsou:", primes)
