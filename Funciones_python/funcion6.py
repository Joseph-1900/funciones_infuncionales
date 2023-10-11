"""Escriba una función de Python para calcular el factorial de un número (un entero no negativo). La función acepta el número como argumento."""

def calcular_factorial(numero):
    if numero < 0:
        return "El factorial no está definido para números negativos."
    elif numero == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        return factorial

numero = int(input("Ingrese m perro un número entero no negativo: "))
resultado = calcular_factorial(numero)
print(f"El factorial de {numero} es: {resultado}")
