'''
clasificar los dias de la semana
'''

dia=input("Ingrese un dia de la semana: ") 
match dia:
    case "martes" | "miercoles" | "jueves" | "viernes":
        print("Dia laboral")
    case "lunes":
        print("Festivo")
    case "sabado" | "domingo":
        print("Fin de semana")
    case _:
        print("Dia no valido")
