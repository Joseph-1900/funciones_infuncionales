"""Escriba un programa para calcular las áreas de las figuras geométricas utilizando una función para cada área. """

import math

def calcular_area_cuadrado(lado):
    return lado ** 2

def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def main():
    print("Aqui se va a Calcular las áreas de figuras geométricas")
    
    figura = input("Ingrese papi la figura de la que deseas calcular, 1 cuadrado, 2 triangulo y 3 circulo: ").lower()
    
    if figura == "1":
        lado = float(input("Ingresa la longitud de un lado del cuadrado: "))
        area = calcular_area_cuadrado(lado)
    elif figura == "2":
        base = float(input("Ingresa la longitud de la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        area = calcular_area_triangulo(base, altura)
    elif figura == "3":
        radio = float(input("Ingresa el radio del círculo: "))
        area = calcular_area_circulo(radio)
    else:
        print("Figura no reconocida. Por favor, ingresa 'cuadrado', 'triángulo' o 'círculo'.")
        return

    print(f"El área del {figura} es: {area:.2f}")

if __name__ == "__main__":
    main()
