"""Escriba un programa Python para invertir una cadena.Cadena de ejemplo: "1234abcd" Resultado esperado: "dcba4321"""

def invertir_cadena(cadena):
    return cadena[::-1]

cadena = input("Ingresa una cadena: ")

resultado = invertir_cadena(cadena)
print("Resultado esperado:", resultado)
