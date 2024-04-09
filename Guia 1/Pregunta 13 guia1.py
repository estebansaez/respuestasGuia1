#Pregunta 13 guia1

def euclides_extendido(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = euclides_extendido(b, a % b)
        return gcd, y, x - (a // b) * y

def inversa_modular(a, m):
    gcd, x, _ = euclides_extendido(a, m)
    if gcd != 1:
        raise ValueError(f"No existe la inversa modular de {a} respecto a {m} porque {a} y {m} no son coprimos.")
    else:
        return x % m

# Ejemplo de uso
a = 9
m = 6
print(f"La inversa modular de {a} respecto a {m} es: {inversa_modular(a, m)}")
