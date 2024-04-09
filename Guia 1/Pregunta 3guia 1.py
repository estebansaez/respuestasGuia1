#Pregunta 3, guia 1

#Resolver sistema de ecuaciones con aritmetica modular:


def euclides_extendido(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = euclides_extendido(b % a, a)
        return (gcd, y - (b // a) * x, x)

def inverso_modular(a, m):
    gcd, x, y = euclides_extendido(a, m)
    if gcd != 1:
        raise ValueError(f"No existe inverso modular para {a} mod {m}")
    else:
        return x % m

def resolver_sistema_ecuaciones_modular(coeficientes, constantes, modulo):
    n = len(coeficientes)
    soluciones = []
    
    for i in range(n):
        suma = 0
        # Resolver coeficientes * variables ≡ constantes mod m
        for j in range(n):
            suma += coeficientes[i][j] * constantes[j]
        
        # Encontrar el inverso modular del coeficiente
        coeficiente_modular = coeficientes[i][i] % modulo
        inverso = inverso_modular(coeficiente_modular, modulo)
        
        # Calcular la solución para la variable
        solucion_variable = (suma * inverso) % modulo
        soluciones.append(solucion_variable)
    
    return soluciones

# Ejemplo de uso:
coeficientes = [[2, 3], [1, -2]]
constantes = [5, 3]
modulo = 7
soluciones = resolver_sistema_ecuaciones_modular(coeficientes, constantes, modulo)
print("Soluciones:", soluciones)
