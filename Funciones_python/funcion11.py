"""Escriba un programa Python para imprimir los números pares de una lista determinada."""

def imprimir_pares(lista):
    for numero in lista:
        if numero % 2 == 0:
            print(numero)

entrada = input("Ingresa elementos separados por comas: ")
lista = [int(x) for x in entrada.split(',')]

print("Números pares en la lista:")
imprimir_pares(lista)
