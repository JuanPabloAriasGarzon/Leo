'''
Ejercicio 6: Clasificar Números en Positivos y Negativos

Problema:
Pedir 6 números al usuario y separarlos en positivos y negativos.
'''
mi_lista=[-8,-3,4,2,-5,6]
cantidad_de_positivos:0
cantidad_de_negativos:0

for numero in mi_lista:
    if numero<0:
        cantidad_de_negativos+=1
    else:
        cantidad_de_positivos+=1

print(cantidad_de_positivos)
print(cantidad_de_negativos)