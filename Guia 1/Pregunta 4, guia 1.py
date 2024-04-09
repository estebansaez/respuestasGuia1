#Pregunta 4, guia 1

def suma_fechas_modular(fecha1, fecha2):
    # Suma las fechas
    suma_total = fecha1 + fecha2
    # Calcula el residuo de la división entre 7
    resultado_modular = suma_total % 7
    return resultado_modular

# Ejemplo de uso:
fecha1 = 5
fecha2 = 10
resultado = suma_fechas_modular(fecha1, fecha2)
print("La suma de las fechas de forma modular es:", resultado)
