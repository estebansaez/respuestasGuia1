#Pregunta 5, guia 1

def calcular_producto_modular(hora1, hora2):
    # Calcular el producto de las horas y aplicar módulo 24
    producto_horas = (hora1 * hora2) % 24
    return producto_horas

# Ejemplo de uso
hora1 = 14  # 14:00
hora2 = 8   # 08:00
resultado = calcular_producto_modular(hora1, hora2)
print("El producto modular de", hora1, "y", hora2, "es:", resultado)
