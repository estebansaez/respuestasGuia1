#Pregunta 6, guia1

import math
#Encuentrar el inverso modular de 'a' módulo 'm', donde 'a' es primo y 'm' es un número grande.
def encontrar_inverso_modular(a, m):
    # Verificar si 'a' y 'm' son coprimos
    if math.gcd(a, m) != 1:
        raise ValueError("El número 'a' no es coprimo con el módulo 'm'.")

    # Algoritmo extendido de Euclides para encontrar el inverso modular
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0

    # Asegurar que el inverso esté en el rango [0, m)
    if x1 < 0:
        x1 += m0

    return x1

# Ejemplo de uso
a = 5
m = 995454353

# Calcular el inverso modular de 'a' módulo 'm'
inverso = encontrar_inverso_modular(a, m)
print(f"El inverso modular de {a} módulo {m} es: {inverso}")
