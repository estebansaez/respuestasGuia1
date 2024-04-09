#Pregunta 8, guia 1

def mcd_polinomios(polinomio1, polinomio2):
    """Función para calcular el máximo común divisor (MCD) de dos polinomios."""
    
    def polinomio_mcd(a, b):
        """Función interna para calcular el MCD de dos polinomios."""
        while len(b) > 0:
            a, b = b, polinomio_restante(a, b)
        return a

    def polinomio_restante(dividendo, divisor):
        """Función interna para calcular el resto de la división de dos polinomios."""
        while len(dividendo) >= len(divisor) and divisor[-1] != 0:
            factor = dividendo[-1] // divisor[-1]
            divisor_desplazado = [0] * (len(dividendo) - len(divisor)) + [term * factor for term in divisor]
            dividendo = [x - y for x, y in zip(dividendo, divisor_desplazado)]
            while dividendo and dividendo[-1] == 0:
                dividendo.pop()
        return dividendo

    # Eliminar ceros redundantes al final de los polinomios
    while polinomio1 and polinomio1[-1] == 0:
        polinomio1.pop()
    while polinomio2 and polinomio2[-1] == 0:
        polinomio2.pop()

    # Calcular el MCD de los polinomios
    return polinomio_mcd(polinomio1, polinomio2)

# Ejemplo de uso
polinomio1 = [6, -5, 1]  # Representa el polinomio 6x^2 - 5x + 1
polinomio2 = [9, -6, 1]  # Representa el polinomio 9x^2 - 6x + 1

resultado = mcd_polinomios(polinomio1, polinomio2)
print("El máximo común divisor de los polinomios es:", resultado)
