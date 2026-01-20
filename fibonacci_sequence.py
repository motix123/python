#toto je fce na fibonacci sequence
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)


answer = fibonacci(8)
print(answer)
