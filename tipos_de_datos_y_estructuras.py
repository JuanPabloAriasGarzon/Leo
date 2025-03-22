'''
Tipos de datos
<class 'int'>: Identifica que la variable es un número entero.
<class 'float'>: Identifica que la variable es un número decimal.
<class 'str'>: Identifica que la variable es una cadena de texto.
<class 'bool'>: Identifica que la variable es un valor booleano (True o False).
'''

# x=True #True y False son palabras reservadas del lenguaje
# print(type(x))

# autor='Juan'
# print(type(autor))

# carro="This is John' car"
# modelo='2003'
# print(carro+' '+modelo) # El simbolo + permite concatenar textos en Python

'''
Tipos de estructuras de datos y metodos
1-Conjuntos +
2-Tuplas ++
3-Listas  +++
4-Diccionarios  +++
'''

#Uso de conjuntos
'''
Los conjuntos o sets son estructuras especiales que permiten almacenar 
un grupo de elementos. Cuando el odern de los elementos no es importante
podemos utilizar sets en python. Ademas esta estructura no permite elementos duplicados.

como se definen: {, , , , ,}'''
# set1={"a","b",'c','d'}
# print(type(set1))

# set2={"e",'f',"g"}
#metodos para el tratamiento de conjuntos
# set1.union()
# Union de conjunto
# print(set1.union(set2))

# set3={"a","b","c","c","d","d"}
# print(set3)
# set4=set3.union(set1)
# print(set4)

#Interseccion de conjuntos con python
# set5={"f","w","a","b"}
# print(set5.intersection(set1))

# set5.remove("w")
# print(set5)

# set4.add("a")
# print(set4)

# print(set4.issuperset(set5))
# set4.issuperset(set5)

# print(set1.difference(set5))

# set6={"juan", 5, True}
# set7={"juan", 5, True,"laura"}
# print(set6.issuperset(set7)) # False
# print(set7.issuperset(set6)) # True

# print(set6.issubset(set7)) # True
# print(set7.issubset(set6)) # False

'''
Uso de tuplas
Son estructuras de datos rigidos, que no permiten muchos metodos
se usan cuando queremos resguardar la informacion (inmutable)
como se definen: (, , , , ,)
si permiten valores duplicados
<class 'tuple'>'
'''
tupla1=(1,1,1,1,1,1,2,3,4,5)
#       0 1 2 3 4 5 6 7 8 9
# print(type(tupla1))

# Metodos
# Count: permite contar la cantidad de veces que se repite un valor en la tupla 
conteo=tupla1.count(1)
# print(conteo)

# Index: permite obtener el indice de un valor en la tupla
indice=tupla1.index(5)
# print(indice)

'''
PYTHON ES UN LENGUAJE INDEXADO DESDE 0
Siempre el primer elemento de una estructura de datos en python es el 0,la posicion 
inicial es el 0
indice<->posicion 
'''

'''
Uso de listas
Las listas son estructuras de datos que almacenan elementos de manera ordenada y
mutable. Son un tipo de nativo del lengueje python'
como se definen: [, , , , , ,]
si permiten valores duplicados
<class 'list'>
puede contener cualquier tipo de dato, numeros, letras , o incluso otras listas
'''

lista1=[8,9,7,5,4,10]
# print(type(lista1))

lista2=[["Jhon","Alejandro","Lewin"],["Isabel","Juan","Daniel"]]
# print(type(lista2)) # <class 'list'>

# Metodos
#count
lista1.count(9)
# print(lista1.count(14))

#reverse
lista1.reverse()
# print(lista1)

#append
lista1.append(20)
# print(lista1)


# print(lista1.remove(7))
# print(lista1)

#Acceder a un elemento de una lista
# print(lista2[0][1])

#sort 

lista1.sort() #en este caso ordena ascendentemente
# print(lista1)

lista1.sort(reverse=True) #en este caso ordena descendentemente
# print(lista1)
