from decimal import Decimal

def exp_rapida(a, b, m):

    result = 1
    a = a % m  # Reduce a modulo m si es necesario
    while b > 0:
        # Si b es impar, multiplicar result por a
        if b % 2 == 1:
            result = (result * a) % m
        # Dividir b por 2 y elevar a al cuadrado
        a = (a * a) % m
        b //= 2
    return result

# Ejemplo de uso:
a = 7
b = 92
m = 17


resultado = exp_rapida(a, b, m)
print(f"{a}^{b} mod {m} = {resultado}")
