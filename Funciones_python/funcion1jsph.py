"""Escriba una función de Python para encontrar el máximo de tres números."""

numero1 = int(input("1. digite el primer numero: "))
numero2 = int(input("2. digite el segundo numero: "))
numero3 = int(input("3. digite el tercer numero: "))

def encontrar_el_maximo(a,b,c):
    maximo = max(a,b,c)
    return maximo

resultado = encontrar_el_maximo(numero1, numero2, numero3)


print(F"El numero maximo es: {resultado}")
print("Gracias por usar Industrias Joseph, no vuelva nunca :)")