"""Escriba una función de Python que tome una lista y devuelva una nueva lista con elementos únicos de la primera lista. """

def elementos_unicos(lista):
    lista_unicos = []
    for elemento in lista:
        if elemento not in lista_unicos:
            lista_unicos.append(elemento)
    return lista_unicos

entrada = input("Ingresa elementos separados por comas: ")
lista = entrada.split(',')

lista_unicos = elementos_unicos(lista)
print("Elementos únicos en la lista:", lista_unicos)
