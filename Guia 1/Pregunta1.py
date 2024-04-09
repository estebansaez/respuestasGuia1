#Pregunta 1, guia 1

import random

def miller_rabin(n, k=15):
  
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Escribir n - 1 como 2^s * d, donde d es impar
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    # Realizar k iteraciones del test de Miller-Rabin
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Ejemplo de uso:
numero = 221
if miller_rabin(numero):
    print(f"{numero} es probablemente primo.")
else:
    print(f"{numero} es compuesto.")
