#Pregunta 10 guia1

def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mcm(a, b):
    return (a * b) // mcd(a, b)

def mcm_de_varios_numeros(numeros):
    resultado = 1
    for num in numeros:
        resultado = mcm(resultado, num)
    return resultado

# Ejemplo de uso
numeros = [15,20,25,30]
print("El mínimo común múltiplo de", numeros, "es:", mcm_de_varios_numeros(numeros))
