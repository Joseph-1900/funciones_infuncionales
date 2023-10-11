"""Escriba una función de Python para sumar todos los números de una lista. Lista de muestras: (8, 2, 3, 0, 7)Resultado esperado: 20."""

def sumar_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

numeros = input("Ingresa los números separados por comas: ")

lista_muestra = [int(numero) for numero in numeros.split(',')]
 
resultado = sumar_lista(lista_muestra)
print("Resultado esperado:", resultado)


