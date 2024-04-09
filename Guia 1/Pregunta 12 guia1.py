#Pregunta 12 guia1

def euclides_extendido(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = euclides_extendido(b, a % b)
        return gcd, y, x - (a // b) * y

def calcMcd(a, b):
    mcd, _, _ = euclides_extendido(a, b)
    return mcd

# Ejemplo de uso
num1 = 123456789012345678901234567890
num2 = 87654321098765432109876543210
print("El MCD de", num1, "y", num2, "es:", calcMcd(num1, num2))
