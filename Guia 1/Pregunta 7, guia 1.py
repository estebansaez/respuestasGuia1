#Pregunta 7, guia 1

#Función para verificar si dos números son primos
def es_primo(numero):
    
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True    

#Funcion para calcular primo1 mod primo2
def calcular_modulo_primos(primo1, primo2):
    
    if not es_primo(primo1) and not es_primo(primo2):
        print("Ambos números no son primos.")
    elif not es_primo(primo1):
        print(f"{primo1} no es primo.")
    elif not es_primo(primo2):
        print(f"{primo2} no es primo.")
    else:
        resultado = primo1 % primo2
        print(f"El resultado de {primo1} mod {primo2} es: {resultado}")

# Ejemplo de uso
calcular_modulo_primos(17, 5)  # Ejemplo con números primos
calcular_modulo_primos(20, 5)  # Ejemplo con número no primo (20)
calcular_modulo_primos(17, 6)  # Ejemplo con un número no primo (6)
calcular_modulo_primos(20, 6)  # Ejemplo con ambos números no primos
