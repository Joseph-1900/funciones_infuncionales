"""Escriba una función de Python que compruebe si una cadena pasada es palíndromo o no. Una palabra o frase que es palíndromo se lee igual de izquierda a derecha que de derecha a izquierda. Por ejemplo: Ana, Anita lava la tina. """

frase = input("ingrse la palabra o frase del palindromo: ")
 
frase = frase.replace(" ", "") 
frase = frase.lower()

frase_invertida = frase[::-1]
print(frase_invertida)