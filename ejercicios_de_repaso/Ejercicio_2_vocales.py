'''
Ejercicio 2: Contar Vocales en un String

Problema:
Pedir una frase al usuario y contar cuántas vocales (a, e, i, o, u) tiene.
'''

palabra=input("Ingrese una palabra")

vocales="aeiouAEIOU"
contador_de_vocales=0
for letra in palabra:
    if letra in vocales:
     contador_de_vocales+=1
print(contador_de_vocales)
