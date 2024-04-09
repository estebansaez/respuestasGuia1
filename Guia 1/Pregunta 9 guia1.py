#Pregunta 9 guia1

def encontrar_factores_primos(n):
    factores = []

    # Encuentra el factor 2 repetidamente
    while n % 2 == 0:
        factores.append(2)
        n //= 2

    # Encuentra los factores impares
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factores.append(i)
            n //= i

    # Si n es un número primo mayor que 2, añádelo a los factores
    if n > 2:
        factores.append(n)

    return factores

# Ejemplo de uso
numero = 101520
print("Factores primos de", numero, ":", encontrar_factores_primos(numero))
