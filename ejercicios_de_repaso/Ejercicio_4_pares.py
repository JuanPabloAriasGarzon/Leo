'''
Ejercicio 4: Contar Números Pares en una Lista

Problema:
Solicitar 5 números al usuario, almacenarlos en una lista y contar cuántos son pares.
'''

mi_lista=[3,2,4,5,2]
cantidad_de_numeros_pares=0
for numero in mi_lista:
    if numero%2==0:
        cantidad_de_numeros_pares+=1
print(cantidad_de_numeros_pares)
