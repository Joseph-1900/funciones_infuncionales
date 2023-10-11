"""Escriba una función de Python para comprobar si un número cae en un rango determinado."""

def en_rango(numero, rango_inicio, rango_fin):
    if numero >= rango_inicio and numero <= rango_fin:
        return True
    else:
        return False

numero = float(input("Ingresa un número: "))
rango_inicio = float(input("Ingresa el límite inferior del rango: "))
rango_fin = float(input("Ingresa el límite superior del rango: "))

if en_rango(numero, rango_inicio, rango_fin):
    print(f"El número {numero} está en el rango [{rango_inicio}, {rango_fin}].")
else:
    print(f"El número {numero} NO está en el rango [{rango_inicio}, {rango_fin}].")
