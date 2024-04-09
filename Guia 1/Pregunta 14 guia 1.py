#Pregunta 14 guia 1

def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def son_coprimos(a, b):
    return mcd(a, b) == 1

# Ejemplo de uso
num1 = 15
num2 = 30
if son_coprimos(num1, num2):
    print(f"{num1} y {num2} son coprimos.")
else:
    print(f"{num1} y {num2} no son coprimos.")
