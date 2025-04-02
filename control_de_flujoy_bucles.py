'''
condicional "if then else"
"si se cumple la condicion entonces 
se realiza la operacion de lo contario,
se realiza otra operacion(opcionalmente)"
'''

x = 100
y = 200
#if x > y: #condicion
#   print("x es mayor que y") #operacion
    
#uso de control if-else
#else: significa "de lo contrario"

w= 500
z= 2000
# if w > z: #condicion
#    print("w es mayor que z") #operacion 
# else:                         #de lo contrario
#    print("z es mayor que w") #operacion

#uso de control if-elif-else

w= 500
z= 2000
#if w > z: #condicion
#    print("w es mayor que z") #operacion
#elif w==500: #condicion 2...
#    print("w es igual a 500") 
#elif w==100: #condicion 3...
#    print("w es igual a 100")
#else:                         #de lo contrario
#    print("w es menor que z") #operacion
'''
elif sirve para evaluar multiples condiciones
'''

#uso de if anidados
#usuario=input("ingrese su usuario: ")
#password=input("ingrese su contraseña: ")

# if usuario=="andres": #condicion 1 se cumple?
#     if password=="1234": #condicion 2 se cumple?
#         print("usuario puede acceder")
#     else: 
#         print("contraseña incorrecta")
# else: 
#     print("usuario incorrecto")

usuario=input("ingrese su usuario: ")
password=input("ingrese su contraseña: ")
#print(len(usuario))
#print(password.isnumeric())

if len(usuario)==5 and password.isnumeric(): #condicion 1 se cumple?
         print("usuario puede acceder")
else: 
     print("usuario o contraseña incorrecto")

