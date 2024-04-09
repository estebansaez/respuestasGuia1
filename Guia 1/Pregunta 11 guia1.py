#Pregunta 11 guia1

def euclides(a, b):
    while b:
        a, b = b, a % b
    return a

def son_congruentes_modulo(a, b, m):
    if euclides(a, m) == euclides(b,m):
        return True
    else:
        return False

# Ejemplo de uso
a = 2
b = 22
m = 6

if son_congruentes_modulo(a, b, m):
    print(f"{a} y {b} son congruentes módulo {m}.")
else:
    print(f"{a} y {b} no son congruentes módulo {m}.")
