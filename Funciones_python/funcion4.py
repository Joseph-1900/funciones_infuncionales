"""Escriba una función de Python para multiplicar todos los números de una lista. Lista de muestra: (8, 2, 3, -1, 7)Resultado esperado: -336"""

def multiplicar_lista(lista):
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado

numeros = input("Ingresa los números separados por comas: ")

lista_muestra = [int(numero) for numero in numeros.split(',')]
resultado = multiplicar_lista(lista_muestra)
print("Resultado esperado:", resultado)


