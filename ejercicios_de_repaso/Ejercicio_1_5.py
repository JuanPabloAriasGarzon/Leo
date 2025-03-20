# Ejercicio 1.5
'''
Escriba un programa que realice la comprobacion de la division. Recuerde:
Divisor * Cociente + Residuo = Dividendo
Tome como entrada dos numeros, realice la division entre ellos y entregue al usuario
un texto descriptivo con la comprobacion de la division'''

dividendo=int(input("Ingrese el primero numero"))
divisor=int(input("Ingrese el segundo numero"))

#Calculo 
cociente=dividendo/divisor
residuo=dividendo%divisor
divisor*cociente+residuo=dividendo
print(f"La comprobacion de la vision es: {divisor} por {cociente} mas {residuo} es igual a {dividendo}")